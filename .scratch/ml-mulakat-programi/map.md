# Harita: ML/AI Mülakat Programı

Label: wayfinder:map

## Destination

**Program spec'i**: 3 aylık (~450 saat), lisans bölümü gibi kurgulanmış bir programın tüm kararları verilmiş olur: kategorize edilmiş zor soru bankasının yapısı ve kaynakları, ders listesi ve dönemlere dağılımı, ünite formatı (seçilmiş/üretilmiş video, sıfırdan kod, debug, zor sorular, çizerek anlatma), video üretim hattı ve Hoca sisteminin işleyişi. Spec, içerik üretimine devredilecek kadar net olur.

## Notes

- **Öğrenen**: Mert (tek kullanıcı). **Hedef rol**: frontier lab Research Engineer + biyoinformatik (bio-ML lab mülakatları dahil). Terimler: `GLOSSARY.md`.
- **Başlangıç seviyesi**: orta-ileri. Seviye tespit sınavı yok; eksik temeller Hoca'dan "sıfırdan anlat" istenerek kapatılır.
- **Bütçe**: 450 saat = 3 dönem × 4 hafta × 7 gün × 5 sa (420) + Final haftası (30). Paralel dersler, haftalık ödev, ara sınav, final mock mülakat.
- **Kapsam**: klasik ML, derin öğrenme, transformer/LLM, ML sistem tasarımı ve dağıtık eğitim, matematik, algoritma/LeetCode, bio-ML (~%15).
- **Kod perspektifi**: sıfırdan implementasyon ve debug görevleri, pytest testleriyle. Implement görevleri JAX öncelikli (isteğe bağlı NumPy karşılığı); debug görevleri JAX/PyTorch karışık; CS336 ödevleri PyTorch.
- **Görsel perspektif**: seçilmiş dış videolar (omurga) + Manim tarzı üretilmiş videolar (yalnızca öğrenen istediğinde) + notebook içi grafikler + "çizerek anlat" alıştırmaları.
- **Formül yazımı**: LaTeX yok; düz metin/Unicode veya kod biçimi, uzun türetimler kâğıtta + fotoğraf.
- **Dil**: sorular ve terimler İngilizce, açıklamalar Türkçe, cevap provaları İngilizce.
- **Dağıtık eğitim**: sadece teorik anlatılır; rig/TRUBA üzerinde koşturma yok. Rig'in tek 3090'ı yalnızca tek-GPU ödevleri (kernel, profiling) için kullanılır.
- Her oturum `grilling` + `domain-modeling` skill'lerini kullanır; araştırma biletleri `research` skill'iyle çözülür, bulgular `.scratch/ml-mulakat-programi/research/` altına yazılır.

## Decisions so far

<!-- kapanan bilet başına bir satır -->

- [Seçilmiş video ve ders kaynakları envanteri](issues/02-video-ve-ders-kaynaklari.md): omurga CS336 (LLM/sistemler) + Karpathy Zero to Hero + 3B1B + CME295; dağıtık eğitim için en iyisi metin (HF Ultra-Scale Playbook, How to Scale Your Model); bio-ML videoları zayıf; çekirdek liste ~210 sa; 16 üretilmiş video adayı (KV cache, FlashAttention, FSDP, RoPE, AF2/AF3...).
- [Manim ile video üretim hattı](issues/03-manim-video-uretim-hatti.md): Manim Community (sürüm sabitlenmiş, CPU/Cairo); ajan tek seferde zayıf, render→kare incele→düzelt döngüsüyle ~%90+; seslendirme altyazı ya da Türkçe TTS (Azure/Gemini/ElevenLabs veya yerel); video ~2–4 sa (şablonlarla 1–2 sa); önce tek prototip video (KV cache) önerisi.
- [Zor mülakat sorusu kaynakları envanteri](issues/01-soru-kaynaklari-envanteri.md): RE seviyesinde hazır zor soru bankası yok; zorluk implementasyon setlerinden (TorchLeet, Deep-ML, Sasha Rush puzzles, CS336 ödevleri) ve derin kitaplardan (Huyen, Kashani, UDL) geliyor; bio-ML ve "debug this training loop" için kaynak yok; çoğu repo lisanssız → kendi cümlelerimizle yeniden yazılmalı; 12 kaynaklık kısa liste.
- [Soru kategori şeması](issues/04-soru-kategori-semasi.md): üç ana eksen Tur (6) × Alan (8) × Format (8) + sabit tur–format geçerlilik matrisi; alan başına kontrollü alt konu listesi; kendi L1–L3 zorluk ölçeğimiz; serbest anahtar kelime + 0–2 ilgili alan; behavioral ve şirket etiketi yok.
- [Ders listesi ve dönemlere dağılım](issues/05-ders-listesi-ve-donemler.md): 8 ders (Algorithms I/II/III her dönemde); D1 Foundations+DL+LLMs I, D2 LLMs II+ML Systems, D3 System Design+Bio-ML; 385 sa ders + 65 sa rezerv; ön koşul zinciri, ders–alan eşlemesi, video tavanı %35, CS336 ödev yerleşimi (rig tek GPU).
- [Örnek ünite formatı](issues/06-ornek-unite-formati.md): ünite 2–3 sa (günde ~2); sabit küçük döngü: soğuk deneme → seçilmiş video → TR açıklama → tek pratik görev (Implement/Debug dönüşümlü) → 2–3 zor soru → (istenirse) üretilmiş video → çizim → İngilizce prova → hata kaydı; oranlar konu düzeyinde; JAX öncelikli; LaTeX'siz formül kuralı.
- [Hoca sistemi](issues/07-hoca-sistemi.md): Claude Code skill'leri, 7 komut (/gun /unite /sifirdan /soru /degerlendir /video /mock); üniteler önceden üretilip doğrulanır, Hoca yürütür; kayıtlar markdown + tekrar için tek YAML; takip zinciri 0–2 puan, 0'da durur; Leitner tekrarı (banka sorusu + hata kartı), günde 30 dk; prova voxtype dikte; video haftada ≤2, arka planda; mock protokolü mülakatçı modu + rubrik.
- [Soru bankası fiziksel formatı](issues/08-soru-bankasi-fiziksel-formati.md): soru başına markdown (frontmatter + sabit başlıklar), kodlu sorular klasör (gorev/test/cozum); `banka/<alan>/`, değişmez id `tll-0042`; köken, kaynaklar, hedef_halka, sure_dk, cerceve, durum alanları; halka halka model cevap; schema.yaml + pytest doğrulayıcı (testler çözümde geçer, görevde kalır); bankada durum yok, mini sorular bankaya girmez; pratik görevler de banka sorusu.
- [Günlük ve haftalık çalışma şablonu](issues/09-gunluk-ve-haftalik-calisma-sablonu.md): 13 hafta (3×4 + Final haftası 30 sa); ünite günü = 30 dk tekrar + 30 dk algoritma bloğu + 2 harmanlanmış ünite; 7. gün hafif gün (ödev ~3 sa + hafta kapanışı, D1/D2 4. hafta ara sınav); tekrar ders saatinden sayılır; yuvalar ders saatiyle orantılı; D3'ün ~20 sa fazlası program geneli kayma tamponu; önceden yazılmış dönem planı + kayma kuralı.
- [Sınav ve ödev formatı](issues/10-sinav-ve-odev-formati.md): ödev = ~2 sa birleşik kod görevi (CS336 haftalarında CS336 dilimi) + ~1 sa 3–4 zincirli soru; `/degerlendir` 4 kriter × 0–2, test tavanı, toplam not yok; ara sınav 3 tur × 45 dk + 15 dk rubrik (D1/D2'ye özgü turlar); Final haftası 5 loop günü + tampon, 14 tur (1 Behavioral); bankada `havuz: sinav` ayrılmış sorular; kırılanlar hata kaydına, sınav raporu sonraki dönemi yönlendirir.
- [Proje repo yapısı](issues/11-proje-repo-yapisi.md): ayrı repo (`ml-program`); içerik (banka, dersler, plan, ödev/sınav, videolar) / `kayit/` (yalnızca Hoca yazar) / `calisma/` (commit'lenir) ayrımı; komut başına skill + ortak protokol klasörü; ünite id `llm1-04`; seçilmiş video kataloğu `secilmis.yaml`; Manim kaynağı commit, render gitignore; günde bir otomatik commit; tek uv ortamı + `video`/`gpu` group'ları.
- [İçerik üretim sırası ve devri](issues/12-icerik-uretim-sirasi-ve-devri.md): dilim = hafta, artı dönem başı paketi (plan + CS336 dilimleme + gizli sınav havuzu); ünite soruları dilimle, havuz pakette; 6 adımlı kalite kapısı (5 otomatik + doğrulayıcı ajan), öğrenen önceden onaylamaz; hafta kapanışında tetiklenen ayrı Üretici skill'i, 1 hafta tampon, tempo gerçek ilerlemeye bağlı; plan sabit, vurgu hata kaydına göre; sıfırıncı dilim + D1 1. hafta pilotu, tek şablon revizyonu.
- [Kaynağı olmayan alanlarda soru türetme yöntemi](issues/13-kaynagi-olmayan-alanlarda-soru-turetme.md): her türetilmiş soru alan başına sabit kaynak listesinden bir çapaya dayanır; Debug = doğrulanmış Implement çözümüne id'li hata kataloğundan 2–4 hata (en az biri sessiz), taban yoksa önce Implement üretilir; L3 = Methods/Supplement ayrıntısı ya da gerekçeli trade-off; doğrulayıcı kör ikinci türetim + çapa kontrolü; `original` yalnızca L1–L2; `kaynak_listesi.yaml` ve `hata_katalogu.yaml` sıfırıncı dilimde.
- [Algorithms dersleri ile ML Coding turunun ilişkisi](issues/14-algorithms-ve-ml-coding-iliskisi.md): iki hat ayrı; etiket "değerlendirilen beceri" testiyle (ML bilgisi gerekmiyorsa Practical Coding × Algorithms = kılıklı problem); algoritma bloğunda haftada ~1 kılıklı problem, 30 dk sınırı; kavramın iki yüzü iki ayrı soru; Final Gün 4'te biyo kılıklı Practical Coding (D3'te ≥2 `havuz: sinav`).
- [Bio-ML'de öğrenenin kendi projelerinin kullanımı](issues/15-bio-ml-ogrenen-projeleri.md): 3 proje (KIF13A atlası, AcRLSD, pdnph-bench) → Bio-ML'e 4 proje ünitesi (~10 sa, Bio-ML ~%15); matris içinde Research Discussion/ML Debugging/ML Depth; `proje:` alanı; çapalar D3 paketinde `banka/proje_kaynaklari/`'na dondurulmuş kopyalar, `derived`; "neden" halkaları rubrikle; pdnph metodoloji üzerine (gerçek sonuç yok); hata kataloğuna 6 gerçek olay; Final Gün 4 Research Discussion = proje derin dalışı.

## Not yet specified

<!-- boş: tüm biletler kapandı; spec içerik üretimine devredilmeye hazır -->

## Out of scope

- Başarı ölçümü / "vardım mı" kriteri: program öğretmeye odaklanır (sınavlar sadece öğretme aracı).
- Seviye tespit sınavı: başlangıç orta-ileri varsayılır.
- Ayrı interaktif web demoları (tarayıcıda oynanabilen HTML/JS görseller).
- Dağıtık eğitimi gerçek donanımda (rig 2×3090, TRUBA) koşturmak.
- İçerik üretiminin kendisi: spec bitince ayrı bir işe devredilir.
