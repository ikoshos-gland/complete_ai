# İçerik üretim sırası ve devri

Type: grilling
Status: resolved
Blocked by: 09
Map: ../map.md

## Question

Spec bitince içerik üretimi (üniteler, banka soruları, ödevler, sınavlar) tek seferde mi yapılır, parça parça mı? Öğrenenin önerisi: parça parça. Bu bilet üretimin kendisini değil, devrin nasıl dilimleneceğini belirler:

- Dilimin birimi ne: hafta, ders, dönem?
- Üretim öğrenenin kaç hafta önünden gider (ör. hep 1–2 hafta önde)?
- İlk dilim pilot olur mu (ör. D1'in 1. haftası)? Pilottan sonra ünite formatı ve şablonlar nasıl güncellenir?
- Hata kaydı ve tekrar verisi sonraki dilimlerin içeriğini nasıl etkiler (zayıf konulara daha çok soru vb.)?
- Banka soruları ünitelerle birlikte mi üretilir, yoksa önce alan alan topluca mı?
- Her dilim hangi kontrollerden geçmeden öğrenene açılmaz (`dogrula.py`, testlerin çözümde geçmesi, kaynak kontrolü)?
- Kayma olursa (öğrenen hızlanır veya geride kalır) üretim temposu nasıl ayarlanır?

Not (**Sınav ve ödev formatı** kararı): Üretilecekler arasında birleşik ödev görevleri, CS336 ödevlerinin haftalık dilimleri ve sınav havuzu soruları da var (alt konu başına L2–L3'ten en az 2). Sınav havuzunun ara sınavdan önce hazır olması gerekir.

Not (**Proje repo yapısı** kararı): Üretim ayrı `ml-program` reposunda yapılır. Her dilim yalnızca içerik dizinlerine yazar (`banka/`, `dersler/`, `plan/`, `odevler/`, `sinavlar/`, `videolar/`). İlk dilimden önce repo iskeleti, uv ortamı ve Hoca skill'leri kurulmuş olmalı mı, yoksa bunlar pilot dilimin parçası mı?

## Answer

**Birimler**:
- **Dilim**: bir hafta. O haftanın 12 ünitesi, 7 algoritma problemi, haftalık ödevi (ya da ara sınavı) ve bunların istediği banka soruları.
- **Dönem paketi**: dönem başlamadan önce bir kerede üretilir. İçinde dönem planı, o dönemin CS336 ödev dilimlemesi ve sınav havuzu var. D3 paketi Final haftasının 14 turunun havuzunu da içerir.

**Banka soruları ne zaman üretilir**:
- Ünite soruları ve pratik görevler dilimle birlikte üretilir, yalnızca o haftanın ünitelerinin istediği kadar. Alan alan toplu üretim yapılmaz.
- Sınav havuzu dönem paketinde toplu üretilir: o dönemin her alt konusu için L2–L3'ten en az 2 soru.

**Öğrenen içeriği önceden görmez**: Ne ünite içeriğini ne de havuzu öğrenen onaylar. Havuz soruları gizli kalır; `dogrula.py` çıktısında havuz için yalnızca sayılar görünür.

**Kalite kapısı** (geçmeyen dilim öğrenene açılmaz):
1. `dogrula.py`: şema, geçerlilik matrisi, kontrollü alt konu listesi, id'ler değişmemiş.
2. Kodlu sorularda testler `cozum/`'de geçer, `gorev.py`'de kalır.
3. Dönem planındaki her id gerçekten var. Seçilmiş video bağlantıları açılıyor (HTTP kontrolü).
4. LaTeX yok (`$`, `\frac` taraması).
5. Köken ve kaynak alanları dolu. Yeniden yazılan sorular orijinalin birebir kopyası değil.
6. Taze bağlamlı ayrı bir doğrulayıcı ajan her model cevabı ve takip zincirini teknik doğruluk açısından okur.

1–5 otomatiktir, 6 ajan işidir. Hata bulunursa öğe üreticiye döner ve en fazla 2 düzeltme turu yapılır. Hâlâ geçemeyen ünite ya da soru dilimden çıkarılır. Çıkan ünitenin yerine dönem planında aynı dersin bir sonraki ünitesi öne alınır. Çıkarılan öğe hafta kapanışında öğrenene tek satırla bildirilir ve sonraki dilimde yeniden denenir. Havuz sorusu geçemezse yalnızca sayı bildirilir.

**Hata kaydının etkisi**: Dönem planındaki ünite listesi sabit kalır; ünite eklenmez ya da çıkarılmaz. Değişen yalnızca vurgudur:
- Haftalık ödevin soru kısmı ve birleşik görevin vurgusu, son haftanın hata kaydındaki zayıf alt konulara kayar.
- Zayıf alt konu sıradaki dilimin bir ünitesine denk geliyorsa o ünitenin Türkçe açıklaması ve soru seçimi oraya ağırlık verir.

**Üretici ve tetikleme**:
- Üretim, program repo'sunda Hoca'dan ayrı bir **üretim skill'idir** (Üretici). Hoca'nın 7 komutuna eklenmez.
- Öğrenen hafta kapanışında tek bir komutla tetikler. Üretim arka planda çalışır ve öğrenenin 5 saatinden yemez.
- Üretici şunları okur: dönem planı, ilerleme dosyası, hata kaydı, sınav raporu.
- Sözlükteki Hoca tanımı buna göre düzeltildi: Hoca dilim üretmez. Anında ürettiği tek şeyler `/sifirdan`, `/video` ve hata kartlarının mini sorusu.

**Tempo**:
- **1 hafta tampon**: Öğrenenin bulunduğu haftadan sonraki hafta her zaman hazırdır. Hafta N'nin kapanışında N+2 üretilir. Dönem paketi, önceki dönemin son haftasının kapanışında ya da daha önce hazır olur.
- Tempo takvime değil, ilerleme dosyasındaki gerçek konuma bağlıdır:
  - Geride kalınırsa üretim bekler, ileri üretilmez. Böylece hata kaydı geri bildirimi taze kalır.
  - Hızlanılırsa sıradaki dilim zaten hazırdır. Üretim bir sonraki kapanışta yeniden 1 hafta öne geçer.
  - Dönem sonunda atlanan üniteler hiç üretilmez.

**Sıfırıncı dilim ve pilot**: Program başlamadan önce bir kerede şunlar hazırlanır: repo iskeleti, şema + `dogrula.py`, Hoca skill'leri, üretim skill'i, D1 dönem paketi, D1'in 1. haftası (**pilot**) ve 2. hafta. Pilot haftanın kapanışında ünite formatı ve şablonlar **bir kez** gözden geçirilir. Değişiklikler yalnızca henüz üretilmemiş dilimlere uygulanır; 2. hafta geriye dönük yeniden yazılmaz.

**Sonraki bilete kalan**: Hazır kaynağı olmayan alanlarda (bio-ML, debug, LLM pretraining/RLHF teorisi, dağıtık eğitim) Üretici'nin zor soruları nasıl türeteceği → **Kaynağı olmayan alanlarda soru türetme yöntemi**.
