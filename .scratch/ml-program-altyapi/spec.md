# Spec: ml-program altyapısı (repo, doğrulayıcı, tekrar betiği, Hoca ve Üretici skill'leri)

Status: ready-for-agent
Kaynak harita: [../ml-mulakat-programi/map.md](../ml-mulakat-programi/map.md)
Sözlük: `GLOSSARY.md` (planlama reposu kökünde)

## Problem Statement

Öğrenen için 450 saatlik ML/AI mülakat programının bütün kararları verildi (harita kapandı), ama programın çalışacağı bir yer yok. İçerik üretimi başlayamaz: banka sorularının yazılacağı repo, onları kontrol edecek doğrulayıcı, dilimleri üretecek Üretici ve içeriği yürütecek Hoca henüz yok. Bunlar olmadan:

- Üretilen her banka sorusunun şemaya, geçerlilik matrisine ve alt konu listesine uyup uymadığını kimse otomatik söyleyemez. Kodlu sorularda testlerin gerçekten çözümde geçip görevde kaldığı, Debug hatalarının gerçekten test düşürdüğü elle kontrol edilmek zorunda kalır.
- Hoca'nın tekrar planı (Leitner kutuları, tarihler) her oturumda modelin kafasında yeniden hesaplanır ve sessizce kayar.
- Öğrenen günü başlatacak, ünite yürütecek, soru çalışacak, mock yapacak tek bir tutarlı komut setine sahip olmaz.

## Solution

Ayrı bir program reposu (`ml-program`) kurulur. İçinde, içerik üretiminin ilk günü kullanılabilecek bütün altyapı bulunur, ama içerik yoktur:

- Repo iskeleti: içerik / kayıt / çalışma alanı ayrımı, tek uv ortamı, kökte Hoca kişiliği ve dosya haritası.
- **Doğrulayıcı**: repo kökünü alıp kalite kapısının 1–5. adımlarını çalıştıran tek komut. İçerik üretimi her sorudan ve her dilimden sonra, Hoca da bankaya dokunduğunda bunu çalıştırır.
- **Tekrar betiği**: tekrar YAML'ını okuyup yazan, Leitner hesabını yapan küçük komut. Hoca tekrar dosyasını elle düzenlemez, bu betiği çağırır.
- **Hoca**: 7 komut (`/gun /unite /sifirdan /soru /degerlendir /video /mock`), her biri ayrı skill, ortak protokoller tek referans klasöründe.
- **Üretici**: hafta kapanışında tetiklenen ayrı skill. Dilim ve dönem paketi üretir, kalite kapısını (otomatik adımlar + taze bağlamlı doğrulayıcı ajan) yürütür.

Altyapı bittiğinde içerik üretimi sıfırıncı dilimin kalanına (kaynak listesi, hata kataloğu, D1 dönem paketi, pilot hafta) doğrudan başlayabilir.

## User Stories

### Repo ve ortam

1. As the Öğrenen, I want the program to live in its own git repo separate from the planning repo, so that planning artifacts and learning artifacts never mix.
2. As the Öğrenen, I want a single `uv sync` to give me a CPU environment with JAX, PyTorch, NumPy and pytest, so that every Implement and Debug task runs without setup.
3. As the Öğrenen, I want an optional `video` dependency group with pinned Manim Community, so that video rendering does not bloat the default environment.
4. As the Öğrenen, I want an optional `gpu` dependency group with CUDA JAX and PyTorch for the rig's single 3090, so that kernel and profiling assignments run on real hardware.
5. As the Öğrenen, I want the repo split into içerik, `kayit/` and `calisma/`, so that I can see at a glance what changes during learning and what never does.
6. As the Hoca, I want a root CLAUDE.md that states my persona, language rules (English questions and terms, Turkish explanations, no LaTeX) and the file map, so that every skill starts from the same rules.
7. As the Öğrenen, I want rendered videos ignored by git while Manim sources and narration text are committed, so that the repo stays small and every video can be re-rendered.
8. As the Öğrenen, I want the empty skeleton folders (banka, dersler, plan, odevler, sinavlar, videolar, calisma, kayit) to exist from day one, so that content production writes into a known layout.

### Doğrulayıcı

9. As the Üretici, I want one command that validates the whole repo and exits non-zero on any violation, so that I can gate a dilim on a single result.
10. As the Üretici, I want each violation reported with the file, the rule broken, and a one-line reason, so that I can fix it without reading the validator.
11. As the Üretici, I want every banka sorusu's taxonomy values (tur, alan, format, zorluk, alt_konu) checked against `schema.yaml`, so that mislabelled questions never reach the Öğrenen.
12. As the Üretici, I want the tur–format geçerlilik matrisi enforced, so that, for example, a Debug question cannot be filed under ML Depth.
13. As the Üretici, I want the "Algorithms alanı yalnızca Practical Coding turunda" rule enforced, so that kılıklı problem labelling stays consistent.
14. As the Üretici, I want alt konu values checked against the controlled list for their alan, so that new alt konular are only added deliberately.
15. As the Üretici, I want ilgili_alanlar limited to 0–2 and different from the main alan, so that alan counts stay clean.
16. As the Üretici, I want id uniqueness and id format (`<alan>-NNNN-<slug>`) checked across the bank, so that references never collide.
17. As the Üretici, I want the validator to detect an id that changed or disappeared compared to the last commit, so that the "id hiç değişmez" rule holds even when a question moves alan.
18. As the Üretici, I want required body headings checked (Soru, Model cevap, Takip zinciri with `H<n> · L<k>` rings, 0–4 rings), so that the Hoca can address rings one by one.
19. As the Üretici, I want format-specific sections enforced (Değerlendirme ölçütleri for Design/Estimation, Çizim kontrol listesi for Whiteboard, Yerleştirilmiş hatalar for Debug), so that /degerlendir always has a rubric.
20. As the Üretici, I want required frontmatter fields checked (koken, kaynaklar, hedef_halka, sure_dk, durum, and cerceve on coded questions), so that the Hoca never meets a half-filled question.
21. As the Üretici, I want hedef_halka checked to point at an existing ring, so that tekrar never waits for a ring that does not exist.
22. As the Üretici, I want optional fields (makale, proje, havuz) checked for allowed values when present, so that filters in /soru and /mock work.
23. As the Üretici, I want coded questions checked for the folder shape (soru.md, gorev.py, test_gorev.py, cozum.py, optional cozum_numpy.py), so that the unit can copy them into a çalışma alanı.
24. As the Üretici, I want the validator to run each coded question's tests against the solution (must pass) and against the task (must fail), so that a task is never shipped already solved or unsolvable.
25. As the Üretici, I want Debug questions checked so that every yerleştirilmiş hata drops at least one test, so that no injected bug is invisible.
26. As the Üretici, I want the sessiz hata's failing test to fail by assertion rather than exception, so that "silent" really means the code runs and gives wrong numbers.
27. As the Üretici, I want every hata kataloğu id used in a Debug question to exist in the catalogue, so that bugs stay anchored to real incidents.
28. As the Üretici, I want every `kaynaklar` entry to resolve either to a source in the kaynak listesi or to a banka id, so that no question is derived from nowhere.
29. As the Üretici, I want L3 questions with `koken: original` rejected, so that frontier questions are always anchored.
30. As the Üretici, I want derived questions' rings checked for a trailing `Çapa:` line, so that the doğrulayıcı ajan can trace each claim.
31. As the Üretici, I want a LaTeX scan (`$`, `\frac` and similar) over the bank and unit pages, so that the no-LaTeX rule holds everywhere.
32. As the Üretici, I want every unit id, banka id, ödev and sınav referenced by a dönem planı to exist, so that /gun never points at a missing file.
33. As the Üretici, I want every unit page's banka id and seçilmiş video id references to resolve, so that units are references, not copies.
34. As the Üretici, I want seçilmiş video URLs checked over HTTP, with a switch to skip network checks offline, so that dead links are caught without blocking offline work.
35. As the Üretici, I want `rewritten` questions checked for not being verbatim copies of their recorded source text, so that unlicensed material is never copied.
36. As the Üretici, I want the hata kataloğu and kaynak listesi themselves validated (id format, required fields, anchor present), so that the references into them are trustworthy.
37. As the Öğrenen, I want the validator's output to show only counts for `havuz: sinav` questions, never their text or titles, so that I meet exam questions for the first time in the exam.
38. As the Üretici, I want to validate a single question or a single dilim as well as the whole repo, so that the per-question loop is fast.
39. As the Hoca, I want to run the validator after any change I make to the bank (for example promoting a mini soru), so that my edits obey the same rules as production.
40. As the Üretici, I want the validator to report `draft` questions referenced by a dönem planı or unit as errors, so that the Hoca only ever serves `verified` questions.

### Tekrar betiği

41. As the Hoca, I want a command that lists today's due tekrar kartları from the tekrar YAML, so that the tekrar bloğu starts from a deterministic list.
42. As the Hoca, I want a command that records a result for a card (deepest ring reached) and moves it per Leitner (1→3→7→14→30 days; hedef halkaya ulaşan bir kutu ilerler, kırılan 1. kutuya döner), so that scheduling never drifts.
43. As the Hoca, I want to add a newly studied banka sorusu as a card, so that every worked question enters tekrar.
44. As the Hoca, I want to add a hata kartı either linked to a banka id or carrying its own mini soru text, so that both card types live in one schedule.
45. As the Hoca, I want questions used in an exam added with the exam rule (kırılan 1. kutudan, geçen 2. kutudan), so that exam results feed tekrar.
46. As the Hoca, I want the betiği to read hedef_halka and ring structure from the bank by id, so that "geçti" is judged against the question's own threshold.
47. As the Hoca, I want the betiği to refuse `havuz: sinav` questions before they have been used in an exam, so that the pool stays unseen.
48. As the Hoca, I want the due list capped to what fits in ~30 minutes using sure_dk, with overflow carried to the next day, so that the tekrar bloğu stays fixed in length.
49. As the Öğrenen, I want the tekrar YAML to stay human-readable, so that I can inspect or repair it by hand if needed.
50. As the Hoca, I want the betiği to reject unknown card ids and malformed results with a clear error, so that a typo cannot corrupt the schedule.

### Hoca

51. As the Öğrenen, I want `/gun` to show today's plan (tekrar bloğu, algoritma bloğu, two harmanlanmış üniteler, or the hafif gün tasks) from the dönem planı and ilerleme, so that I never decide what to study.
52. As the Öğrenen, I want `/gun` to carry unfinished units to the next day and close kayma at hafta kapanışı, so that the plan follows my real progress.
53. As the Öğrenen, I want `/gun` on the hafif gün to run the hafta kapanışı (kayma, a look over the week's hata kaydı) and remind me to trigger the Üretici, so that the next dilim is produced on time.
54. As the Öğrenen, I want `/gun` at dönem end to list unfinished units and let me pick which to skip, so that skipped units are my decision.
55. As the Öğrenen, I want `/unite <id>` to walk the 9-step loop (soğuk deneme → seçilmiş video → Türkçe açıklama → pratik görev → 2–3 soru → optional video → çizim → İngilizce prova → hata kaydı), so that every unit feels the same.
56. As the Öğrenen, I want `/unite` to copy the pratik görev into my çalışma alanı and never touch the bank original, so that my attempts are mine.
57. As the Öğrenen, I want `/unite` to adapt emphasis using my hata kaydı without rewriting the pre-produced content, so that the unit is personal but verified.
58. As the Öğrenen, I want `/sifirdan <kavram>` to explain a concept assuming no prior knowledge, so that I can fill gaps the program assumed I had.
59. As the Öğrenen, I want `/soru` to fetch a `verified`, non-pool question (filterable by alan, alt konu, format, makale, proje) from topics I have already studied, so that practice matches where I am.
60. As the Öğrenen, I want the Hoca to open the takip zinciri ring by ring, score each 0–2, stop at 0, open only that ring's model cevap and log it, so that I learn exactly where I break.
61. As the Öğrenen, I want `/degerlendir` to run the tests first and then score doğruluk, sayısal kararlılık/kenar durumlar, verim, okunabilirlik 0–2 each (doğruluk ≤1 if any test fails), so that I get consistent code feedback with no total grade.
62. As the Öğrenen, I want `/degerlendir` to score an ödev's question part by the takip zinciri rule, so that ödev and unit questions are judged alike.
63. As the Öğrenen, I want `/degerlendir` on a Debug task to check my fixes against the Yerleştirilmiş hatalar list, so that I know which bugs I missed.
64. As the Öğrenen, I want `/video <kavram>` to first suggest a matching seçilmiş video from the catalogue, so that production cost is only paid when needed.
65. As the Öğrenen, I want `/video` to produce a Manim video in the background with the render → frame review → fix loop, so that my unit does not wait.
66. As the Öğrenen, I want `/video` to refuse beyond 2 videos per week, so that production stays within budget.
67. As the Öğrenen, I want `/mock <tur>` to switch to mülakatçı modu with the tur's real duration, no explanations, real-interviewer-level hints, so that rehearsal is honest.
68. As the Öğrenen, I want `/mock` to pick questions weighted toward weak areas, never from unstudied alt konular, so that mocks test what I should know.
69. As the Öğrenen, I want coding mocks to have me write to a file and run tests afterwards, so that mock coding matches the real format.
70. As the Öğrenen, I want `/mock` to end with a rubric (per-signal strong/weak and strong hire … no hire), then switch to öğretmen modu and log every break, so that a mock becomes study material.
71. As the Öğrenen, I want ara sınav and Final haftası loops to run as sequences of `/mock` turns drawn from the sınav havuzu, so that exams reuse one protocol.
72. As the Öğrenen, I want the Hoca to write a sınav raporu after each ara sınav, so that next dönem's emphasis follows my results.
73. As the Öğrenen, I want to dictate prose answers and provas with voxtype into the prompt and get feedback on content and structure, not language, so that I practise speaking answers.
74. As the Öğrenen, I want to hand the Hoca a photo of my drawing and get feedback against the çizim kontrol listesi, so that whiteboard practice has a checklist.
75. As the Öğrenen, I want the Hoca to write only to `kayit/` and `calisma/`, so that content is never altered during learning.
76. As the Öğrenen, I want hata kaydı lines in one fixed format (`tarih | ünite | alan/alt konu | tek satır | durum`), so that the Üretici and tekrar can read them.
77. As the Öğrenen, I want the Hoca to make one automatic commit of `kayit/` and `calisma/` at day close with a `D1-H2-G3` message and never push, so that every day is recoverable.
78. As the Hoca, I want the shared protocols (takip zinciri scoring, hata kaydı line format, tekrar rules, mock rubric, file map) in one reference folder referenced by name, so that no rule is copied across skills.

### Üretici

79. As the Öğrenen, I want to trigger the Üretici with one command at hafta kapanışı and have it run in the background, so that production does not eat my 5 hours.
80. As the Üretici, I want to read the dönem planı, ilerleme, hata kaydı and sınav raporu before producing, so that emphasis follows weak alt konular.
81. As the Üretici, I want to produce week N+2 at the close of week N and wait if the Öğrenen is behind, so that the 1-week buffer holds and feedback stays fresh.
82. As the Üretici, I want to produce a dönem paketi (dönem planı, CS336 dilimlemesi, sınav havuzu with ≥2 L2–L3 per alt konu) before the dönem starts, so that the dönem is fully planned.
83. As the Üretici, I want to produce a base Implement before any Debug that needs it, gate it, and only then inject 2–4 catalogue bugs (≥1 silent), so that every Debug has a verified correct version.
84. As the Üretici, I want to run the validator after every question and on the whole dilim, so that problems are caught early.
85. As the Üretici, I want a fresh-context doğrulayıcı ajan to do a blind second derivation of every model cevap and to check every Çapa line against the source, so that technical errors are caught by someone other than the author.
86. As the Üretici, I want at most 2 fix rounds per failing item, after which the item is dropped and the next unit of the same ders is pulled forward in the plan, so that a bad item never blocks a dilim.
87. As the Öğrenen, I want dropped items reported to me in one line at hafta kapanışı (pool items only as counts), so that I know what changed without spoiling anything.
88. As the Üretici, I want to keep the dönem planı's unit list fixed and only shift emphasis, so that the program shape stays stable.
89. As the Üretici, I want new kaynak listesi or hata kataloğu entries allowed only during a dönem paketi, so that anchors change deliberately.
90. As the Üretici, I want to freeze copies of öğrenen projesi documents (with source path and commit/date header) during the D3 paketi, so that the gate works without TRUBA access.

## Implementation Decisions

**Modüller** (beş derin modül, her birinin küçük bir arayüzü var):

1. **Repo iskeleti.** Yerleşim [11 numaralı bilet](../ml-mulakat-programi/issues/11-proje-repo-yapisi.md) kararına birebir uyar: içerik grupları (banka, dersler, plan, ödevler, sınavlar, videolar), `kayit/` (yalnızca Hoca yazar), `calisma/` (commit'lenir). Tek uv projesi; varsayılan CPU kurulumu + `video` ve `gpu` dependency group'ları. Manim Community sürümü sabitlenir. Render çıktıları gitignore'da, Git LFS yok.

2. **Şema ve doğrulayıcı.** Bankanın kuralları tek bir `schema.yaml`'da veri olarak durur: tur/alan/format/zorluk değerleri, geçerlilik matrisi, alan başına alt konu listeleri, Algorithms kuralı, format başına zorunlu bölümler, alan kısaltmaları (`math cml dlf tll sys msd alg bio`), `proje` değerleri (3 sabit id), `havuz` değerleri. Doğrulayıcı kural eklemek için kod değil şema değiştirilecek biçimde yazılır (matris ve listeler kodda sabit değil).
   - Arayüz: tek komut, hedef olarak repo kökü (varsayılan), bir dilim ya da tek bir soru yolu alır; ağ kontrollerini kapatan bir bayrak vardır. Çıkış kodu 0/1; her ihlal `dosya · kural · açıklama` satırı. Havuz soruları çıktıda yalnızca sayı olarak görünür.
   - pytest üzerinde çalışır (karar: "pytest doğrulayıcı"); kodlu soruların testleri alt süreçte, sorunun kendi klasöründe, önce `cozum.py`'ye sonra `gorev.py`'ye bağlanarak koşturulur.
   - Kalite kapısının 1–5. adımlarını kapsar: şema/matris/alt konu/id; kodlu soru testleri (çözümde geçer, görevde kalır; Debug'da her hata ≥1 test düşürür, sessiz hatanınki assertion ile); plan ve ünite referansları + seçilmiş video HTTP kontrolü; LaTeX taraması; köken/kaynak çözümlemesi, L3'te `original` yasağı, `Çapa:` satırı, `rewritten` için birebir kopya kontrolü.
   - Id değişmezliği git geçmişine karşı kontrol edilir (son commit'teki id kümesi yeni kümede bulunmalı).
   - Debug sorularında "her hata ≥1 test düşürür" kontrolü için her yerleştirilmiş hatanın tek başına uygulanabilir olması gerekir. Karar: `## Yerleştirilmiş hatalar` bölümündeki her madde, hatanın yerini doğrulayıcının `cozum.py` üzerinde tek tek uygulayabileceği kadar kesin tanımlar (örn. her hata için küçük bir diff bloğu). Kesin biçim uygulamada belirlenir, ama soru formatına yeni frontmatter alanı eklenmez.

3. **Kaynak listesi ve hata kataloğu biçimi.** İki YAML dosyasının şeması bu spec'te tanımlanır ve doğrulayıcı tarafından kontrol edilir: kaynak listesi alan → kaynaklar (kısa id, URL/konum, Bio-ML altında ayrı `proje` grubu); hata kataloğu `hk-NNN` id'li maddeler (kategori, açıklama, çapa). Altyapı yalnızca biçimi ve testler için küçük bir tohum içerir; asıl doldurma (~25–40 madde, alan başına kaynaklar) içerik üretimine aittir.

4. **Tekrar betiği.** Tekrar YAML'ının tek yazarı. Arayüz dört işlemden ibaret:
   - `bugun`: zamanı gelen kartları `sure_dk` toplamı ~30 dk'yı aşmayacak biçimde listeler; taşanlar ertesi güne kalır.
   - `ekle`: banka sorusu kartı, hata kartı (banka id'ye bağlı ya da mini soru metni taşıyan) veya sınav sonrası kart ekler.
   - `sonuc`: bir kart için ulaşılan en derin halkayı kaydeder; hedef halkaya (bankadan okunur) ulaşan bir kutu ilerler, kırılan 1. kutuya döner. Aralıklar 1 → 3 → 7 → 14 → 30 gün.
   - Sınav sonrası ekleme: kırılan soru 1. kutudan, geçen 2. kutudan başlar.
   - Kurallar: `havuz: sinav` sorusu sınavda kullanılmadan eklenemez; bilinmeyen id ve bozuk girdi hata verir ve dosyaya dokunulmaz. Bugünün tarihi parametre olarak verilebilir (testler için).
   - Dosya insan tarafından okunabilir YAML kalır; soğuk denemeler ve çizim alıştırmaları kart olmaz.

5. **Hoca skill'leri.** 7 komutun her biri ayrı skill; ortak protokoller tek referans klasöründe (takip zinciri puanlaması, hata kaydı satır biçimi, tekrar kuralları ve tekrar betiğinin kullanımı, mock protokolü ve rubriği, dosya haritası). Skill'ler kuralları kopyalamaz, adıyla başvurur. Kişilik ve dil kuralları kök CLAUDE.md'de. Davranış kararları [07](../ml-mulakat-programi/issues/07-hoca-sistemi.md), [06](../ml-mulakat-programi/issues/06-ornek-unite-formati.md), [09](../ml-mulakat-programi/issues/09-gunluk-ve-haftalik-calisma-sablonu.md), [10](../ml-mulakat-programi/issues/10-sinav-ve-odev-formati.md) biletlerinde sabit; özetle:
   - Hoca yalnızca `verified` ve (sınav dışında) `havuz: sinav` olmayan soruları getirir; çalışılmamış alt konulardan soru getirmez.
   - Hoca yalnızca `kayit/` ve `calisma/`'ya yazar; bankayı değiştirdiği tek durum mini soruyu bilinçli kararla bankaya almaktır ve ardından doğrulayıcıyı çalıştırır.
   - Tekrar durumu yalnızca tekrar betiği üzerinden değişir.
   - Gün kapanışında `kayit/` + `calisma/` tek otomatik commit, mesaj `D1-H2-G3`, push yok.
   - `/video`: önce `secilmis.yaml` taraması; üretim arka planda, Manim CE, `-ql` render → kare/kontakt sayfası → inceleme → düzeltme döngüsü; ses altyazı ile (TTS sonraya kalabilir); haftada ≤2 video sınırı kayıttan sayılır. Kaynak ve seslendirme metni commit'lenir.
   - Ara sınav ve Final haftası ayrı komut değildir; `/mock` turlarının sıralı dizisidir ve sınav klasöründeki tanımı okur. Sınav raporu `kayit/` altına yazılır.

6. **Üretici skill'i.** Hoca'dan ayrı, 7 komuta eklenmeyen tek skill. Davranış [12](../ml-mulakat-programi/issues/12-icerik-uretim-sirasi-ve-devri.md), [13](../ml-mulakat-programi/issues/13-kaynagi-olmayan-alanlarda-soru-turetme.md), [15](../ml-mulakat-programi/issues/15-bio-ml-ogrenen-projeleri.md) biletlerinde sabit. İki giriş noktası: **dilim üret** (hafta N kapanışında N+2; öğrenen gerideyse bekler) ve **dönem paketi üret**. Kalite kapısını yürütür: her sorudan sonra ve dilim sonunda doğrulayıcı; ardından taze bağlamlı doğrulayıcı ajan (kör ikinci türetim + çapa izlenebilirliği). En fazla 2 düzeltme turu; geçemeyen ünite dilimden çıkar ve dönem planında aynı dersin sonraki ünitesi öne alınır; çıkarılanlar hafta kapanışında tek satırla (havuz için yalnızca sayı) bildirilir. Debug için taban Implement önce üretilip kapıdan geçirilir. Proje belgelerinin dondurulmuş kopyaları D3 paketinde, kaynak yolu ve commit/tarih başlığıyla alınır.

**Veri sözleşmeleri** (biletlerde sabit, burada yalnızca altyapının dayandığı kısımlar):
- Banka sorusu: YAML frontmatter + sabit başlıklı gövde; kodlu sorular klasör. Alanlar ve gövde düzeni [08](../ml-mulakat-programi/issues/08-soru-bankasi-fiziksel-formati.md) cevabındaki gibidir, artı `havuz` (10) ve `proje` (15). Yeni alan eklenmez.
- Ünite id `<ders-kodu>-NN` (örn. `llm1-04`), banka id `<alan>-NNNN`; ikisi de değişmez.
- Hata kaydı satırı: `tarih | ünite | alan/alt konu | tek satır | durum`; ünite sütunu ödev/sınavda `ödev`, `ara sınav`, `final`.
- Dönem planı: dönem başına bir YAML (hafta × gün → ünite id'leri + ödev/sınav yuvaları). Altyapı yalnızca şemasını ve doğrulayıcı kontrolünü getirir.
- Seçilmiş video kataloğu: kayıt başına id, URL, başlangıç–bitiş zaman damgası, alt konu(lar).

## Testing Decisions

**İyi test**: yalnızca dışarıdan görünen davranışı sınar. Testler komutu çağırır ve çıkış kodunu, çıktı satırını ya da yazılan dosyayı kontrol eder; iç fonksiyonlara, ara veri yapılarına ya da kural sırasına bakmaz. Bir kural yeniden yazıldığında davranış aynıysa hiçbir test kırılmamalıdır.

**Seam 1 — doğrulayıcı komutu (ana seam)**:
- Her test geçici bir dizinde küçük bir örnek repo kurar (bir `schema.yaml`, birkaç banka sorusu, isteğe bağlı plan/ünite/kaynak listesi/katalog), doğrulayıcıyı çalıştırır, çıkış kodunu ve ihlal satırını kontrol eder.
- Bir "altın" geçerli repo tüm kontrollerden temiz geçer. Her kural için bu repodan türetilmiş, yalnızca o kuralı bozan bir varyant vardır (yanlış matris eşleşmesi, listede olmayan alt konu, tekrarlanan id, değişmiş id, eksik bölüm, olmayan hedef halka, görevde geçen test, çözümde kalan test, test düşürmeyen hata, exception ile düşen sessiz hata, çözülmeyen kaynak, L3 `original`, LaTeX, plan'da olmayan id, `draft` referansı, birebir kopya `rewritten` ...).
- Havuz gizliliği: havuz sorusu içeren bir repoda çıktının o sorunun başlığını ya da metnini içermediği test edilir.
- Ağ kontrolü testlerde kapalı bayrakla çalışır; HTTP kontrolü yerel bir sahte sunucuya karşı ayrı tek bir testle sınanır.

**Seam 2 — tekrar betiği**:
- Her test bir tekrar YAML'ı ve küçük bir banka verir, bugünün tarihini sabitler, komutu çalıştırır ve yazılan YAML'ı ya da günün listesini kontrol eder.
- Kapsam: kutu ilerleme ve 1. kutuya dönüş, aralık tablosu, hedef halka eşiği (bonus L3'ten önceki halka), sınav sonrası 1./2. kutu başlangıcı, mini sorulu hata kartı, 30 dk sınırı ve taşma, havuz sorusu reddi, bilinmeyen id ve bozuk girdide dosyanın değişmemesi.

**Otomatik testi olmayanlar**: Hoca'nın 7 skill'i ve Üretici prompt dosyalarıdır. Bunları sıfırıncı dilimin pilot haftası (D1 1. hafta) ve doğrulayıcı ajan denetler; pilot hafta kapanışında ünite formatı ve şablonlar bir kez gözden geçirilir. Skill'lerin deterministik kısmı (tekrar hesabı, kapı kontrolleri) bilerek iki seam'in arkasına çekilmiştir.

**Önceki örnek**: Planlama reposundaki ünite prototipinin pytest testleri (attention implementasyonu ve hatalı MHA debug testleri) davranış sınayan test tarzını gösterir: naif referansa eşitlik, gelecek sızıntısı yok, head bağımsızlığı, sayısal kararlılık. Kodlu banka sorularının testleri ve doğrulayıcının "çözümde geçer / görevde kalır" kontrolü bu tarzı varsayar. Program reposunda başka bir test öncülü yoktur.

## Out of Scope

- **İçerik üretimi**: banka soruları, üniteler, dönem planlarının içeriği, D1 dönem paketi, pilot hafta ve 2. hafta, ödevler, sınav havuzu, CS336 dilimlemesi.
- Kaynak listesinin ve hata kataloğunun doldurulması (yalnızca biçim ve test tohumu bu spec'te).
- Seçilmiş video kataloğunun kayıtları ve video tavanına göre kırpma.
- Öğrenen projesi belgelerinin dondurulmuş kopyalarının fiilen alınması (Üretici'nin bu davranışı kapsamda, D3 paketindeki çalıştırması değil).
- Önceden üretilmiş herhangi bir üretilmiş video; TTS seslendirme (altyazı yeterli, TTS sonraki bir karar).
- Başarı ölçümü, toplam not, seviye tespit sınavı, interaktif web demoları, dağıtık eğitimin gerçek donanımda koşturulması (haritanın kapsam dışı listesi).
- Otomatik push ya da uzak repo kurulumu.

## Further Notes

- Bütün kararların gerekçesi harita ve biletlerde; bu spec onları yeniden tartışmaz, yalnızca altyapıya çevirir. Çelişki görülürse bilet cevabı geçerlidir.
- Doğrulayıcının kuralları şemada veri olarak tutulduğu için yeni bir alt konu ya da tur–format değişikliği kod değişikliği gerektirmez; bu, "yeni alt konu yalnızca bilinçli kararla" kuralının uygulandığı yerdir (şema diff'i commit'te görünür).
- Önerilen uygulama sırası: repo iskeleti → şema + doğrulayıcı (altın repo ve bozuk varyantlarla, test önce) → tekrar betiği → Hoca ortak protokol klasörü ve 7 skill → Üretici. İlk iki adım bitince içerik üretimi kaynak listesi ve hata kataloğuyla paralel başlayabilir.
- Bu spec, sıfırıncı dilimin altyapı yarısıdır; diğer yarısı (D1 paketi, pilot hafta, kaynak listesi, katalog) içerik üretimi işi olarak ayrıca devredilir.
