# Seçilmiş video ve ders kaynakları envanteri

Type: research
Status: resolved
Blocked by: —
Map: ../map.md

## Question

Kapsamdaki her alan (matematik, klasik ML, derin öğrenme, transformer/LLM, ML sistemleri/dağıtık eğitim, algoritmalar, bio-ML) için en iyi **dış video ve ders kaynakları** neler (ör. 3Blue1Brown, Karpathy Zero to Hero, Stanford CS229/CS224N/CS336, Umar Jamil, MIT, bio-ML dersleri)? Her kaynak için: kapsadığı konular, süre, seviye (orta-ileri öğrenene uygun mu), kod içeriği, güncellik. Hangi önemli kavramlarda iyi görsel anlatım **eksik** (üretilmiş video adayı)?

## Answer

- **LLM ve sistemler omurgası:** Stanford CS336 (Bahar 2026). 19 ders (~25 sa) ve 5 ağır ödev: tokenizer, Triton FlashAttention2, DDP, scaling law, veri, SFT/RL. RE mülakat müfredatıyla neredeyse birebir örtüşüyor.
- **Derin öğrenme ve görsel sezgi:** Karpathy Zero to Hero (8 ders, 14,5 sa, baştan sona kod) ve 3Blue1Brown NN bölüm 1–7. Daha kısa ve modern bir LLM turu için Stanford CME295 (Güz 2025, ~18 sa). Kod ve türetim için Umar Jamil kanalı.
- **Dağıtık eğitim (yalnızca teori):** En iyi kaynaklar metin: HF Ultra-Scale Playbook (2025) ve DeepMind "How to Scale Your Model" (2025). Video tarafını CS336 paralellik dersleri, GPU MODE (~60 ders) ve MIT 6.5940 (Song Han; kuantizasyon ve dağıtık eğitim) tamamlıyor.
- **Matematik ve klasik ML:** Kaynaklar eski ama hâlâ en iyileri: MIT 18.065 ve 18.S096, MacKay, CS229 (2018), Cornell CS4780. Seçici izlenmeli. Difüzyon için MIT 6.S184 (2025/2026).
- **Bio-ML:** Video tarafı zayıf. MIT 6.874 2020 tarihli ve eski; Kellis MLCB24 biyoloji ağırlıklı. AF2 için Bouatta (Harvard CMSA), AlQuraishi, Jumper ve Ovchinnikov konuşmaları, tek hücre için FM4Bio seminerleri var. ESM3 ve Evo 2 için resmi video bulunamadı; bu konular makale okumayla karşılanacak.
- **Süre:** Çekirdek liste ~210 sa (bunun ~175 saati video), tam liste ~375 sa. 450 saatlik programda kalan süre ödev, kod ve soru çözümüne ayrılmalı.
- **Özel animasyon için öncelikli konular:** KV cache ve prefill/decode roofline, PagedAttention, FlashAttention tiling, ring all-reduce ve ZeRO/FSDP, pipeline bubble, MoE ve all-to-all, kuantizasyon outlier'ları, RoPE, PPO/DPO/GRPO, AF2 Evoformer/IPA, AF3 difüzyonu, ESM ile sıfır-atış varyant skoru.

Detaylar: [../research/02-video-ve-ders-kaynaklari.md](../research/02-video-ve-ders-kaynaklari.md)
