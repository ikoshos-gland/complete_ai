# 02 — Video ve ders kaynakları envanteri

Bilet: [../issues/02-video-ve-ders-kaynaklari.md](../issues/02-video-ve-ders-kaynaklari.md) · Tarih: 2026-11-01

## Türkçe özet

- **Omurga dersler.** Görsel omurga birkaç dersten oluşur:
  - LLM ve sistemler için en güncel, en "frontier-lab" odaklı ders **Stanford CS336 (Bahar 2026)**: 19 ders (~25 sa), 5 ağır ödev (tokenizer, Triton FlashAttention2, dağıtık eğitim, scaling law, veri, SFT/RL).
  - **Karpathy Zero to Hero** (8 ders, ~14,5 sa) derin öğrenme ve backprop sezgisini kodla kurar.
  - Transformer'ın görsel sezgisi için **3Blue1Brown** bölüm 5–7 var.
  - Kısa ve modern bir transformer/LLM turu için **Stanford CME295 (Güz 2025)** (9 ders, ~18 sa) uygun.
- **Dağıtık eğitim (yalnızca teori).** En iyi kaynaklar video değil, metin:
  - Hugging Face **Ultra-Scale Playbook** (2025) ve DeepMind **How to Scale Your Model** (2025).
  - Video olarak bunları CS336'nın paralellik dersleri, **GPU MODE** ve **MIT 6.5940 (Song Han)** tamamlar.
- **Matematik ve klasik ML.** Kaynaklar eski ama hâlâ en iyileri: 3B1B, MIT 18.06/18.065 (Strang), CS229 (2018, Ng), Cornell CS4780, MacKay. Bunlar seçici izlenmeli.
- **Bio-ML.** Video kaynakları zayıf ve dağınık:
  - Ders düzeyinde yalnızca MIT 6.874 (2020, eski) ve Kellis MLCB24 dersleri var.
  - AlphaFold, ESM ve Evo için konuşmalar (Jumper, AlQuraishi, Bouatta, Ovchinnikov) ve makale okuma gerekiyor.
- **Toplam video süresi.** Tüm önerilenlerin toplamı ~270 sa. Programın 450 saatlik bütçesi için **çekirdek liste ~175 sa** öneriliyor; kalan süre ödev, kod ve soru çözümüne ayrılacak.
- **Özel animasyon adayları.** Görsel anlatımın en zayıf olduğu ve mülakatta en çok sorulan konular:
  - KV cache ve PagedAttention, prefill/decode ve roofline
  - FlashAttention tiling ve online softmax
  - ZeRO/FSDP ve kolektif iletişim, pipeline bubble
  - Kuantizasyon (outlier, GPTQ/AWQ)
  - MoE yönlendirme ve all-to-all
  - PPO/DPO/GRPO matematiği, RoPE
  - AF2 Evoformer/IPA, AF3 difüzyonu
  - ESM ile sıfır-atış varyant skoru (Mert'in araştırmasıyla doğrudan bağlantılı)

**Doğrulama notasyonu.** Her kaynağın doğrulama durumu şöyle işaretlendi:
- **[V]**: Birincil kaynakta (ders sitesi, resmi repo veya OCW) bu araştırma sırasında doğrulandı.
- **[V2]**: Yalnızca ikincil listelerde (aggregator, blog) doğrulandı.
- **[K]**: Önceki bilgiye dayanıyor; izlemeden önce URL ve süreyi kontrol et.

Süreler doğrulanmadıysa tahmindir (ders sayısı × ders uzunluğu).

---

## 1. Matematik temelleri (lineer cebir, olasılık, kalkülüs, bilgi teorisi, optimizasyon)

| Kaynak | Konular | Süre | Seviye | Kod/ödev | Yıl | URL |
|---|---|---|---|---|---|---|
| 3Blue1Brown, *Essence of Linear Algebra* [K] | vektör uzayları, lineer dönüşüm, determinant, özdeğer, değişim tabanı | ~3 sa (16 video) | sezgi tazeleme; orta-ileri için hızlı | yok | 2016 | https://www.3blue1brown.com/topics/linear-algebra |
| 3Blue1Brown, *Essence of Calculus* [K] | türev, zincir kuralı, Taylor | ~3 sa | tazeleme | yok | 2017 | https://www.3blue1brown.com/topics/calculus |
| MIT 18.065, *Matrix Methods in Data Analysis, Signal Processing, and ML* (Strang) [V] | SVD, PCA, düşük rank, en küçük kareler, GD/SGD, backprop yapısı | 34 video ≈ 28 sa | orta-ileri; ML'e doğrudan bağlanıyor | problem setleri (PDF) | 2018 | https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/ |
| MIT 18.06SC, *Linear Algebra* (Strang) [K] | klasik lineer cebir | ~30 sa | yalnızca boşluk varsa | ödev ve sınavlar | 2011 | https://ocw.mit.edu/courses/18-06sc-linear-algebra-fall-2011/ |
| MIT 18.S096, *Matrix Calculus for ML and Beyond* (Edelman & Johnson) [K] | matris türevleri, Jacobian, vektör-Jacobian çarpımı, autodiff | ~8 sa | ileri; mülakatta "softmax veya LayerNorm'un türevini al" sorusu için birebir | ödev var | IAP 2023 | https://ocw.mit.edu/courses/18-s096-matrix-calculus-for-machine-learning-and-beyond-january-iap-2023/ |
| Harvard Stat 110 (Blitzstein) [K] | olasılık, dağılımlar, koşullu beklenti, MGF | ~35 sa (seçici: ~10 sa) | orta-ileri | problem setleri | 2013 | https://projects.iq.harvard.edu/stat110 |
| MIT RES.6-012, *Introduction to Probability* (Tsitsiklis) [K] | kısa klipler hâlinde olasılık | ~15 sa (seçici) | orta | çözümlü problemler | 2018 | https://ocw.mit.edu/courses/res-6-012-introduction-to-probability-spring-2018/ |
| David MacKay, *Information Theory, Pattern Recognition and Neural Networks* [K] | entropi, KL, kaynak/kanal kodlama, Bayes çıkarımı | 16 ders ≈ 16 sa (seçici: 6 sa) | ileri | kitap alıştırmaları (ücretsiz kitap) | 2012 | https://www.inference.org.uk/itprnn_lectures/ |
| Stanford EE364A, *Convex Optimization* (Boyd) [K] | konvekslik, dualite, KKT | ~20 sa (seçici: 6 sa) | ileri | ödev (CVXPY) | 2023 | https://web.stanford.edu/class/ee364a/ |

**Alan için tahmini süre:** çekirdek ~25 sa, tam liste ~45 sa.

**Önerilen çekirdek:** 18.065'in seçili dersleri, 18.S096, MacKay'in 1–6. dersleri ve 3B1B (yalnızca tazeleme olarak).

## 2. Klasik ML

| Kaynak | Konular | Süre | Seviye | Kod/ödev | Yıl | URL |
|---|---|---|---|---|---|---|
| Stanford CS229 (Andrew Ng) [V2] | GLM, üretici/ayırıcı modeller, SVM ve kernel, bias-variance, EM, PCA/ICA, RL'e giriş | 20 ders ≈ 25 sa | orta-ileri; türetim ağırlıklı | ödev ve notlar (cs229.stanford.edu) | Güz 2018 (en yeni halka açık tam seri) | https://www.youtube.com/playlist?list=PLoROMvodv4rMiGQp3WXShtMGgzqpfVfbU |
| Cornell CS4780 (Kilian Weinberger) [K] | kNN, perceptron, MLE/MAP, bias-variance, kernel, GP, boosting/bagging, ağaçlar | ~37 ders ≈ 30 sa (seçici: 12 sa) | orta-ileri; sezgi çok iyi | notlar ve projeler | 2018 | https://www.cs.cornell.edu/courses/cs4780/2018fa/ |
| StatQuest (Josh Starmer) [K] | XGBoost, gradient boosting, ağaçlar, ROC/AUC, regularization | ~5 sa seçili | hızlı görsel tazeleme | yok | sürekli | https://www.youtube.com/@statquest |
| Caltech, *Learning from Data* (Abu-Mostafa) [K] | VC boyutu, genelleme, bias-variance | 18 ders ≈ 18 sa (seçici: 4 sa) | teori | ödev | 2012 | https://work.caltech.edu/telecourse |

Not: CS229'un Güz 2025 sitesi var (https://cs229.stanford.edu/), ancak bu sürümün halka açık videosu doğrulanamadı.

**Alan için tahmini süre:** çekirdek ~20 sa, tam liste ~35 sa.

## 3. Derin öğrenme (temeller, CNN, optimizasyon, üretici modeller, RL temeli)

| Kaynak | Konular | Süre | Seviye | Kod/ödev | Yıl | URL |
|---|---|---|---|---|---|---|
| **Karpathy, *Neural Networks: Zero to Hero*** [V] | micrograd ile backprop, makemore (bigram, MLP, BatchNorm, aktivasyon ve gradyan istatistikleri, elle backprop, WaveNet), GPT, GPT tokenizer | 8 ders, **14 sa 32 dk** (sayfa "ongoing" diyor) | her seviye; orta-ileri için "backprop ninja" ve BatchNorm dersleri çok değerli | baştan sona kod (repo: karpathy/nn-zero-to-hero) | 2022–2024 | https://karpathy.ai/zero-to-hero.html |
| Karpathy, *Let's reproduce GPT-2 (124M)* ve *Deep Dive into LLMs like ChatGPT* [K] | karışık hassasiyet, torch.compile, FlashAttention, DDP; LLM yaşam döngüsü | ~4 sa + ~3,5 sa | orta-ileri | kod (build-nanogpt) | 2024–2025 | https://www.youtube.com/@AndrejKarpathy |
| 3Blue1Brown, *Neural Networks* (bölüm 1–7) [V] | gradyan inişi, backprop kalkülüsü, transformer (bl. 5), attention (bl. 6, 26 dk, 2024), MLP'lerin bilgiyi nasıl depoladığı (bl. 7, Ağustos 2024) | ~2,5 sa | görsel sezgi; en iyi attention anlatımı | yok | 2017–2024 | https://www.3blue1brown.com/topics/neural-networks |
| Stanford CS231N (Bahar 2025) [V2] | CNN, eğitim dinamikleri, ViT, üretici modeller, self-supervised öğrenme, 3D, robotik | 18 ders ≈ 22 sa (seçici: 8 sa) | orta-ileri | 3 ödev (numpy ve PyTorch) | 2025 | https://cs231n.stanford.edu/2025/schedule.html |
| MIT 6.S184, *Intro to Flow Matching and Diffusion Models* [V] | SDE/ODE, flow matching, score matching, CFG, DiT/VAE; protein tasarımı konuk dersi (2025) | ~6–8 sa ders + lecture notes (arXiv 2506.02070) | ileri; difüzyonun matematiği için en iyi kısa kaynak | 3 lab | IAP 2025 ve 2026 | https://diffusion.csail.mit.edu/2026/ |
| MIT 6.S191, *Intro to Deep Learning* [V] | genel tur | ~9 ders × 1 sa | **başlangıç**; Mert için büyük ölçüde atlanabilir | 3 Colab lab | Ocak 2026 | https://introtodeeplearning.com/ |
| Berkeley CS285, *Deep RL* (Levine) [V] | policy gradient, actor-critic, varyans azaltma, PPO/TRPO altyapısı, offline RL | ~25 ders (seçici: ~8 sa, RLHF arka planı için) | ileri | 5 ödev | Güz 2023 (kayıtlar sitede) | https://rail.eecs.berkeley.edu/deeprlcourse-fa23/ |

**Alan için tahmini süre:** çekirdek ~35 sa (Karpathy 14,5 sa + GPT-2 4 sa + 3B1B 2,5 sa + 6.S184 7 sa + CS285 seçili 8 sa), tam liste ~60 sa.

## 4. Transformer ve LLM (pretraining, tokenizasyon, RLHF/DPO, scaling law, çıkarım, KV cache, kuantizasyon, MoE)

| Kaynak | Konular | Süre | Seviye | Kod/ödev | Yıl | URL |
|---|---|---|---|---|---|---|
| **Stanford CS336, *Language Modeling from Scratch*** (Liang & Hashimoto) [V] | tokenizasyon; PyTorch ve kaynak hesabı; mimari ve hiperparametreler; attention alternatifleri ve MoE; GPU/TPU; kernel ve Triton; paralellik (2 ders); scaling law (2 ders); çıkarım; değerlendirme; veri (2 ders); SFT/RLHF; RLVR; hizalama ve multimodalite; konuklar (Selsam, Dan Fu) | 19 ders × 80 dk ≈ **25 sa** | **ileri; Research Engineer mülakatının birebir müfredatı** | **5 ağır ödev:** (1) BPE, Transformer, AdamW, eğitim; (2) profiling, Triton FlashAttention2, DDP; (3) scaling law fit; (4) Common Crawl filtreleme ve dedup; (5) SFT ve RL ile matematik muhakemesi, opsiyonel DPO | **Bahar 2026** (2025 ve 2024 arşivleri de var) | https://cs336.stanford.edu/ · playlist 2026: https://www.youtube.com/playlist?list=PLoROMvodv4rMqXOcazWaTUHhq-yembLCV · 2025 [V2]: https://www.youtube.com/playlist?list=PLoROMvodv4rOY23Y0BoGoBGgQ1zmU_MT_ |
| Stanford CME295, *Transformers & LLMs* (Afshine & Shervine Amidi) [V2] | transformer, transformer tabanlı modeller, LLM temelleri, eğitim, tuning (SFT, RLHF), muhakeme, ajanlar, değerlendirme, güncel trendler | 9 ders × ~2 sa ≈ 18 sa | orta-ileri; görsel ve derli toplu (yazarlar "cheatsheet" serileriyle tanınıyor) | slaytlar ve sınavlar açık | Güz 2025 (Güz 2026 da başlamış görünüyor) | https://cme295.stanford.edu/ (YouTube: Stanford Online) |
| Stanford CS224N (Manning) [V] | word vectors, RNN, transformer, pretraining, post-training (RLHF/DPO), PEFT, ajan/RAG, muhakeme | Bahar 2024 halka açık: ~18 ders ≈ 22 sa (seçici: 6 sa) | orta-ileri | ödevler ve GPT-2 projesi | 2024 halka açık; **Kış 2026 kayıtları halka açık değil** | https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D · https://web.stanford.edu/class/cs224n/ |
| Stanford CS25, *Transformers United* (V5 kayıtları; V6 sürüyor) [V] | araştırmacı konuşmaları (Hinton dahil), güncel trendler | konuşma başına ~1 sa (seçici: 5 sa) | ileri, seminer | yok | 2025–2026 | https://web.stanford.edu/class/cs25/recordings |
| Umar Jamil (YouTube) [K, başlıklar ve süreler doğrulanmalı] | LLaMA mimarisi (RoPE, RMSNorm, GQA, KV cache) ve sıfırdan kodlanması, Mistral/Mixtral (MoE, sliding window), RLHF/PPO, DPO, kuantizasyon, Triton ile FlashAttention (~7 sa), PyTorch ile dağıtık eğitim | video başına 1–7 sa; seçili toplam ~20 sa | orta-ileri; matematik ve kodu satır satır anlatıyor | kod (GitHub: hkproj) | 2023–2025 | https://www.youtube.com/@umarjamilai |
| Karpathy, *Let's build the GPT Tokenizer* (Zero to Hero'nun parçası) [V] | BPE, tiktoken, özel token'lar | 2 sa 13 dk | orta | kod | 2024 | https://karpathy.ai/zero-to-hero.html |

**Alan için tahmini süre:** çekirdek ~55 sa (CS336 25 sa + CME295 seçili 10 sa + Umar Jamil seçili 15 sa + CS25 5 sa), tam liste ~85 sa.

## 5. ML sistemleri ve dağıtık eğitim (yalnızca teori; donanım yok)

| Kaynak | Konular | Süre | Seviye | Kod/ödev | Yıl | URL |
|---|---|---|---|---|---|---|
| **Hugging Face, *The Ultra-Scale Playbook*** [V] | tek GPU'dan binlerce GPU'ya: aktivasyon yeniden hesaplama, gradyan biriktirme, DP, ZeRO 1–3, TP, SP, CP (ring attention), PP (1F1B, interleaved), EP, iletişim ve hesap örtüşmesi, kernel füzyonu. 512 GPU'ya kadar 4000'den fazla deneye dayanıyor | metin + etkileşimli grafikler; okuma ~12–15 sa | ileri; **mülakattaki dağıtık eğitim sorularının ana kaynağı** | nanotron/picotron kodu | 2025 | https://huggingface.co/spaces/nanotron/ultrascale-playbook |
| **Google DeepMind, *How to Scale Your Model*** (Austin, Douglas, Frostig, Pope ve diğerleri) [V] | roofline analizi, TPU/GPU donanımı, sharding notasyonu, DP/FSDP/TP/PP'nin iletişim maliyetleri, çıkarımda gecikme ve throughput | metin; okuma ~12 sa | ileri; "kaç GPU, ne kadar iletişim" tarzı soruların hesap pratiği | alıştırma problemleri | 2025 | https://jax-ml.github.io/scaling-book/ |
| CS336, ders 5–8 ve 10 (GPU, kernel/Triton, paralellik ×2, çıkarım) [V] | yukarıdakilerin video karşılığı | ~7 sa (bölüm 4 ile örtüşüyor) | ileri | ödev 2 | 2026 | https://cs336.stanford.edu/ |
| GPU MODE (eski adı CUDA MODE) [V] | ~60 numaralı ders; seçilecekler: 1 (profiling), 8 (CUDA performans kontrol listesi), 12 (FlashAttention), 13 (Ring Attention), 14 (Triton), 17 (NCCL), 30 (quantized training), 36 (CUTLASS ve FA3), 39 (TorchTitan), 40 (FlashInfer), 69 (4-bit eğitim) | seçili ~12 ders ≈ 15 sa | ileri, uygulayıcı | slayt ve kod | 2024–2026 | https://github.com/gpu-mode/lectures · https://www.youtube.com/@GPUMODE |
| MIT 6.5940, *TinyML and Efficient Deep Learning Computing* (Song Han) [V] | pruning, kuantizasyon (I/II), NAS, distilasyon, LLM deployment (AWQ, SmoothQuant), uzun bağlam, dağıtık eğitim (I/II) | ~23 ders × 75 dk; seçici ~12 sa | ileri | 5 lab | Güz 2024 kayıtlı; Güz 2026 sürüyor | https://hanlab.mit.edu/courses/2024-fall-65940 |

Not: serving konusu (vLLM/PagedAttention, continuous batching, speculative decoding) için CS336'nın çıkarım dersi ve GPU MODE'un FlashInfer dersi yeterli. Ayrıca vLLM makalesi okunmalı.

**Alan için tahmini süre:** çekirdek ~35 sa (Playbook 12 + Scaling Book 8 + GPU MODE seçili 8 + 6.5940 seçili 7), tam liste ~55 sa.

## 6. Algoritmalar / LeetCode

| Kaynak | Konular | Süre | Seviye | Kod/ödev | Yıl | URL |
|---|---|---|---|---|---|---|
| NeetCode (Roadmap / NeetCode 150) [V2] | 18 desen kategorisi: two pointers, sliding window, binary search, trees, graphs, DP, heap, backtracking… | video başına ~10–20 dk; 150 problem ≈ 35 sa (yalnızca takıldığında izle) | mülakat odaklı | problem çözümü kendi başına | sürekli | https://neetcode.io/roadmap |
| MIT 6.006, *Introduction to Algorithms* [K] | karmaşıklık, hashing, grafik, DP | ~25 sa (seçici: 6 sa) | orta | problem setleri | Bahar 2020 | https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/ |

**Alan için tahmini süre:** video ~15 sa (asıl süre problem çözümüne gider).

Not: RE mülakatlarında LeetCode'un yanında "ML kodlaması" da soruluyor: attention'ı, KV cache'li decode döngüsünü ve top-k/top-p örneklemeyi sıfırdan yazmak gibi. Bunlar CS336 ödev 1 ve Karpathy dersleriyle kapsanıyor.

## 7. Bio-ML (protein LM/ESM, AlphaFold 2/3, genomik LM/Evo, tek hücre temel modelleri, protein tasarımında difüzyon)

| Kaynak | Konular | Süre | Seviye | Kod/ödev | Yıl | URL |
|---|---|---|---|---|---|---|
| MIT 6.874 / 6.802, *Deep Learning in the Life Sciences* (Kellis, Gifford) [V2] | genomikte CNN/RNN, regülasyon, tek hücre, protein, yorumlanabilirlik | ~24 ders ≈ 25 sa (seçici: 8 sa) | orta-ileri; **2020 tarihli**, LLM öncesi | ödevler (mit6874.github.io) | Bahar 2020 | https://mit6874.github.io/ |
| Kellis, *MLCB24* dersleri (MIT 6.047/6.878 devamı) [V2] | tek hücre analizi, epigenomik ve HMM, regülasyon devreleri, GWAS/PRS, karşılaştırmalı genomik | ~23 ders (seçici: 6 sa) | orta-ileri; biyoloji tarafı güçlü, model mimarisi tarafı zayıf | — | 2024 | Manolis Kellis YouTube kanalı (playlist linki video açıklamalarında) |
| Harvard CMSA, *ML for Protein Folding* (Nazim Bouatta) [V] | AlphaFold2 ve OpenFold mimarisinin matematiksel anlatımı | ~6–8 sa | ileri; AF2 için en derin ders | — | 2023 | https://cmsa.fas.harvard.edu/event/protein-folding |
| Mohammed AlQuraishi, Simons Presidential Lecture [V] | AlphaFold ne öğreniyor, nasıl öğreniyor | ~1 sa | ileri | — | 2024 | https://www.simonsfoundation.org/?p=45951 |
| John Jumper, Bloch Lecture (UChicago) ve 2024 Nobel dersi [V] | AlphaFold'un tarihçesi ve tasarım kararları | ~1 sa + ~0,5 sa | orta | — | 2024–2025 | https://news.uchicago.edu/story/nobel-laureate-john-jumper-returns-uchicago-discuss-alphafold-protein-revolution |
| Sergey Ovchinnikov, *What could AlphaFold 4 look like?* (Owl Posting podcast) [V] | AF3'ün sorunları, MSA ile tek dizi karşılaştırması, protein tasarımı | ~2 sa | ileri; mülakat tartışma soruları için ideal | — | 2025 | https://www.owlposting.com/i/161619288/timestamps |
| Princeton COS597N, *ML for Structural Biology* (Ellen Zhong) [V] | AF1/AF2, protein LM, difüzyon, cryo-EM | slayt ve okuma listesi (video doğrulanmadı) | ileri | — | Güz 2022–2023 | https://www.cs.princeton.edu/courses/archive/fall22/cos597N |
| M. Á. González Arias, *A roadmap for AI-driven protein design* [V] | ML/DL, transformer ve LM, protein yapısı/işlevi/evrimi, AlphaFold, AI ile protein tasarımı, veri ve önyargılar | 10 ders ≈ 37 sa | orta; **dil ve kalite doğrulanmadı** (muhtemelen İspanyolca) | — | Şubat 2026 | https://zenodo.org/records/18498885 · https://www.youtube.com/@miangoar_bio |
| GenBio AI, *FM4Bio Seminar Series* [V] | DNA/RNA/protein/tek hücre temel modelleri (scGPT, scPRINT, moscot, Kundaje'nin regülasyon modelleri) | konuşma başına ~1 sa (seçici: 4 sa) | ileri | — | 2025 | https://genbio.ai/fm4bio-seminar/ |
| MIT 6.S184, protein tasarımı konuk dersi [V] | flow/difüzyon modelleriyle protein üretimi | ~1 sa | ileri | — | 2025 | https://diffusion.csail.mit.edu/2025/ |

**Bu araştırmada doğrulanamayanlar.** ESM3 (Alex Rives / EvolutionaryScale) ve Evo 2 (Brian Hie / Arc Institute) için resmi konuşma videoları bulunamadı. Bunlar için birincil kaynak makaleler (ESM3 Science 2025, Evo 2 preprint 2025) ve kurumların YouTube kanalları olacak. RFdiffusion için de Baker Lab / IPD konuşmalarına bakılmalı. Bunlar bilet 03 (okuma listesi) için not edildi.

**Alan için tahmini süre:** çekirdek ~25 sa, tam liste ~60 sa. Bu alanda video yetersiz olduğu için makale okuma ve özel animasyon payı büyük.

---

## Süre özeti

| Alan | Çekirdek (sa) | Tam liste (sa) |
|---|---|---|
| Matematik | 25 | 45 |
| Klasik ML | 20 | 35 |
| Derin öğrenme | 35 | 60 |
| Transformer ve LLM | 55 | 85 |
| Sistemler ve dağıtık eğitim | 35 (yarısı metin) | 55 |
| Algoritmalar | 15 | 35 |
| Bio-ML | 25 | 60 |
| **Toplam** | **~210** (yalnızca video ~175) | **~375** |

450 saatlik programda çekirdek liste toplam sürenin ~%40–45'i eder. Geri kalan süre CS336 ödevleri, kod, soru çözümü ve okuma için kalır.

## Özel animasyon adayları (görsel anlatımın eksik ya da zayıf olduğu konular)

Seçim ölçütleri:
- (a) Mülakatta sık soruluyor.
- (b) Kavram dinamik ve süreç odaklı, yani statik diyagramla zor anlaşılıyor.
- (c) Mevcut kaynaklar ya metin/statik şekil, ya da kod okuma düzeyinde kalıyor.

3B1B attention ve MLP konularını çok iyi kapsıyor; bunlar için animasyon gerekmez.

1. **KV cache, prefill/decode ve roofline.** Decode adımında cache'in büyümesi, bellek hesabı (2 · katman · başlık · d_head · bayt · token), MQA/GQA'nın etkisi ve decode'un neden bellek-bant-genişliği sınırlı olduğu (aritmetik yoğunluk) ele alınmalı. Kaynaklar formülleri veriyor, ama zaman içinde akan bir görsel yok. *En yüksek öncelik.*
2. **PagedAttention ve continuous batching.** Blok tablosu, parçalanma ve isteklerin batch'e girip çıkması. Mevcut anlatım vLLM makalesindeki statik şekillerden ibaret.
3. **FlashAttention'da tiling ve online softmax.** Q/K/V bloklarının HBM'den SRAM'e akışı ve çalışan max/sum düzeltmesi. Umar Jamil ve GPU MODE türetimi veriyor, ama adım adım bellek hiyerarşisi animasyonu yok.
4. **Kolektif iletişim ve ZeRO/FSDP.** Ring all-reduce'un reduce-scatter + all-gather olarak ayrışması; ZeRO-1/2/3'te parametre, gradyan ve optimizer durumunun GPU'lar arasında parçalanıp yeniden toplanması. Playbook'ta etkileşimli grafikler var, ama zamanlı animasyon yok. Donanım olmadan teori öğrenildiği için bu konu özellikle değerli.
5. **Pipeline bubble'ları.** GPipe, 1F1B ve interleaved 1F1B'nin zaman çizelgeleri ve bubble oranı formülü. Tensor parallel tarafında Megatron'un sütun/satır bölmesi ve f/g operatörleri.
6. **MoE.** Router'ın top-k seçimi, kapasite faktörü ve token düşürme, load-balancing loss; expert parallel all-to-all iletişimi.
7. **Kuantizasyon.** absmax ve zero-point ölçekleme, aktivasyon outlier'ları (LLM.int8, SmoothQuant), GPTQ'nun hata telafisi, AWQ'nun önemli kanalları; INT8/FP8/FP4 grid'leri. Song Han'ın dersleri var, ama görselleştirme zayıf.
8. **RoPE ve bağlam uzatma.** 2D düzlemde dönen q/k çiftleri, frekans bantları, NTK/YaRN ölçekleme.
9. **RLHF matematiği.** PPO'da KL-cezalı ödül, GAE ve clipping; DPO'nun Bradley-Terry modelinden kapalı form türetimi (örtük ödül); GRPO'da grup bazlı baseline. Mevcut anlatımlar (Umar Jamil, CS336 ders 15–16) tahta ve slayt düzeyinde.
10. **Scaling law.** IsoFLOP eğrileri, Chinchilla'nın hesap-optimal noktası ve C ≈ 6ND ilişkisi. Ayrıca μP ile hiperparametre aktarımı.
11. **Optimizasyon dinamikleri.** Adam/AdamW'nin moment ve bias düzeltmesi, warmup ve cosine LR, karışık hassasiyette loss scaling; KL(p‖q) ile KL(q‖p) karşılaştırması (mode-covering ve mode-seeking).
12. **Speculative decoding.** Taslak model ve doğrulama, kabul/ret örneklemesi ve bunun dağılımı neden korduğu.
13. **AlphaFold2.** Evoformer'ın MSA↔pair iletişimi, triangle multiplicative update ve triangle attention, IPA'nın lokal çerçeveleri, recycling. Mevcut anlatım statik şekiller ve uzun derslerden oluşuyor.
14. **AlphaFold3.** Pairformer ve difüzyon modülü (tüm atomlar üzerinde gürültü giderme). RFdiffusion'da SE(3) çerçeve difüzyonu.
15. **ESM ile sıfır-atış varyant etkisi.** Maskeli marjinallerle log-olabilirlik oranı, attention'dan contact map çıkarımı, AlphaMissense ile ilişkisi. Mert'in araştırmasına doğrudan bağlı; mülakatta "kendi işini anlat" sorusu için güçlü bir görsel olur.
16. **Genomik LM'ler.** Evo/StripedHyena'da uzun konvolüsyon ve attention'ın karmaşıklık karşılaştırması, tek nükleotit tokenizasyonu. Tek hücre modellerinde gen-sıralama tokenizasyonu (Geneformer, scGPT).

## Kaynaklar (doğrulananlar)

- CS336 Bahar 2026 ders ve ödev listesi, playlist: https://cs336.stanford.edu/
- Karpathy Zero to Hero ders süreleri: https://karpathy.ai/zero-to-hero.html
- CS224N Kış 2026 programı ve Bahar 2024 halka açık playlist notu: https://web.stanford.edu/class/cs224n/
- GPU MODE ders listesi: https://github.com/gpu-mode/lectures
- MIT 6.S184: https://diffusion.csail.mit.edu/2025/ · https://diffusion.csail.mit.edu/2026/
- MIT 6.S191 2026: https://introtodeeplearning.com/
- MIT 6.5940: https://hanlab.mit.edu/courses/2024-fall-65940
- CS285 Güz 2023: https://rail.eecs.berkeley.edu/deeprlcourse-fa23/
- CS25 kayıtları: https://web.stanford.edu/class/cs25/recordings
- Ultra-Scale Playbook: https://huggingface.co/spaces/nanotron/ultrascale-playbook
- How to Scale Your Model: https://jax-ml.github.io/scaling-book/ · https://github.com/jax-ml/scaling-book
- Kellis'in ders sayfası: https://compbio.mit.edu/teaching.html
- MIT 18.065 OCW: https://ocw.mit.edu/courses/18-065-matrix-methods-in-data-analysis-signal-processing-and-machine-learning-spring-2018/
- Protein tasarımı yol haritası: https://zenodo.org/records/18498885
- FM4Bio: https://genbio.ai/fm4bio-seminar/
- 3B1B Neural Networks: https://www.3blue1brown.com/topics/neural-networks
