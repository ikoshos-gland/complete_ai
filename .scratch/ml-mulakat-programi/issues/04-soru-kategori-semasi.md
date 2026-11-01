# Soru kategori şeması

Type: grilling
Status: resolved
Blocked by: 01
Map: ../map.md

## Question

Zor mülakat soruları hangi taksonomiyle kategorize edilecek? Eksenler (alan, alt konu, soru tipi: teori / sıfırdan kod / debug / sistem tasarımı / çizerek anlat, zorluk) ve her eksenin değerleri neler?

## Answer

Her soru üç ana eksende tam olarak bir değer alır: **Tur × Alan × Format**. Bunlara alt konu, zorluk, anahtar kelime ve ilgili alan eklenir.

**Tur** (6): Practical Coding · ML Coding · ML Debugging · ML Depth · System Design · Research Discussion. Behavioral bankaya girmez, mock mülakata kalır.

**Alan** (8): Math · Classical ML · DL Foundations · Transformers & LLMs · ML Systems & Distributed Training · ML System Design · Algorithms · Bio-ML. Alanlar derslerden bağımsızdır; ders–alan eşlemesi **Ders listesi ve dönemlere dağılım** biletinde yapılır.

**Format** (8): Conceptual · Derivation · Implement · Debug · Estimation · Design · Whiteboard · Paper Discussion.

**Geçerlilik matrisi** (sabit kural; matrise uymayan soru yanlış etiketlenmiştir):

| Tur | Geçerli formatlar |
|---|---|
| Practical Coding | Implement |
| ML Coding | Implement, Derivation |
| ML Debugging | Debug |
| ML Depth | Conceptual, Derivation, Estimation, Whiteboard |
| System Design | Design, Estimation, Whiteboard |
| Research Discussion | Paper Discussion, Conceptual, Design |

Ek kural: Algorithms alanı yalnızca Practical Coding turunda yer alır.

**Alt konu**: Her alanın altında kontrollü bir liste var. Yeni alt konu yalnızca bilinçli bir kararla eklenir.
- Math: Linear Algebra · Probability · Statistics & Estimation · Optimization · Information Theory · Calculus & Autodiff Math
- Classical ML: Linear/Logistic Models · Trees & Ensembles · Kernels & SVM · Clustering & Dim. Reduction · Bias–Variance & Generalization · Evaluation & Metrics
- DL Foundations: Backprop & Autograd · Optimizers & LR Schedules · Initialization & Normalization · Regularization · CNN · RNN/Sequence Models · Training Dynamics & Stability
- Transformers & LLMs: Attention & Architecture · Positional Encoding · Tokenization · Pretraining & Data · Scaling Laws · Post-training (SFT/RLHF/DPO/GRPO) · Evaluation · Inference & Decoding
- ML Systems & Distributed Training: GPU & Memory Hierarchy · Kernels · Mixed Precision & Quantization · Data/Tensor/Pipeline Parallelism · FSDP/ZeRO · Profiling & Throughput Math
- ML System Design: Training Infrastructure · Serving & Latency · Data Pipelines · Experimentation & Evaluation Infra · Recommendation/Ranking-style Product Design
- Algorithms: Arrays & Hashing · Two Pointers & Sliding Window · Trees & Graphs · DP · Heaps & Greedy · Binary Search
- Bio-ML: Protein Structure (AF2/AF3) · Protein/DNA Language Models · Variant Effect Prediction · Single-cell & Omics · Bioimage Segmentation · Biological Data Pitfalls

**Zorluk**: Kendi 3 seviyeli ölçeğimiz kullanılır: L1 Warm-up, L2 Standard, L3 Frontier. Banka ağırlıklı olarak L2–L3'ten oluşur. Kaynağın kendi zorluk etiketi yalnızca bilgi olarak saklanır.

**Etiketler**:
- Serbest **anahtar kelime** (ör. RoPE, GRPO); arama bu alanla yapılır.
- İsteğe bağlı **ilgili alan** (0–2 alan); alan sayımlarına girmez.
- Şirket etiketi yoktur.

**Bu biletin dışında kalanlar**: kaynak alanı, model cevap ve tekrar alanları **Soru bankası fiziksel formatı** biletine aittir.
