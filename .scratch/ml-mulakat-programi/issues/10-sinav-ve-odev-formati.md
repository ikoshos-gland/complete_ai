# Sınav ve ödev formatı

Type: grilling
Status: resolved
Blocked by: 09
Map: ../map.md

## Question

Haftalık ödev, ara sınav ve final mock mülakat haftası nasıl kurgulanır? Ödevin içeriği ve puanlaması (`/degerlendir` ne ölçer) ne olacak? Ara sınavlar her dönem sonunda mı yapılır, hangi turlardan oluşur, kaç saat sürer? Final haftası (13. hafta, 6 gün × 5 sa = 30 sa; ~20 sa mock + ~10 sa tampon) kaç `/mock` turu içerir ve turlar hangi sırayla gelir? Haftalık ödev ~3 sa, ara sınav ~3 sa; ikisi de hafif günde (7. gün) yapılır, ara sınav yalnızca D1 ve D2 sonunda (**Günlük ve haftalık çalışma şablonu** kararı). Sınav sonuçları hata kaydına ve tekrar planına nasıl döner? Tek bir mock turunun protokolü **Hoca sistemi** kararında sabitlendi; bu bilet onların birleşimini belirler.

## Answer

**Haftalık ödev** (~3 sa, hafif gün):
- **Kod kısmı (~2 sa)**: Haftanın birkaç konusunu birbirine bağlayan tek bir **birleşik görev**, pytest ile test edilir (ör. tokenizer + attention + eğitim döngüsü → küçük LM). Konusu haftadan haftaya haftanın iki ana dersi arasında dönüşümlü seçilir.
- **Soru kısmı (~1 sa)**: İki dersten 3–4 banka sorusu, takip zinciriyle cevaplanır.
- **CS336 ödevleri**: CS336 ödevi bulunan haftalarda ödevin kod kısmı CS336 ödevinin sıradaki dilimidir. Kalanı ünitelerin pratik görevlerine dağılır. Dilimleme içerik üretimine bırakılır. Diğer haftalarda kod kısmı kendi ürettiğimiz birleşik görevdir.

**`/degerlendir` puanlaması**:
- Önce testler koşturulur. Geçmeyen test varsa doğruluk en fazla 1 olabilir.
- Kod incelemesi dört kriteri 0–2 puanlar: **doğruluk**, **sayısal kararlılık / kenar durumlar**, **verim** (vektörleştirme, gereksiz kopya), **okunabilirlik**.
- Soru kısmı takip zinciri kuralıyla puanlanır: sorunun sonucu ulaşılan en derin halkadır.
- Toplam not üretilmez (başarı ölçümü kapsam dışı). Çıktı, kriter başına puan ve hata kaydına düşen satırlardır.

**Ara sınav** (~3 sa, D1 ve D2'nin 4. haftasındaki hafif gün): 3 mock turu × ~45 dk. Her turun ardından ~15 dk rubrik ve öğretmen modu gelir.
- **D1**: Practical Coding (Algorithms I) · ML Coding (Foundations/DL/LLMs I) · ML Depth (Math, Classical ML, DL, LLM mimarisi).
- **D2**: ML Debugging (LLMs II / Systems) · ML Depth (post-training, inference, throughput/bellek hesabıyla Estimation) · Practical Coding (Algorithms II).
- System Design ve Research Discussion ara sınava girmez, çünkü ilgili dersler D3'te. Bu turlar Final haftasında gelir.

**Final haftası** (6 gün × 5 sa): Her gün gerçek bir onsite loop'u gibi kurulur. Bir tur ~1 sa mock ve ~20–30 dk rubrik/öğretmen modundan oluşur. Tekrar bloğu (30 dk) her gün devam eder.

| Gün | Loop | Turlar |
|---|---|---|
| 1 | Temeller | Practical Coding · ML Coding · ML Depth |
| 2 | LLM | ML Debugging · ML Depth (LLM) · Research Discussion (LLM makalesi) |
| 3 | Sistemler | System Design · ML Depth (Systems/Estimation) · ML Coding |
| 4 | Bio-ML lab | Research Discussion (bio makalesi) · ML Depth (Bio-ML) · Practical Coding |
| 5 | Zayıf noktalar | Hoca'nın seçtiği en zayıf 2 tur + 1 Behavioral tur |
| 6 | Tampon | Gün 1–5'te kırılan noktaların hedefli tekrarı |

Toplam 14 tur, ~20 sa. Behavioral tur bankada yer almaz, yalnızca mock'ta yapılır.

**Sınav havuzu**:
- Bankada her alt konu için birkaç soru sınava ayrılır. Bunlar soru dosyasında sabit bir alanla işaretlenir (ör. `havuz: sinav`).
- Hoca bu soruları ünitede, tekrarda ve `/soru`'da kullanmaz; yalnızca ara sınav ve Final haftası kullanır. Böylece mock'ta öğrenen soruyu ilk kez görür.
- Bu bir durum değil, statik bir özelliktir. Bu yüzden "bankada durum yok" kuralıyla çelişmez.
- Hedef: alt konu başına L2–L3'ten en az 2 sınav sorusu.

**Sonuçların geri dönüşü**:
- Ödevde ve sınavda kırılan her nokta hata kaydına normal bir satır olarak yazılır. Ünite sütununa `ödev`, `ara sınav` ya da `final` yazılır.
- Sınavda kullanılan sorular sınavdan sonra normal tekrar kartı olur. Kırılan soru 1. kutudan, geçen soru 2. kutudan başlar.
- Ara sınavın tur başına rubrik özeti bir **sınav raporu** dosyasına yazılır. Hoca bu raporu sonraki dönemde iki yerde kullanır: D3 kayma tamponunu dağıtırken ve mock soru seçiminde zayıf alanlara ağırlık verirken.
- Ödevler için ayrı rapor tutulmaz; hata kaydı ve hafta kapanışı yeterlidir.

**Başka biletlere düşenler**: sınav raporunun ve ödev dosyalarının yeri → **Proje repo yapısı**. Sınav havuzu sorularının ve birleşik görevlerin üretimi → **İçerik üretim sırası ve devri**.
