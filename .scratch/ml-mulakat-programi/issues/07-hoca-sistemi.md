# Hoca sistemi

Type: grilling
Status: resolved
Blocked by: 06
Map: ../map.md

## Question

Hoca (Claude) program içinde nasıl çalışacak? Hangi skill'ler/komutlar olacak (ders anlat, sıfırdan anlat, mock mülakat, ödev değerlendir), öğrenenin ilerlemesi ve zayıf noktaları nerede ve hangi formatta tutulacak, tekrar planlaması nasıl yapılacak, mock mülakat protokolü nasıl işleyecek?

Örnek ünite formatı kararından gelenler: üretilmiş videonun öğrenen istediğinde nasıl üretileceği (tetik, süre, maliyet), soruların takip zincirinin nasıl açılıp puanlanacağı, hata kaydının nereye ve hangi biçimde yazılıp tekrar planına nasıl gireceği, çizim fotoğrafı ve sözlü prova için geri bildirim protokolü.

## Answer

**Yer**: Hoca, program repo'sunda Claude Code skill'leri ve slash komutları olarak yaşar. Dosyaları okur, testleri koşturur, ilerleme dosyalarını yazar.

**Komutlar** (yalnızca bu 7 komut var):
- `/gun`: günün planı. Önce tekrar bloğu, sonra üniteler.
- `/unite`: ünitenin 9 adımlık döngüsünü yürütür.
- `/sifirdan <kavram>`: konuyu ön bilgi varsaymadan anlatır.
- `/soru`: bankadan soru getirir, takip zincirini açar.
- `/degerlendir`: pratik görevi ya da haftalık ödevi puanlar (test sonucu + kod incelemesi).
- `/video <kavram>`: üretilmiş video ister.
- `/mock <tur>`: mock mülakat yapar.

Ara sınav ve final `/mock` üzerine kurulur.

**Ünite içeriği önceden üretilir**: Açıklama, pratik görev, testler, referans çözüm ve soru referansları içerik üretiminde önceden yazılır ve doğrulanır. `/unite` bu dosyaları yürütür ve hata kaydına göre kişiselleştirir. Anında üretim yalnızca `/sifirdan` ve `/video` için yapılır.

**Durum dosyaları**:
- Okunabilir kayıtlar markdown'da tutulur. Ünite başına bir ilerleme satırı vardır. Hata kaydının sütunları: `tarih | ünite | alan/alt konu | tek satır | durum`.
- Tekrar zamanlaması makinenin okuduğu tek bir YAML/JSON dosyasında tutulur. Bu dosya kartlara id ile başvurur.
- Dosyaların yerleşimi repo yapısı kararına kalır.

**Takip zinciri protokolü**:
- Hoca halkaları sırayla açar ve her halkayı 0–2 puanlar: 0 bilmiyor, 1 kısmi, 2 mülakatta geçer.
- Bir halkada 0 alınırsa zincir durur. Hoca model cevabın o kısmını açar ve halka hata kaydına düşer.
- Sorunun puanı ulaşılan en derin halkadır (ör. "L2'de kırıldı").

**Sözlü prova**:
- Omarchy'nin yerel dikte aracıyla (`voxtype`) doğrudan Claude Code istemine konuşulur.
- Hoca içeriği ve yapıyı değerlendirir, dile geri bildirim vermez.
- 2 dakikalık süre zaman damgalarından yaklaşık olarak ölçülür.

**Çizim**: Fotoğraf Hoca'ya verilir, Hoca öz değerlendirme listesine göre geri bildirim yazar.

**Üretilmiş video**:
- `/video` ile istenir. Hoca önce o noktayı karşılayan bir seçilmiş video olup olmadığına bakar; varsa onu önerir.
- Video arka planda üretilir (~1–2 saat). Ünite beklemez, video sonraki tekrar oturumunda izlenir.
- Üst sınır haftada en fazla 2 videodur. Gerçek kullanım farklı çıkarsa sınır değiştirilir.

**Tekrar**:
- Leitner kutuları kullanılır, aralıklar 1 → 3 → 7 → 14 → 30 gündür. Hedef halkaya ulaşan kart bir kutu ilerler. Kırılan kart 1. kutuya döner.
- İki kart türü vardır:
  - (1) Üzerinde çalışılmış her banka sorusu.
  - (2) **Hata kartı**: hata kaydındaki bir satır. Satır bir banka sorusuna bağlanabiliyorsa o soruya bağlanır. Bağlanamıyorsa Hoca satırdan tek bir mini soru üretir.
- Soğuk denemeler ve çizim alıştırmaları tekrara girmez. Whiteboard formatındaki sorular tekrarda da çizilerek cevaplanır.

**Tekrar bloğu**: Günde ~30 dakika sabit. Gün bu blokla başlar ve süre 5 saatin içinden çıkar (2 ünite ≈ 4–4,5 sa + 30 dk tekrar).

**Mock mülakat protokolü**:
- Hoca mülakatçı moduna geçer. Açıklama yapmaz, ipucunu yalnızca gerçek bir mülakatçı kadar verir.
- Süre turun gerçek süresidir (45–60 dk).
- Sorular zayıf alanlara ve hata kaydına ağırlık verilerek seçilir. Henüz çalışılmamış alt konulardan soru gelmez.
- Coding turlarında kod bir dosyaya yazılır, testler sonradan koşturulur.
- Cevaplar dikte edilir.
- Sonunda rubrik değerlendirme gelir: sinyal başına güçlü/zayıf ve strong hire … no hire kararı. Ardından öğretmen moduna dönülür ve kırılan her nokta hata kaydına yazılır.
- Sınavların tur sayısı ve sıralaması **Sınav ve ödev formatı** biletine kalır.
