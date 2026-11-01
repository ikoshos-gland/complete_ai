# Zor mülakat sorusu kaynakları envanteri

Type: research
Status: resolved
Blocked by: —
Map: ../map.md

## Question

Frontier lab Research Engineer ve bio-ML lab (Isomorphic, EvolutionaryScale, Arc Institute, Genentech/Prescient vb.) seviyesindeki **zor** AI/ML/LLM mülakat soruları hangi kaynaklarda bulunuyor? Kapsam: klasik ML, derin öğrenme, transformer/LLM, ML sistem tasarımı/dağıtık eğitim, matematik, ML'e özgü kodlama, LeetCode tarzı algoritma, bio-ML. Her kaynak için: ne içerdiği, yaklaşık soru sayısı, zorluk seviyesi, güncellik, lisans, hangi kategorileri kapsadığı ve güvenilirlik. Bulgular kategori şemasını ve soru bankasının kaynaklarını besler.

## Answer

- Frontier-lab RE seviyesinde hazır, "zor" bir soru bankası yok. İngilizce LLM soru repoları çoğunlukla AI-Engineer/RAG seviyesinde, FAANG-MLE repoları da orta zorlukta.
- En güçlü zor kaynaklar implement-from-scratch/bulmaca setleri: TorchLeet (68 problem, MIT; DPO/PPO/GRPO, KV cache, FlashAttention, FSDP), Deep-ML (~164 açık problem), srush puzzles (MIT), Stanford CS336 ödevleri (2026).
- Kavramsal omurga: Chip Huyen MLI Book (200+ soru, zorluk etiketli, lisanssız), Kashani DL Interviews (yüzlerce çözümlü), UDL alıştırmaları (CC BY-NC-ND). Dağıtık eğitim teorisi için: *How To Scale Your Model* (DeepMind), stas00/ml-engineering, Ultra-Scale Playbook.
- Aday raporları (Glassdoor, 1point3acres, PracHub, Exponent) yalnızca format sinyali veriyor: pratik kodlama, ML kodlama, **ML/transformer debug**, araştırma tartışması, değerler/güvenlik. Güvenilirlikleri düşük, yeniden kullanıma da kapalılar.
- Boşluklar: bio-ML (soru kaynağı neredeyse yok), "training loop'u debug et" (açık set yok), LLM ön-eğitim/ölçekleme/RLHF teorisinde derin kavramsal sorular, dağıtık eğitim soruları. Bunların hepsi türetilmeli.
- Lisans: popüler repoların çoğunda lisans yok. Kişisel bankada soruları yeniden yazmak uygun, birebir kopyalayıp paylaşmak uygun değil.
- 12 kaynaklık kısa liste ve kategori ekseni gözlemleri (round × alan/yaşam döngüsü × format × zorluk) raporda.

Ayrıntılar: [../research/01-soru-kaynaklari-envanteri.md](../research/01-soru-kaynaklari-envanteri.md)
