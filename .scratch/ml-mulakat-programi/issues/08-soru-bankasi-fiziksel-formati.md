# Soru bankası fiziksel formatı

Type: grilling
Status: resolved
Blocked by: 04
Map: ../map.md

## Question

Soru bankası fiziksel olarak nasıl tutulacak? Dosya formatı ve yerleşimi (soru başına tek dosya mı, tek tablo mu) ne olacak? Kategori şemasının dışında soru başına hangi alanlar bulunacak: kaynak ya da türetildiği makale/repo, model cevap, takip zinciri, Implement ve Debug sorularında kod ve test bağlantısı, Whiteboard sorularında görsel bağlantısı? Geçerlilik matrisi ve kontrollü alt konu listesi nasıl doğrulanacak? Tekrar zamanlamasının kendisi **Hoca sistemi** biletinde kalır; bu bilet yalnızca tekrarın ihtiyaç duyduğu veri alanlarını belirler.

Not (Örnek ünite formatı kararı): model cevaplar LaTeX içermez; kısa formüller düz metin/Unicode ya da kod biçiminde yazılır. Ünite soruları bankaya referanstır, kopya değildir.

Not (Hoca sistemi kararı): Tekrar durumu (Leitner kutusu, sonraki tarih) soru dosyasında değil, ayrı bir tekrar YAML'ında tutulur ve sorulara id ile başvurur. Bu yüzden her sorunun kalıcı bir id'si olmalı. Takip zincirinin halkaları ayrı ayrı puanlanır (0–2) ve hedef halkası belirlidir; bu da halkaların ayrı ayrı adreslenebilmesini gerektirir. Hata kartları bir banka sorusuna bağlanabilir.

## Answer

**Birim**: Her banka sorusu bir markdown dosyasıdır: YAML frontmatter ve sabit başlıklı gövde. Kodlu sorular (Implement, Debug) dosya değil klasördür ve şunları içerir:
- `soru.md`
- `gorev.py`: Implement'te iskelet, Debug'da hatalı kod.
- `test_gorev.py`
- `cozum.py`
- `cozum_numpy.py`: isteğe bağlı.

Ünite bu klasörü bir çalışma alanına kopyalar ve öğrenen kopya üzerinde çalışır. Bankadaki asıl dosyalar değişmez.

**Yerleşim**:
```
banka/
  schema.yaml          (değerler, geçerlilik matrisi, alt konu listeleri, Algorithms kuralı)
  dogrula.py           (pytest doğrulayıcı)
  <alan>/<id>-<slug>.md
  <alan>/<id>-<slug>/  (kodlu soru)
```
Alan kısaltmaları: `math` Math · `cml` Classical ML · `dlf` DL Foundations · `tll` Transformers & LLMs · `sys` ML Systems & Distributed Training · `msd` ML System Design · `alg` Algorithms · `bio` Bio-ML.

Bankanın repo içindeki yeri ve çalışma alanının yolu **Proje repo yapısı** kararına kalır.

**Id**:
- Biçim `<alan>-NNNN-<slug>` (ör. `tll-0042-sqrt-dk-scaling`).
- Bütün referanslar `tll-0042` kısmıyla yapılır. Bu kısım bir kez verilir ve hiç değişmez; soru başka alana taşınsa bile aynı kalır.
- Slug yalnızca okunabilirlik içindir.

**Frontmatter alanları**:
- Taksonomi (Soru kategori şeması kararı): `tur, alan, alt_konu, format, zorluk, anahtar_kelimeler, ilgili_alanlar`
- `koken`: `rewritten`, `derived` ya da `original`. `rewritten` sorularda kaynak metin kopyalanmaz, yalnızca bağlantı tutulur.
- `kaynaklar`: liste (URL, kitap+bölüm, repo+dosya).
- `kaynak_zorluk`: kaynağın kendi etiketi, yalnızca bilgi için.
- `makale`: isteğe bağlı, Paper Discussion ve Research Discussion sorularında **tartışılan** makale. Kökenden ayrı bir alandır.
- `hedef_halka`: tekrarda geçme eşiği. Varsayılanı son halkadır; son halka bonus L3 ise daha önceki bir halka seçilir.
- `sure_dk`: tahmini cevap süresi. Mock'u doldurmak ve ünite planı için kullanılır.
- `cerceve`: yalnızca kodlu sorularda, `jax`, `pytorch` ya da `numpy`.
- `durum`: `draft` ya da `verified`. Hoca yalnızca `verified` soruları getirir.

**Gövde**:
```
## Soru
## Model cevap
## Takip zinciri
### H1 · L2
**Soru:** ...
**Model cevap:** ...
### H2 · L3
...
```
- Model cevap halka halka ayrılır, böylece kırılan halkanın cevabı tek başına açılır.
- Halka sayısı 0–4'tür. L1 sorular zincirsiz olabilir.
- Sorunun `zorluk` alanı ana sorunun seviyesidir.
- Model cevaplar Türkçe yazılır, terimler İngilizce kalır.

Format'a özel zorunlu bölümler:
- **Design ve Estimation**: `## Değerlendirme ölçütleri`. Model cevap bir örnek cevaptır, Hoca bu ölçütlere göre puanlar.
- **Whiteboard**: `## Çizim kontrol listesi`. İsteğe bağlı `Referans görsel:` satırı (PNG ya da mermaid/ASCII).
- **Debug**: `## Yerleştirilmiş hatalar`. Her hata için yer, belirti ve düzeltme yazılır. `/degerlendir` ve takip zinciri bu listeyi kullanır.

**Doğrulama**: `dogrula.py`, `schema.yaml`'a göre bankanın tamamını kontrol eder:
- değerler,
- geçerlilik matrisi,
- alt konu listesi,
- Algorithms kuralı,
- zorunlu başlıklar ve format'a özel bölümler,
- id'nin tekil olması.

Kodlu sorularda ayrıca testler `cozum.py`'de geçmeli, `gorev.py`'de kalmalıdır. Doğrulayıcı içerik üretiminde her yeni sorudan sonra ve Hoca bankayı her değiştirdiğinde çalışır.

**Sınırlar**:
- Banka salt içeriktir; durum (kutu, son görülme, puan) tekrar YAML'ında tutulur.
- Tekrarın bankadan okuduğu alanlar: id, `hedef_halka` ve halka yapısı.
- Ünitelerin pratik görevleri de banka sorusudur. Üniteler, tekrar ve mock bankaya id ile başvurur.
- Mini sorular bankaya girmez, tekrar kartının içinde yaşar. İyi çıkan bir mini soru bilinçli bir kararla bankaya alınabilir.

Sözlük güncellendi: banka sorusu, model cevap, hedef halka, köken, mini soru.

> Not: **Sınav ve ödev formatı** kararı soru dosyasına sabit bir `havuz` alanı ekler (`sinav` değerli sorular ünite, tekrar ve `/soru`'da kullanılmaz). Hedef: alt konu başına L2–L3'ten en az 2 sınav sorusu. Bkz. [10](10-sinav-ve-odev-formati.md).
