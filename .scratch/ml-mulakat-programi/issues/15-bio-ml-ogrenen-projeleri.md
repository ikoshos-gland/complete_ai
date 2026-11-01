# Bio-ML'de öğrenenin kendi projelerinin kullanımı

Type: grilling
Status: resolved
Blocked by: —
Map: ../map.md

## Question

Öğrenenin kendi projeleri Bio-ML dersinde ve soru bankasında nasıl kullanılacak? Projeler: KIF13A varyant atlası ve AlphaMissense kalibrasyonu, Evo2 skorları, LSD/AcRLSD nöron segmentasyonu, PD–NPH yürüyüş benchmark'ı.

- Hangi ünitelerde örnek olay olarak yer alırlar?
- Hangi tur ve formatta soru üretirler? Aday: Research Discussion ("projeni anlat" derin dalışı), Paper Discussion, ML Debugging (ör. pdnph-bench'teki feature-selection sızıntısı).
- Proje dosyaları ve raporları **kaynak listesine** çapa olarak girer mi? `koken` alanı nasıl doldurulur?
- Bu sorular mock'taki "project deep dive" ya da Behavioral turuyla nasıl ilişkilenir?

Not (**Kaynağı olmayan alanlarda soru türetme yöntemi** kararı): Her türetilmiş soru, kaynak listesindeki bir çapaya dayanır. L3 sorular `original` olamaz.

## Answer

**Projeler** (3 adet; Evo2 skorları atlasın içindedir): `kif13a-atlas` (AlphaMissense/paralog kalibrasyonu + Evo2), `acrlsd` (LSD/AcRLSD, LICONN), `pdnph-bench` (PD–NPH yürüyüş benchmark'ı).

**Proje üniteleri**: Bio-ML dersine 4 ayrı proje ünitesi eklenir, toplam ~10 sa. Bu saatler dersin 60 saatine eklenir ve Bio-ML %13'ten ~%15'e çıkar. Üniteler normal ünite döngüsünü izler, yalnızca seçilmiş videonun yerine öğrenenin proje raporu okunur. Her ünite ilgili alt konunun son ünitesidir, id'leri `bio-NN` dizisinde ilerler:

| Ünite | Alt konu |
|---|---|
| atlas-kalibrasyon | Variant Effect Prediction |
| atlas-Evo2 | Variant Effect Prediction (kısmen Protein/DNA Language Models) |
| LSD | Bioimage Segmentation |
| pdnph | Biological Data Pitfalls |

Yeni alt konu açılmaz.

**Tur ve format** (geçerlilik matrisi değişmez):
- Research Discussion × Conceptual/Design: "projeni anlat" derin dalışı (neden bu yöntem, alternatifler neydi, bir daha yapsan neyi değiştirirdin). Paper Discussion kullanılmaz.
- ML Debugging × Debug: gerçekten yaşanmış hata yeniden kurulur. Standart Debug kuralı işler: 2–4 hata, en az biri sessiz.
- ML Depth × Conceptual/Estimation: projenin dayandığı kavram sorulur (ör. AlphaMissense eşik kalibrasyonu, VOI).

**`proje:` alanı**: Soru dosyasına isteğe bağlı bir alan eklenir. Değerleri sabit 3 id'dir. `makale:` alanının eşidir: kökenden ve çapadan ayrıdır. Hoca tekrar ve mock için bu alana göre süzer.

**Çapa ve köken**:
- Proje belgeleri kaynak listesine Bio-ML altında ayrı bir `proje` grubu olarak girer.
- Çapalar **dondurulmuş kopyalara** işaret eder: D3 dönem paketinde Üretici ilgili belgeleri `banka/proje_kaynaklari/<proje>/` altına kopyalar ve her kopyanın başına kaynak yolu ile commit/tarih notu yazar. Gerekçe: LSD ve pdnph'in kodu yalnızca TRUBA ve GitHub'da, atlas da değişmeye devam ediyor. Kalite kapısı TRUBA'ya erişmeden bu kopyalar üzerinde çalışır.
- Başlangıç kopyaları:
  - atlas: `README.md`, `docs/kalibrasyon_olcumleri.md`, `docs/missense_sonuc.md` (repo `~/Claude/kif13a-neurovariant-atlas`)
  - LSD: `acrlsd-truba` skill'inin `references/results.md` ve `traps.md` dosyaları (`claude-config` repo'su)
  - pdnph: `pdnph-bench` skill'inin `references/methodology.md` dosyası
- `koken: derived` olur, L3 dahil.

**"Neden" halkaları**: Model cevap öğrenenin gerçek gerekçesini uydurmaz. Bu halkalar için rubrik yazılır: iyi bir cevap hangi alternatifleri, trade-off'ları ve sınırlamaları anmalı. Olgusal halkalar (sayılar, mimari, sonuç) çapaya bağlı kalır. Öğrenen önceden onaylamaz. Gerçek gerekçe ilk provada kayda geçer ve hata kaydı/tekrar akışıyla ilerler.

**pdnph'te gerçek sonuç yok**: Envanter yalnızca sentetik veriyle uçtan uca kontrol buldu. Bu yüzden ünite ve sorular metodoloji üzerine kurulur: greedy seçim sızıntısı (≈0.80, örneklem içi), nested LOSO (dürüst aralık ~0.70–0.75), saf gürültü testi, N=23 yayın karşılaştırması (0.70 acc / 0.74 AUC), "N≈50'de ≥0.85 kırmızı bayrak" kuralı. Gerçek kohort sayısı uydurulmaz. D3 paketine kadar gerçek sonuç çıkarsa kopya yenilenir. Debug görevi sentetik veriyle kurulur.

**Hata kataloğuna eklenen gerçek olaylar** (çapaları dondurulmuş kopyalar). Bu maddeler başka alanların Debug görevlerinde de kullanılabilir:
1. pdnph: özellik seçimi ile değerlendirme aynı LOSO'da (sessiz)
2. LSD: kimlik düzeyinde train/test sızıntısı; voksel örtüşmesi yok ama 519 ortak nöron id'si, test voksellerinin %29.5'i (sessiz)
3. LSD: küçük test bloğunun VOI'yi şişirmesi; 144³'te 0.445, tam hacimde 1.288 (sessiz)
4. LSD: anizotropik vokselde (18×18×24 nm) z↔y/x transpoze eden augmentasyon (sessiz)
5. LSD: job resume'da iterasyon sayacının 0'dan başlaması
6. atlas: aday listesini gnomAD'de görülmüş varyantlarla sınırlamak, yani seçim yanlılığı; KIF1A patojeniklerinin %89'u gnomAD'de yok (sessiz)

**Mock ile ilişki**:
- Final Gün 4'teki (Bio-ML lab) Research Discussion turu **proje derin dalışı** olur: mülakatçı bir projeyi seçer ve L3'e kadar zorlar. Bio makale tartışması D3 ünitelerinde ve ödevlerinde çalışılır.
- Behavioral ayrı kalır ve bankaya girmez. Projeler orada yalnızca hikâye malzemesidir.
- D3 sınav havuzuna `proje:` alanlı en az 2 `havuz: sinav` sorusu ayrılır.

Sözlüğe eklenenler: proje ünitesi, öğrenen projesi, proje derin dalışı.
