# Manim ile video üretim hattı — araştırma notu

Bilet: `../issues/03-manim-video-uretim-hatti.md` · Tarih: 2026-11-01 · Yalnızca okuma yapıldı, hiçbir şey kurulmadı.

## Türkçe özet

- **Motor: Manim Community Edition (CE).** CE aktif olarak bakılıyor: v0.22.1 27 Ekim 2026'da çıktı ve Python ≥3.11 istiyor. ManimGL'in PyPI'deki son sürümü 1.7.2 (Aralık 2024). ManimGL deposuna commit gelmeye devam ediyor, ama sürümler arasındaki kırıcı değişiklikler belgelenmiyor. Akademik ajanlar da (Code2Video, ManiBench) CE'yi hedefliyor. LLM'lerin en sık hatası GL ve CE API'lerini karıştırmak, bu yüzden tek sürüme sabitlenmek şart.
- **Kurulum (Omarchy/Arch):** `pacman -S base-devel cairo pango`, ardından `uv add manim`, kontrol için `manim checkhealth`. LaTeX yalnızca formül için gerekli (TeX Live önerilir). Türkçe düz metin LaTeX'e değil Pango'ya giden `Text` ile yazılır. Arch resmi depolarında manim paketi yok. Alternatif olarak Docker imajı minimal TeX Live ile geliyor. Cairo varsayılan ve CPU'da çalışan renderer, 3090'lar gerekmez.
- **LLM güvenilirliği:** Tek atışta zayıf, döngüyle iyi. TheoremExplainAgent'ta o3-mini için başarı, hata→düzeltme döngüsü olmadan %3–7, en fazla 5 denemeyle %91–96. ManiBench'te (12 problemlik pilot) Claude-Sonnet-4 tek atışta %66.7 render edebildi. Tipik hatalar: uydurma veya eski API (`ShowCreation`, `CONFIG`), LaTeX sözdizimi ve layout (üst üste binme, kadraj dışı). Çalışan desen şu: plan → kod → düşük kalitede render → kare/kontakt sayfası çıkar → VLM (Claude kendisi) incele → düzelt.
- **Seslendirme:** `manim-voiceover` v0.4.0 (Haziran 2026) Gemini, Azure, ElevenLabs, OpenAI, gTTS, pyttsx3 ve kendi sesini kaydetmeyi destekliyor. Türkçe seçenekler:
  - Azure: Emel ve Ahmet sesleri var, ücretsiz kotası ayda 0.5M karakter.
  - Gemini 3.8 Flash TTS: Türkçe destekliyor, 10 sn ses ≈ $0.00225.
  - ElevenLabs Multilingual v2: 1K karakter $0.08.
  - Yerel seçenekler: XTTS-v2 (CPML lisans), Chatterbox Multilingual (MIT) ve Piper `tr_TR-dfki`.
  
  5 dakikalık bir video bulutta birkaç sent ile birkaç kuruş arası tutar. Altyazı için Manim'in `add_subcaption` özelliği yeterli.
- **Ünite içine gömme:** Yerel markdown'da `<video src="...mp4" controls>` ya da Obsidian'da `![[x.mp4]]` kullanılabilir. Notebook'ta `%%manim` veya `IPython.display.Video` çalışır. GitHub'a yüklemede ücretsiz planda video başına 10 MB sınırı var ve H.264 öneriliyor.
- **Süre (tahmin):** 2–5 dakikalık bir kavram videosu, ilk birkaçında insan gözetimiyle yaklaşık 2–4 saat sürer. Şablon ve stil kütüphanesi oturunca yaklaşık 1–2 saate iner. Makalelerde salt ajan süresi video başına yaklaşık 19–40 dakika, insan incelemesi bunun dışında.

---

## 1. Manim Community Edition vs ManimGL

| | Manim CE | ManimGL (3b1b) |
|---|---|---|
| Maintenance | Regular releases. 0.22.1 (Oct 27 2026), 0.22.0 (Oct 8 2026), 0.21.0 (Aug 10 2026). Requires Python ≥3.11. [PyPI](https://pypi.org/project/manim/#history) | Last PyPI release 1.7.2 (Dec 13 2024). [PyPI](https://pypi.org/project/manimgl/#history) Repo still gets commits; last one seen 2026-09-09 via GitHub API, `repos/3b1b/manim/commits`. [repo](https://github.com/3b1b/manim) |
| Positioning | Community fork from 2020, "more stable, better tested". [3b1b README](https://github.com/3b1b/manim). Recommended for beginners, better documented. [CE FAQ](https://docs.manim.community/en/stable/faq/installation.html) | "More experimental features and breaking changes between versions are not documented". [CE FAQ](https://docs.manim.community/en/stable/faq/installation.html) |
| Requirements | Linux needs a C compiler, Python headers, pkg-config, and Cairo and Pango with their dev headers. Arch: `sudo pacman -Syu base-devel cairo pango`, then `uv add manim`, then `uv run manim checkhealth`. [CE install](https://docs.manim.community/en/stable/installation/uv.html) | Python ≥3.10, FFmpeg, OpenGL, LaTeX (optional), Pango dev headers. [3b1b README](https://github.com/3b1b/manim) |
| Renderer | Cairo (default, CPU) or OpenGL (`--renderer`). [CLI config](https://docs.manim.community/en/stable/guides/configuration.html). The OpenGL path is still being fixed: v0.22.0 found OpenGL code paths that had never run (#4929). [releases](https://github.com/ManimCommunity/manim/releases) | OpenGL only |

Further install notes:

- LaTeX is optional. "In general we recommend to install a TeX Live distribution". TinyTeX with a listed package set is the minimal alternative. [CE install](https://docs.manim.community/en/stable/installation/uv.html)
- For text without math, use `Text` (Pango), which renders non-Latin scripts directly. Fonts must be known to Pango. [Using text](https://docs.manim.community/en/stable/guides/using_text.html) So Turkish characters (ş, ğ, ı) go into `Text`, and `MathTex` is used only for formulas.
- Arch has no official `manim` package (0 results). [archlinux.org](https://archlinux.org/packages/?q=manim) Use uv/pip as above.
- Docker image `manimcommunity/manim` ships a minimal TeX Live. Run with `docker run --rm -it -v "$PWD:/manim" --user="$(id -u):$(id -g)" manimcommunity/manim manim -qm file.py Scene`. [Docker docs](https://docs.manim.community/en/stable/installation/docker.html) This is a fallback if native install on Omarchy is painful.

Render controls that matter for an agent loop: [CLI config](https://docs.manim.community/en/stable/guides/configuration.html)

- Quality presets: `-ql` is 480p15, `-qm` 720p30, `-qh` 1080p60, `-qk` 2160p60.
- `-s` saves only the last frame as PNG. `--format png-sequence` writes every frame. `-n start,end` renders a subrange of animations.
- `--save_sections` writes per-section videos.

**Render times:** I found no authoritative benchmark. A search turned up only anecdotal or inconsistent numbers and advised measuring your own scene. [flyingframes](https://flyingframes.readthedocs.io/en/latest/ch8.html) Frame arithmetic (my calculation, not a source):

- A 3-minute video at `-qh` is 10,800 frames.
- The same video at `-ql` is 2,700 frames at about 1/9 the pixels.

So iterate at `-ql` and render `-qh` once at the end. Expect 1080p60 renders of minutes, not seconds, for 3–5 minute videos. This is a measurement to take in the first prototype.

**Recommendation:** Use CE and pin the version (e.g. `manim==0.22.*`) in the project. Stay on Cairo; the GPUs are not needed.

## 2. How reliably LLMs write Manim code

**TheoremExplainAgent** (ACL 2025, TIGER-Lab). [arXiv abs](https://arxiv.org/abs/2502.19400), [HTML v2](https://arxiv.org/html/2502.19400v2)

- Setup: a planner plus a coding agent, producing videos longer than 5 minutes. TheoremExplainBench has 240 theorems.
- Error-correction loop: up to N=5 retries. o3-mini success went from 7% to 93% on Easy and from 3% to 96% on Hard as N went from 0 to 5.
- Overall success without RAG, by model:

  | Model | Success |
  |---|---|
  | o3-mini | 93.8% |
  | GPT-4o | 55.0% |
  | Gemini 2.0 Flash | 14.6% |
  | Claude 3.5 Sonnet v1 | 2.1% |

- RAG over the Manim docs often hurt, with generic retrievals and more tokens. o3-mini went from 93.8% to 82.1%.
- Failure taxonomy: Manim API hallucination (the largest share), LaTeX rendering errors, and general coding errors. Successful videos still have "minor issues with visual element layout".
- Agent time per video: 1120–2380 s, cost $0.10–$4.67 (Table 5). These are older models.

**ManiBench** (arXiv 2603.13251, Feb 2026). [HTML](https://arxiv.org/html/2603.13251v1)

- Targets Manim CE and catalogs 145 GL→CE incompatibilities.
- Zero-shot executability on a 12-problem pilot:

  | Model | Executability |
  |---|---|
  | Claude-Sonnet-4 | 66.7% |
  | Kimi-K2.5 | 66.7% |
  | Gemini-2.5-Pro | 33.3% |
  | DeepSeek-R1 | 13.9% |

- Failure modes: deprecated APIs (`ShowCreation` instead of `Create`, `CONFIG` classes), hallucinated classes, and missing scene classes.
- Mitigations: few-shot examples were the only thing that raised executability. A forbidden-GL-constructs list in the prompt dropped version-conflict errors to 0%.
- Caveat: small pilot, keyword-based alignment, no human eval.

**Code2Video** (Show Lab NUS; NeurIPS'25 DL4Code workshop, listed at ICML 2026). [arXiv](https://arxiv.org/abs/2510.01174), [PMLR](https://proceedings.mlr.press/v306/chen26bx.html), [repo](https://github.com/showlab/Code2Video)

- Agents: Planner, Coder (with "scope-guided auto-fix"), and Critic (a VLM with visual anchor prompts for layout).
- Reports about 40% improvement over direct code generation.
- The README says the best code quality came with Claude-4-Opus, and the Critic used Gemini-2.5-pro. It targets Manim CE v0.19.0.

**PhysicsSolutionAgent** (arXiv 2601.13453). [arXiv](https://arxiv.org/abs/2601.13453)

- VLM-feedback loop producing physics videos of up to 6 minutes.
- 100% completion and 3.8/5 automated score on 32 videos.
- Still shows "visual layout inconsistencies" and VLM misinterpretation.

**ManimAgent** (arXiv 2606.30296). [arXiv](https://arxiv.org/abs/2606.30296)

- Keyframe VLM scoring plus an episodic memory of "Known Pitfalls".
- Human Pass@1 rises and reflection rounds fall as memory grows.
- This supports keeping a project-local pitfalls file.

**Claude Code skills:**

- [DominikPeters/manim-skill](https://github.com/DominikPeters/manim-skill) renders low-quality PNG frames, builds a contact-sheet grid, and has the agent inspect for overlap, cropping and timing. It keeps a local copy of the CE docs.
- [Yusuke710/manim-skill](https://github.com/Yusuke710/manim-skill) runs plan → code → render → iterate, with a human pasting feedback.
- Claude Code reads images by path. [Claude Code docs](https://code.claude.com/docs/en/common-workflows)
- Generative Manim is an older prompt→Manim suite (GPT-4o/Claude, fine-tuned small models). [repo](https://github.com/360macky/generative-manim)

**Synthesis**

- Typical failure modes, in order:
  1. Non-existent or GL-only API.
  2. LaTeX errors.
  3. Layout problems: overlap, off-frame, text too small.
  4. Pedagogical or semantic drift, where the code runs but the animation is wrong or misleading.
- Items 1–2 are caught by the render loop. Item 3 needs frame inspection. Item 4 needs a human, the learner, to check against the source. This matters especially for technical correctness of KV cache, FSDP and similar topics.

## 3. Voiceover: none, subtitles, or TTS

**manim-voiceover**

- v0.4.0 released 2026-06-14, requires Python ≥3.11. Extras: `azure, elevenlabs, gemini, gtts, openai, pyttsx3, recorder, transcribe, translate`. [PyPI JSON](https://pypi.org/pypi/manim-voiceover/json)
- The README lists Gemini as "Recommended for AI voices". It syncs animations to speech, with Whisper-based word timing, and can record your own voice with a microphone. [repo](https://github.com/ManimCommunity/manim-voiceover)
- The services page compares quality, offline use and cost. Coqui is listed as local, free and needing PyTorch. [services](https://voiceover.manim.community/en/stable/services.html) The 0.4.0 extras list has no `coqui`, so treat Coqui integration as possibly dropped (inference from PyPI metadata).

**Subtitles without TTS:** `Scene.add_subcaption(content, duration, offset)` or `play(..., subcaption=...)` writes timed entries to the scene's subcaption file. [Scene API](https://docs.manim.community/en/stable/reference/manim.scene.scene.Scene.html) From memory, not verified on that page: the file is `.srt`.

**Turkish-capable TTS**

| Engine | Where | Turkish | Cost | Source |
|---|---|---|---|---|
| Azure Neural | cloud | `tr-TR-EmelNeural`, `tr-TR-AhmetNeural`, plus HD `Aydın`/`Elif` (MAI-Voice-2) | Free F0 tier: 0.5M chars/month (Neural) | [voices](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/language-support?tabs=tts), [pricing](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/) |
| Gemini 3.8 Flash(-Lite) TTS | cloud | yes, auto language detection | $9/1M audio tokens (25 tok/s), about $0.00225 per 10 s through 2026, doubling Jan 2027. Free tier available | [TTS docs](https://ai.google.dev/gemini-api/docs/speech-generation), [pricing](https://ai.google.dev/gemini-api/docs/pricing) |
| ElevenLabs | cloud | Multilingual v2, v3, Flash v2.5 | $0.08/1K chars (v2), $0.04 (Flash). Starter plan $6/month | [models](https://elevenlabs.io/docs/overview/models), [pricing](https://elevenlabs.io/pricing/api) |
| OpenAI TTS | cloud | yes, but "voices optimized for English". `gpt-4o-mini-tts`/`tts-1` shut down Jan 6 2027 | — | [docs](https://developers.openai.com/api/docs/guides/text-to-speech) |
| XTTS-v2 (Coqui) | local GPU | yes (17 languages) | free; Coqui Public Model License | [HF](https://huggingface.co/coqui/XTTS-v2). Maintained fork: [idiap/coqui-ai-TTS](https://github.com/idiap/coqui-ai-TTS) |
| Chatterbox Multilingual | local GPU/CPU | yes (23 languages) | free, MIT | [repo](https://github.com/resemble-ai/chatterbox) |
| Piper | local CPU | `tr_TR/dfki` only. `fahrettin` and `fettah` were removed | free. Original repo archived Oct 2025, development moved to OHF-Voice/piper1-gpl | [voices](https://huggingface.co/rhasspy/piper-voices/tree/main/tr/tr_TR), [repo](https://github.com/rhasspy/piper) |

**Cost estimate** (my arithmetic): a 5-minute Turkish narration is about 4–5K characters.

- ElevenLabs v2: about $0.40.
- Gemini Flash TTS: 300 s × 25 tokens/s = 7,500 tokens, about $0.07.
- Azure: well inside the free 0.5M characters per month.

Cost is not a decision factor.

**Note for a single learner:** a TTS voice adds sync work and a quality risk (English terms pronounced inside Turkish sentences). A subtitle-only or silent-plus-written-commentary video is cheaper. This is a decision for the human; see §6.

## 4. Embedding in a study unit

- **Local markdown:** a relative link to the mp4 or an HTML `<video controls src="media/kv-cache.mp4">`, depending on the viewer. Obsidian supports `.mp4/.webm/.mov/.mkv/.ogv` and embeds by drag-and-drop, which produces `![[file.mp4]]`. [Obsidian](https://obsidian.md/help/file-formats)
- **GitHub:**
  - Uploaded videos are capped at 10 MB on free plans and 100 MB on paid plans. Formats are `.mp4/.mov/.webm`, and H.264 is recommended. [GitHub docs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files)
  - iframes are stripped, and relative `<video>` to a repo file reportedly does not work. [bobbyhadz](https://bobbyhadz.com/blog/embed-video-into-github-readme-markdown)
- **Jupyter:**
  - `%%manim -qm Scene` renders inline. `config.media_embed=True` embeds the video, which makes notebooks large but survives moving the file. [ManimMagic](https://docs.manim.community/en/stable/reference/manim.utils.ipython_magic.ManimMagic.html)
  - This means the animation's source can sit next to the explanation as an interactive "edit and re-render" exercise.
- **Practical:** keep `units/<unit>/media/<concept>.mp4` with the source `<concept>.py` next to it. Link both from the unit, and keep a poster PNG (`-s`) as a fallback thumbnail.

## 5. Production time per 2–5 minute concept video

Evidence:

- TheoremExplainAgent reports 1120–2380 s of fully autonomous agent time per video (7 scenes), excluding any human review. [HTML v2](https://arxiv.org/html/2502.19400v2)
- None of the other papers report wall-clock time in their abstracts or READMEs. [Code2Video](https://github.com/showlab/Code2Video), [PSA](https://arxiv.org/abs/2601.13453)

My estimate (not sourced; validate in a prototype):

| Step | First 2–3 videos | After a style/template library exists |
|---|---|---|
| Script and storyboard (Turkish text, scene list, correctness check against paper/docs) | 30–60 min | 20–30 min |
| Agent code→render(-ql)→frame-inspect loop, 4–8 scenes | 45–90 min | 20–40 min |
| Human review and pedagogical fixes | 30–60 min | 15–30 min |
| Final `-qh` render plus optional TTS/subtitles | 15–30 min (mostly unattended) | same |
| **Total** | **≈2–4 h** | **≈1–2 h** |

At 1–2 videos per week, that is about 10–25 videos over 3 months. This should feed the scope decision: keep custom videos for the handful of concepts with no good external visual.

## 6. Recommended pipeline (for the human to decide)

1. **Pin the environment.** Use one project venv via uv with `manim==0.22.*`, on Omarchy, renderer Cairo. Before any agent work:
   - Run `manim checkhealth`.
   - Install TeX Live only if formulas are needed.
   - Use the Docker image as a fallback.
2. **Write a project skill or CLAUDE.md section** that:
   - States "Manim CE only" and includes a forbidden-ManimGL list (`ShowCreation`, `CONFIG`, `from manimlib`, ...), following ManiBench.
   - Contains 3–5 few-shot scenes in the house style.
   - Keeps a `pitfalls.md` the agent appends to after each fixed bug, following ManimAgent.
   - Optionally starts from DominikPeters/manim-skill's frame and contact-sheet scripts.
3. **Script first.** For each concept, the learner and agent write a short Turkish script and storyboard listing scenes, on-screen text and the one key insight. Verify the technical claims against the primary source before any code.
4. **Inner loop, per scene.** Agent writes code → render `-ql` → on crash, read the traceback and fix (cap about 5 tries, as in TheoremExplainAgent) → export frames or a contact sheet → Claude inspects for overlap, cropping, readability and correctness → fix.
5. **Learner review** of the full `-ql` video for pedagogy and correctness. This is the only defense against "runs but wrong".
6. **Final render** at `-qm` or `-qh` (720p30 is likely enough for study and keeps files under 10 MB). Then add `add_subcaption` subtitles. Optionally add TTS via manim-voiceover:
   - Azure free tier (Emel/Ahmet), or
   - Gemini Flash TTS, or
   - local Chatterbox/XTTS on the 3090 rig if offline is preferred.
7. **Embed** `media/<concept>.mp4` and `<concept>.py` in the unit markdown. Optionally provide a notebook with `%%manim` for hands-on tweaking.

**Suggested first step:** a time-boxed prototype of one video (e.g. KV cache) to measure real render time and loop count before committing to a video count.

## 7. Key risks

- **Semantic or pedagogical errors that render fine.** A misleading animation of a technical concept is worse than none. Human review is mandatory. [ManiBench](https://arxiv.org/html/2603.13251v1) notes alignment metrics are heuristic.
- **API drift and GL/CE confusion.** Mitigate by pinning the version, using a forbidden list, and adding few-shot examples. [ManiBench](https://arxiv.org/html/2603.13251v1)
- **Layout problems persist even in successful runs.** [TheoremExplainAgent](https://arxiv.org/abs/2502.19400), [PSA](https://arxiv.org/abs/2601.13453) Frame inspection is required, and VLM critics themselves misread frames.
- **Time sink.** At an estimated 1–4 h per video, the effort competes with actual study time in a 3-month program. Make videos only where no good external visual exists.
- **TTS quality for mixed Turkish and English terms.** Untested. OpenAI's voices are English-optimized. [OpenAI](https://developers.openai.com/api/docs/guides/text-to-speech) Listen to samples before committing; subtitles avoid the problem.
- **Dependency and service churn.**
  - OpenAI TTS models end Jan 2027. [OpenAI](https://developers.openai.com/api/docs/guides/text-to-speech)
  - Gemini TTS price doubles Jan 2027. [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing)
  - Piper was archived and moved. [Piper](https://github.com/rhasspy/piper)
  - Coqui upstream is unmaintained. [idiap fork](https://github.com/idiap/coqui-ai-TTS)
- **Install friction on a rolling distro.** No Arch package and source-built ManimPango and pycairo. [CE install](https://docs.manim.community/en/stable/installation/uv.html), [archlinux](https://archlinux.org/packages/?q=manim) Docker is the escape hatch.

## Open items / not verified

- Real render times on this hardware. Measure in the prototype.
- Whether subcaptions are emitted as `.srt`. The Scene API page only says "subcaption file".
- Turkish quality of each TTS engine with embedded English ML terms.
