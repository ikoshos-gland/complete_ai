# 01 — Zor AI/ML/LLM mülakat sorusu kaynakları envanteri

Ticket: [../issues/01-soru-kaynaklari-envanteri.md](../issues/01-soru-kaynaklari-envanteri.md)
Tarih: 2026-11-01. GitHub yıldız / son push / lisans değerleri GitHub REST API'den (`api.github.com/repos/<owner>/<repo>`) bu tarihte çekildi; README içerikleri `raw.githubusercontent.com` üzerinden okundu.

## Türkçe özet

- **Frontier-lab RE seviyesinde, hazır ve "zor" bir soru bankası yok.** Popüler GitHub soru repoları çoğunlukla FAANG MLE / "AI Engineer" (RAG, prompt, agent) seviyesinde. Zor seviye sorular üç tür kaynaktan **türetilmeli**: (1) implement-from-scratch / bulmaca setleri (TorchLeet, Deep-ML, srush puzzles, CS336 ödevleri), (2) zor kavramsal kitaplar (Chip Huyen MLI book, Kashani DL Interviews, UDL alıştırmaları, *How to Scale Your Model*), (3) aday raporları (Glassdoor, 1point3acres, PracHub, Blind) — bunlar format ve konu sinyali verir ama düşük güvenilirlikte ve yeniden kullanıma kapalı.
- **Lisans:** Çoğu popüler soru reposunun LİSANSI YOK (varsayılan "tüm hakları saklı"). Kişisel çalışma bankasında *kendi kelimelerinle yeniden yazmak / esinlenmek* pratikte sorun değil, ama birebir kopyalayıp paylaşmak değil. Açık lisanslılar: TorchLeet (MIT), srush puzzles (MIT), alirezadir/AIMLInterviews (MIT), KalyanKS (Apache-2.0), stas00/ml-engineering (CC-BY-SA-4.0), CS336 ödevleri (MIT). Deep-ML "Educational Use Only"; UDL CC BY-NC-ND; dmol.pub CC BY-NC.
- **En zayıf kategoriler:** bio-ML (neredeyse hiç soru kaynağı yok — tamamen türetmek gerekecek), dağıtık eğitim *teorisi* soruları (kaynak var ama soru formatında değil), "bu training loop'u debug et" soruları (format çok raporlanıyor, açık set yok), ve LLM ön-eğitim/ölçekleme yasaları hakkında zor kavramsal sorular.
- **Kısa liste (12 kaynak)** aşağıda §(b)'de. Kaynakların kullandığı doğal kategori eksenleri §(c)'de (karar değil, gözlem).

---

## 1. Generalist ML interview question repos / books

| # | Source | What it is | ~Questions | Difficulty | Recency | License | Categories | Reliability |
|---|---|---|---|---|---|---|---|---|
| 1 | **Chip Huyen — *Machine Learning Interviews Book*** ([repo](https://github.com/chiphuyen/ml-interviews-book), [web](https://huyenchip.com/ml-interviews-book/)) | Part I: process/roles; Part II: knowledge questions, each tagged with difficulty | "over 200" ([README](https://github.com/chiphuyen/ml-interviews-book)) | Mixed, explicitly difficulty-tagged; the hardest are good for RE | ©2021; last push 2025-03-21; 4.8k★ (API) | **No license file**; "Copyright ©2021 Chip Huyen" ([repo](https://github.com/chiphuyen/ml-interviews-book)) | Ch5 Math (linear algebra, calculus/convex opt, probability, stats); Ch6 CS (algorithms, complexity/numerical, data structures); Ch7 ML workflows (sampling, objectives/metrics); Ch8 algorithms (classical ML, DL archs, training NNs) ([TOC](https://huyenchip.com/ml-interviews-book/)) | High (author was interviewer at NVIDIA/Snorkel, [README](https://github.com/chiphuyen/ml-interviews-book)). Answers are community-sourced via Discord/`answers` folder — not authoritative. Pre-LLM era. |
| 2 | **Kashani & Ivry — *Deep Learning Interviews*** ([repo](https://github.com/BoltzmannEntropy/interviews.ai), [arXiv 2201.00650](https://arxiv.org/abs/2201.00650)) | Book of fully solved problems, 2nd ed. | "Hundreds of fully solved" ([arXiv](https://arxiv.org/abs/2201.00650)) | Hard/quantitative (derivation-heavy) | arXiv v2 2022-01-04; repo push 2025-08-22; 4.9k★ | **Conflict:** repo README says "private study" only, commercial use prohibited ([README](https://github.com/BoltzmannEntropy/interviews.ai)); arXiv listing shows CC BY 4.0 ([arXiv](https://arxiv.org/abs/2201.00650)). Personal study bank is fine either way. | Information theory, Bayesian stats, algorithmic differentiation, logistic regression, perceptrons, CNNs ([README](https://github.com/BoltzmannEntropy/interviews.ai)) | Medium-high; solutions included. No transformers/LLMs (vol. 1). Good for math-foundations hard questions. |
| 3 | **alirezadir/AIMLInterviews** (formerly *Machine-Learning-Interviews*) ([repo](https://github.com/alirezadir/AIMLInterviews)) | Study guide: DSA coding, ML coding, ML breadth (classic, GenAI, agentic), system design, behavioral | Guide + topic lists, not a numbered Q bank | Medium (FAANG MLE/Applied Scientist) | Push 2026-10-08; 9.9k★; "updated for 2026 with expanded LLM, multimodal AI, post-training" ([README](https://github.com/alirezadir/AIMLInterviews)) | **MIT** | Its 5 chapters are themselves a category axis | Medium-high; author explicitly says it targets MLE/Applied Science, not research roles ([README](https://github.com/alirezadir/AIMLInterviews)). Also sells coaching. |
| 4 | **andrewekhalel/MLQuestions** ([repo](https://github.com/andrewekhalel/MLQuestions)) | Q&A list | 69 ([README](https://github.com/andrewekhalel/MLQuestions)) | Easy–medium | Push 2026-10-15; 5.0k★ | No license | ML fundamentals, DL, CV, NLP, dim. reduction, stats, coding | Medium; too easy for target level. |
| 5 | **khangich/machine-learning-interview** ([repo](https://github.com/khangich/machine-learning-interview)) | Study plan / link collection | — | Medium | Push 2023-08-31 (stale); 12.9k★ | No license | Links + ML system design upsell | Low-medium; mostly links and promotion of paid books ([README](https://github.com/khangich/machine-learning-interview)). |
| 6 | **b7leung/MLE-Flashcards** ([repo](https://github.com/b7leung/MLE-Flashcards)) | Flashcards | "250+" ([README](https://github.com/b7leung/MLE-Flashcards)) | Medium–hard, assumes a good foundation | Push 2026-04-30; 2.5k★ | GPL-3.0 | CS, classical ML, DL, 2D/3D CV, NLP, RL, generative models | Medium; author warns of possible errors. |
| 7 | **youssefHosni/Data-Science-Interview-Questions-Answers** ([repo](https://github.com/youssefHosni/Data-Science-Interview-Questions-Answers)) | DS Q&A | Many | Easy–medium | Push 2024-09-29; 5.9k★ | No license | DS/stats/ML | Low for target level. |
| 8 | **Chinese LLM interview notes** — wdndev/llm_interview_note ([repo](https://github.com/wdndev/llm_interview_note)), km1994/LLMs_interview_notes ([repo](https://github.com/km1994/LLMs_interview_notes)), amusi/Deep-Learning-Interview-Book ([repo](https://github.com/amusi/Deep-Learning-Interview-Book)) | Large Chinese-language notes incl. "real interview questions" (真实面试题) sections | Hundreds | Medium–hard; LLM internals, training, inference | wdndev push 2026-06-14, 15.3k★; km1994 2026-10-11, 2.6k★ (Apache-2.0); amusi 2024-04 | wdndev none; km1994 Apache-2.0 | LLM basics, architectures, training, distributed, inference, RLHF | Medium; answers self-written ("相关答案为自己撰写", [README](https://github.com/wdndev/llm_interview_note)). Notable: Chinese LLM-algorithm-engineer interview culture ("八股") asks deeper LLM-internals questions than English AI-Engineer repos. Language barrier. |

## 2. LLM-specific question repos

| # | Source | ~Questions | Difficulty | Recency | License | Categories | Reliability |
|---|---|---|---|---|---|---|---|
| 9 | **llmgenai/LLMInterviewQuestions** ([repo](https://github.com/llmgenai/LLMInterviewQuestions)) | "100+", 15 categories, questions only (answers behind paid course) ([README](https://github.com/llmgenai/LLMInterviewQuestions)) | Easy–medium; applied/RAG heavy | Push 2025-02-12; 2.0k★ | No license | Prompting, RAG, chunking, embeddings, vector DB internals, LM internals, SFT, RLHF/DPO, eval, hallucination, deployment, agents, prompt hacking, case studies | Low-medium; "top companies" claim unverifiable; commercial funnel. |
| 10 | **KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub** ([repo](https://github.com/KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub)) | "100+" with answers ([README](https://github.com/KalyanKS-NLP/LLM-Interview-Questions-and-Answers-Hub)) | Medium | Push 2026-02-09; 1.1k★ | **Apache-2.0** | LLM fundamentals, training, inference | Medium; reusable license. |
| 11 | **Devinterview-io/llms-interview-questions** ([repo](https://github.com/Devinterview-io/llms-interview-questions)) | 63 ([README](https://github.com/Devinterview-io/llms-interview-questions)) | Easy–medium | Push 2026-02-17; 1.1k★ | No license | LLM concepts | Low; content-farm style, answers on paid site. |
| 12 | **amitshekhariitbhu/ai-engineering-interview-questions** ([repo](https://github.com/amitshekhariitbhu/ai-engineering-interview-questions)) | Large Q&A cheat sheet | Easy–medium | Push 2026-11-01; 3.6k★ | Apache-2.0 | Targets "AI Engineer, LLMOps, FDE" roles: RAG, agents, fine-tuning, vector DBs, AI system design, LLMOps, eval, safety ([README](https://github.com/amitshekhariitbhu/ai-engineering-interview-questions)) | Low-medium for RE; wrong role. |

**Observation:** every English "LLM interview questions" repo found targets *AI-Engineer / applied LLM* roles (RAG, prompting, agents), not research-engineer depth (e.g. derive DPO from the RLHF objective, compute FLOPs/memory of a training step, explain loss spikes). GitHub search for these terms confirms the landscape ([search](https://api.github.com/search/repositories?q=llm+interview+questions&sort=stars)).

## 3. Implement-from-scratch / ML-coding / puzzle sets (best source of *hard* material)

| # | Source | ~Items | Difficulty | Recency | License | Categories | Reliability |
|---|---|---|---|---|---|---|---|
| 13 | **Exorust/TorchLeet** ([repo](https://github.com/Exorust/TorchLeet)) | 68 PyTorch problems (Basics 24, LLM path 23, Advanced 48, overlapping); each has Q + `_SOLN` notebook ([README](https://github.com/Exorust/TorchLeet)) | Easy→"Expert"; includes DPO, PPO-RLHF, GRPO, KV cache, speculative decoding, MoE, Mamba, FlashAttention-2 in Triton, FSDP, ring attention ([README](https://github.com/Exorust/TorchLeet)) | Push 2026-10-21; 2.6k★ | **MIT** | Basics / LLM path / Advanced (modern archs, alignment, decoding, inference, GPU systems) | Medium-high for content; **company tags ("Anthropic, OpenAI…") are the author's claim from "first person reports", unverifiable** ([README](https://github.com/Exorust/TorchLeet)). Solutions partly GPT-assisted per author. Closest thing to an RE-level ML-coding bank. |
| 14 | **Deep-ML** ([site](https://www.deep-ml.com/problems), [open bank repo](https://github.com/Open-Deep-ML/DML-OpenProblem)) | Open repo: ~164 problem folders (counted `questions/*/meta.json`, shallow clone 2026-11-01); site claims "1,200+" vs "100+" in different places ([site](https://www.deep-ml.com/problems)) — inconsistent | Easy/Medium/Hard; LeetCode-like with tests; NumPy, PyTorch, tinygrad variants ([repo README](https://github.com/Open-Deep-ML/DML-OpenProblem)) | Repo last commit 2025-11-10; 711★ | **"Educational Use Only License"** (repo LICENSE); site has paid Premium ([site](https://www.deep-ml.com/problems)) | Linear algebra, ML, DL, NLP, CV ([site](https://www.deep-ml.com/problems)); includes e.g. GRPO objective (`101_grpo_objective`, [repo](https://github.com/Open-Deep-ML/DML-OpenProblem)) | Medium-high; auto-graded tests are a plus. |
| 15 | **Sasha Rush puzzles** — Tensor ([repo](https://github.com/srush/Tensor-Puzzles), 4.4k★), GPU/CUDA ([repo](https://github.com/srush/GPU-Puzzles), 12.6k★), Autodiff ([repo](https://github.com/srush/Autodiff-Puzzles)), **LLM-Training-Puzzles** ([repo](https://github.com/srush/LLM-Training-Puzzles), "8 challenging puzzles about training LLMs on many GPUs") | ~20 each; 8 for LLM training | Hard | 2024 (pushes Jan–Oct 2024) | **MIT** | Tensor broadcasting, CUDA kernels, autodiff, distributed training (memory/pipelining) | High (Cornell/HF researcher). LLM-Training-Puzzles is the only *exercise-format* distributed-training resource found. |
| 16 | **Stanford CS336 — Language Modeling from Scratch** ([course, Spring 2026](https://cs336.stanford.edu/); [assignment1 repo](https://github.com/stanford-cs336/assignment1-basics), MIT, push 2026-04-07) | 5 assignments | Very hard (research-grade) | Spring 2026 offering | MIT (assignment repos) | A1 tokenizer+transformer+optimizer; A2 profiling, FlashAttention2 in Triton, distributed training; A3 scaling-law fitting; A4 Common Crawl filtering/dedup; A5 SFT + RL for reasoning, optional DPO ([course](https://cs336.stanford.edu/)) | Very high. Not a Q bank, but each assignment section maps to hard interview questions ("implement X", "why does Y"). |
| 17 | **eriklindernoren/ML-From-Scratch** ([repo](https://github.com/eriklindernoren/ML-From-Scratch)) | Dozens of NumPy impls | Medium | Push 2023-10 | MIT | Classical ML + basic DL from scratch | Medium; good for classical-ML coding. |
| 18 | **rasbt/LLMs-from-scratch** ([repo](https://github.com/rasbt/LLMs-from-scratch), 107.6k★, push 2026-10-30) / **karpathy/nanoGPT** ([repo](https://github.com/karpathy/nanoGPT), MIT) / **nn-zero-to-hero** ([repo](https://github.com/karpathy/nn-zero-to-hero), MIT) / **labmlai annotated paper implementations** ([repo](https://github.com/labmlai/annotated_deep_learning_paper_implementations), MIT, 67.6k★) | Reference implementations | — | Current | MIT (rasbt: NOASSERTION) | Transformer/LLM internals | High; *reference answers* for implement-from-scratch questions rather than questions. |

## 4. ML system design & distributed training (theory)

| # | Source | What | Recency | License | Reliability |
|---|---|---|---|---|---|
| 19 | **Chip Huyen — ML systems design booklet** ([repo](https://github.com/chiphuyen/machine-learning-systems-design), 10.7k★) | "30 open-ended questions" ([MLI README](https://github.com/chiphuyen/ml-interviews-book)); classic product-ML design | Push 2023-04; content ~2019 | No license | High but product-ML (recsys/ranking), not LLM training. |
| 20 | **Aminian & Xu — *ML System Design Interview*** / **Aminian & Sheng — *Generative AI System Design Interview*** (ByteByteGo, 2024) ([publisher post](https://blog.bytebytego.com/p/our-new-book-generative-ai-system), [library record](https://library.naist.jp/opac/en/volume/259442)) | GenAI book: 10 design questions w/ solutions — Smart Compose, Google Translate, ChatGPT-style assistant, image captioning, RAG, face generation, high-res image synthesis, text-to-image, headshots, text-to-video ([publisher post](https://blog.bytebytego.com/p/our-new-book-generative-ai-system), [Substack note](https://substack.com/@bytebytego/note/c-77746705)) | 2024 | Commercial, copyrighted | Medium-high for MLE/applied design; light on training-infra depth. |
| 21 | **Austin et al. (Google DeepMind) — *How To Scale Your Model*** ([book](https://jax-ml.github.io/scaling-book/), [repo](https://github.com/jax-ml/scaling-book) MIT code, push 2026-10-19) | 12 chapters on TPU/GPU, communication, parallelism for training & inference; includes worked problems ([book](https://jax-ml.github.io/scaling-book/)) | Published 2025-02-04 | Repo MIT; page itself states no license, copyright footer ([book](https://jax-ml.github.io/scaling-book/)) | Very high (frontier-lab authors). Its worked problems are directly RE-interview-shaped (FLOPs, memory, comms-cost estimates). |
| 22 | **stas00/ml-engineering** ([repo](https://github.com/stas00/ml-engineering), 19.6k★, push 2026-10-27) | "Machine Learning Engineering Open Book": compute, storage, network, training, debugging, inference | Current | **CC-BY-SA-4.0** | High (practitioner, BLOOM training). Source for infra/debug question generation. |
| 23 | **HF *Ultra-Scale Playbook*** ([Space](https://huggingface.co/spaces/nanotron/ultrascale-playbook); [InfoQ coverage](https://www.infoq.com/news/2025/03/huggingface-ultra-scale-playbook)) | DP/PP/TP, activation recomputation, gradient accumulation; based on 4000+ scaling experiments up to 512 GPUs (per InfoQ) | 2025-02/03 | Not verified | High; content not fetched directly (Space didn't render) — **partially unverified**. |
| 24 | **donnemartin/system-design-primer** ([repo](https://github.com/donnemartin/system-design-primer), 376k★) / **ashishps1/awesome-system-design-resources** ([repo](https://github.com/ashishps1/awesome-system-design-resources), GPL-3.0) | Generic distributed-systems design | Current | primer NOASSERTION | High but generic SWE; peripheral. |

## 5. Math / DL textbooks with exercises (question generators)

| # | Source | Notes |
|---|---|---|
| 25 | **Prince — *Understanding Deep Learning*** (MIT Press 2023) ([repo](https://github.com/udlbook/udlbook), 10.1k★) | Practice problems + Python notebooks; repo contains `UDL_Answer_Booklet_Students.pdf`; repo license **CC BY-NC-ND 4.0** ([repo](https://github.com/udlbook/udlbook)). Excellent hard conceptual DL questions; no-derivatives clause means paraphrase for personal use only. |
| 26 | **afshinea/stanford-cs-229-machine-learning** cheatsheets ([repo](https://github.com/afshinea/stanford-cs-229-machine-learning), MIT, 2020) | Classical ML refresher; not questions. |

(Other standard texts — Bishop, Murphy PML, Goodfellow — are well known but were not verified in this pass.)

## 6. LeetCode-style algorithms

| # | Source | Notes |
|---|---|---|
| 27 | **Grind 75 / Tech Interview Handbook** ([site](https://www.techinterviewhandbook.org/grind75/), [repo](https://github.com/yangshun/tech-interview-handbook) MIT, 143k★) | "A better Blind 75 you can customize, by the author of Blind 75" ([site](https://www.techinterviewhandbook.org/grind75/)). Counts not shown on page. |
| 28 | **NeetCode** ([site](https://neetcode.io/practice)) | NeetCode 150/250 lists; page content didn't render — **counts/pricing unverified**. |
| 29 | **jwasham/coding-interview-university** ([repo](https://github.com/jwasham/coding-interview-university), CC-BY-SA-4.0, 364k★) | CS study plan, not a Q list. |

Note: candidate reports for frontier labs describe practical, multi-step coding (Colab, CodeSignal, "LC Easy … multi-step problem") more than hard LeetCode ([Blind](https://www.teamblind.com/post/anthropic-research-engineer-interview-tcdmrea3), [Exponent](https://www.tryexponent.com/blog/anthropic-interview-process)) — unverified but consistent across sources.

## 7. Published interview experiences — frontier labs

Primary/first-party:
- **Anthropic — "How to collaborate with Claude during our hiring process"** ([page](https://www.anthropic.com/candidate-ai-guidance)): official AI-use policy for candidates; reportedly no AI in live interviews unless stated. Not a question source.
- **OpenAI** official interview guide: referenced by third parties but **not located** on openai.com in this pass ([Exponent guide mentions it](https://www.tryexponent.com/guides/openai-research-engineer-interview-guide)) — unverified.
- **Aleksa Gordić, "How I got a job at DeepMind as a Research Engineer"** ([Medium](https://gordicaleksa.medium.com/how-i-got-a-job-at-deepmind-as-a-research-engineer-without-a-machine-learning-degree-1a45f2a781de)) — first-person account; page returned 403, **content not verified here**.

Secondary aggregators (format signal, low reliability, often paywalled, ToS typically forbid reuse):
- **Glassdoor** — e.g. Anthropic RE ([page](https://www.glassdoor.com/Interview/Anthropic-Research-Engineer-Interview-Questions-EI_IE8109027.0,9_KO10,27.htm)), Isomorphic Labs (a review lists "take home assignment, coding, HM interview, ML debugging, behavioral" — [review](https://www.glassdoor.ca/Interview/Isomorphic-Labs-Interview-E7140434-RVW97334846.htm)). Sparse; NDA-limited.
- **1point3acres** — OpenAI RE onsite threads ([1](https://www.1point3acres.com/interview/thread/1168926), [2](https://www.1point3acres.com/interview/thread/1177439)), Anthropic RE ([1](https://www.1point3acres.com/interview/thread/1137418), [phone screen](https://www.1point3acres.com/interview/thread/1068565)), Scale AI MLRE ([thread](https://www.1point3acres.com/interview/thread/1039138)). Most detailed raw reports; Chinese; partly login-gated.
- **PracHub** — e.g. OpenAI MLE "surprise debugging round" ([page](https://prachub.com/interview-experiences/openai-machine-learning-engineer-interview-experience-a-malloc-phone-screen-and-a-surprise-debugging-round)).
- **Exponent** OpenAI RE guide — describes an ML debugging round with a transformer implementation, pre-annotated buggy sections, KV-cache extension ([guide](https://www.tryexponent.com/guides/openai-research-engineer-interview-guide)).
- **Thinking Machines** write-up: technical screen on attention, data loaders, debugging a broken training loop ([techinterview.org](https://www.techinterview.org/post/3233476796/thinking-machines-lab-interview/?format=md)).
- **Sundeep Teki** RE/RS guides for OpenAI/Anthropic/DeepMind ([RE](https://www.sundeepteki.org/advice/the-ultimate-ai-research-engineer-interview-guide-cracking-openai-anthropic-google-deepmind-top-ai-labs)) — coach-written synthesis.
- **Interview Query / Blind** company pages ([OpenAI](https://www.interviewquery.com/interview-guides/openai), [Blind ML debugging](https://www.teamblind.com/post/ml-debugging-interviews-lbtbpqzi)).
- **alexeygrigorev/ai-engineering-field-guide** ([repo](https://github.com/alexeygrigorev/ai-engineering-field-guide), 6.0k★, push 2026-09-23): questions consolidated from 100+ sources, with an inventory of **58 Reddit + 46 HN interview threads** and traceability to sources ([data README](https://github.com/alexeygrigorev/ai-engineering-field-guide/tree/main/interview/data)). Best curated meta-index of Reddit/HN experiences — but focused on *AI Engineer* roles. No license.

**Reliability summary:** consistent cross-source signal that frontier RE loops contain (a) practical coding, (b) ML coding/implementation (attention, sampling, KV cache), (c) **ML/transformer debugging**, (d) ML depth/research discussion, (e) values/safety. Specific questions are rarely disclosed (NDAs).

## 8. Bio-ML specific

- **No dedicated bio-ML interview question bank found.** GitHub search for "bioinformatics interview questions" returns essentially nothing relevant ([search](https://api.github.com/search/repositories?q=bioinformatics+interview+questions&sort=stars)); targeted web searches for Genentech/Prescient/Recursion/EvolutionaryScale interview questions returned only generic third-party guides and job postings ([e.g. Calico guide](https://www.interviewquery.com/interview-guides/calico-life-sciences-machine-learning-engineer), [BigHat guide](https://dataford.io/interview-guides/bighat-biosciences)).
- Isomorphic Labs: Glassdoor review mentions an **ML debugging** round and take-home ([review](https://www.glassdoor.ca/Interview/Isomorphic-Labs-Interview-E7140434-RVW97334846.htm)); job postings emphasise large-scale experiments across thousands of accelerators ([posting](https://job-boards.greenhouse.io/isomorphiclabs/jobs/5561630004)) — i.e. RE-style infra questions apply.
- Question *generators* for bio-ML:
  - **Andrew White — *Deep Learning for Molecules and Materials*** ([dmol.pub](https://dmol.pub/)): GNNs, equivariance, attention, VAEs, flows; **CC BY-NC 3.0**.
  - **MIT 6.874 / 6.8710 *Deep Learning in the Life Sciences*** (Gifford/Kellis; now Berger) ([listing](https://toc.csail.mit.edu/node/1812)) — problem sets not located; **unverified**.
  - Primary model repos as "explain/implement" material: AlphaFold 2 ([repo](https://github.com/google-deepmind/alphafold), Apache-2.0), OpenFold ([repo](https://github.com/aqlaboratory/openfold), Apache-2.0), ESM ([facebookresearch/esm](https://github.com/facebookresearch/esm), MIT; ESM3 repo — note `evolutionaryscale/esm` now redirects to `Biohub/esm` per GitHub API on 2026-11-01, [repo](https://github.com/Biohub/esm)).
  - Job postings (Profluent, Manifold, etc.) as topic signals ([Profluent](https://job-boards.greenhouse.io/profluent/jobs/4061679008)).

---

## (a) Gap analysis

| Scope category | Coverage by existing sources | Comment |
|---|---|---|
| Classical ML | **Good** (Huyen, MLQuestions, flashcards, ML-From-Scratch, Deep-ML) | Plenty, though mostly medium difficulty. |
| Deep learning fundamentals | **Good** (Huyen Ch8, Kashani, UDL, flashcards) | UDL + Kashani give hard derivations. |
| Math foundations | **Medium** (Huyen Ch5, Kashani) | Hard probability/info-theory exists in Kashani; linear algebra/optimisation thin at RE level. |
| Transformers/LLMs — conceptual depth (pretraining, scaling laws, RLHF/DPO theory, inference optimisation) | **Weak** | English LLM repos are AI-Engineer/RAG level. Depth must be derived from CS336, *How to Scale Your Model*, papers; Chinese notes help. |
| ML coding / implement-from-scratch | **Good** (TorchLeet, Deep-ML, srush, CS336) | Best-served hard category. |
| "Debug this training loop / transformer" | **Very weak** | Format is widely reported for OpenAI, Thinking Machines, Isomorphic; **no open problem set found**. Must be authored (inject bugs into nanoGPT/CS336 code). |
| ML system design — product ML | Medium (Huyen booklet, ByteByteGo) | Applied/MLE flavour. |
| Distributed training & infra theory | **Weak as questions, strong as material** (scaling-book, Ultra-Scale Playbook, stas00, LLM-Training-Puzzles) | Need to convert to back-of-envelope Qs. |
| LeetCode algorithms | **Saturated** (Grind 75, NeetCode) | Just pick a list. |
| Bio-ML | **Essentially absent** | Must be generated from dmol.pub, model papers (AF2/3, ESM, Evo), and learner's own research. |
| Research discussion / paper deep-dive | Absent as sources | Format reported (research rounds); questions are inherently personalised. |

## (b) Recommended core shortlist (12)

1. **Chip Huyen, ML Interviews Book** — difficulty-tagged breadth backbone (math, CS, ML workflow, algorithms).
2. **Kashani & Ivry, Deep Learning Interviews** — hard solved math/DL problems.
3. **Prince, Understanding Deep Learning** (problems + answer booklet) — hard conceptual DL.
4. **TorchLeet** — RE-level ML coding incl. alignment, inference, GPU systems (MIT).
5. **Deep-ML** — auto-graded implementation problems (educational-use licence).
6. **srush puzzles** (Tensor, Autodiff, GPU, LLM-Training) — hard, MIT.
7. **Stanford CS336 assignments** (2026) — LLM pretraining, systems, scaling, data, alignment; source for hard "implement/explain" questions.
8. ***How To Scale Your Model*** (DeepMind) — distributed training/inference theory with worked problems.
9. **stas00/ml-engineering** (+ Ultra-Scale Playbook) — infra, debugging, training instabilities (CC-BY-SA).
10. **alirezadir/AIMLInterviews** — round structure & system-design framing (MIT), 2026-updated.
11. **Grind 75 / NeetCode 150** — algorithms track.
12. **Interview-experience layer**: 1point3acres + Glassdoor + Exponent/PracHub + alexeygrigorev field-guide threads — format/topic signal only; never as answer source.
(+ bio-ML: **dmol.pub** + primary model papers/repos, as a generator rather than a bank.)

## (c) Observations on natural category axes (input to taxonomy decision — not a decision)

1. **Interview round / module** is the most common top-level axis among prep guides: DSA coding · ML coding · ML breadth · (ML) system design · behavioral ([AIMLInterviews](https://github.com/alirezadir/AIMLInterviews)); field guide uses theory · coding · project deep dive · system design · behavioral · take-home ([field guide](https://github.com/alexeygrigorev/ai-engineering-field-guide)). Frontier-lab reports add **ML debugging** and **research discussion** as distinct rounds.
2. **Knowledge domain** axis (textbook-like): math → CS → ML workflow → ML algorithms (classical/DL) ([Huyen TOC](https://huyenchip.com/ml-interviews-book/)); Kashani: information theory, Bayesian, autodiff, …
3. **LLM lifecycle** axis appears in LLM repos and courses: tokenization → architecture → pretraining/data → scaling → SFT → preference alignment (RLHF/DPO/GRPO) → evaluation → inference/serving ([llmgenai](https://github.com/llmgenai/LLMInterviewQuestions), [CS336](https://cs336.stanford.edu/), [TorchLeet tracks](https://github.com/Exorust/TorchLeet)).
4. **Question format / cognitive task** is orthogonal and used implicitly: conceptual Q&A vs derivation vs implement-from-scratch vs debug vs back-of-envelope estimation vs open design. Sources tend to specialise by format (Huyen = conceptual; Kashani = derivation; TorchLeet/Deep-ML = implement; scaling-book = estimation; ByteByteGo = design).
5. **Difficulty** is tagged explicitly in Huyen (per question), TorchLeet (Easy→Expert), Deep-ML (Easy/Medium/Hard) — scales are not comparable across sources.
6. **Company tag** axis (TorchLeet, aggregators) is common but unreliable.
7. **Role target** (MLE vs Applied Scientist vs AI Engineer vs RE/RS) silently shapes each source's difficulty; most sources are MLE/AI-Engineer, which explains the depth gap.

A plausible taxonomy would likely be two-dimensional (domain/lifecycle × format), with difficulty and source as tags — but that is for the taxonomy ticket to decide.
