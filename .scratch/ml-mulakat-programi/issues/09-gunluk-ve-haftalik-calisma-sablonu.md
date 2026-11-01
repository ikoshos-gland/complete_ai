# Günlük ve haftalık çalışma şablonu

Type: grilling
Status: resolved
Blocked by: —
Map: ../map.md

## Question

5 saatlik bir gün nasıl doldurulur? Gün 30 dakikalık tekrar bloğuyla başlar ve ardından ~2 ünite gelir (Hoca sistemi kararı). Bir dönemin paralel dersleri günlere ve haftalara nasıl dağıtılır: her gün iki farklı dersten birer ünite mi, ders blokları mı? Algorithms (dönem başına 15 sa) hangi günlere girer? D1'deki kaydırma (Foundations 1–2. haftalarda, LLMs I 3–4. haftalarda) haftalık plana nasıl yansır? Haftalık ödev haftanın neresine konur? Rezerv saatleri haftalara nasıl dağıtılır? `/gun` komutu bu şablonu nereden okur?

## Answer

**Takvim**: 3 dönem × 4 hafta × 7 gün × 5 sa = 420 sa, artı ayrı bir **Final haftası** (13. hafta, 6 gün × 5 sa = 30 sa). Toplam 450 sa. Tam dinlenme günü yok; her haftanın 7. günü hafif gündür.

| | Ders saati | Rezerv | Toplam |
|---|---|---|---|
| D1 | 135 | 5 | 140 |
| D2 | 135 | 5 | 140 |
| D3 | 115 | 25 | 140 |
| Final haftası | — | 30 | 30 |
| **Toplam** | **385** | **65** | **450** |

Bu tablo **Ders listesi ve dönemlere dağılım** kararındaki rezerv dağılımının (15 / 15 / 35) yerini alır. Final mock (~20 sa) D3'ten Final haftasına taşınır; haftanın kalan ~10 saati son tampondur.

**Tekrar bloğunun saati**: Tekrar, kartın geldiği dersin saatinden sayılır. Ders saati "yeni içerik + o dersin tekrarı" demektir. Rezerv yalnızca sınav ve tampona kalır.

**Ünite günü** (haftanın 1–6. günleri, 5 sa):
1. Tekrar bloğu: 30 dk.
2. **Algoritma bloğu**: 30 dk, günde 1 problem. 9 adımlık ünite döngüsünü kullanmaz: problem, çözüm, test, kısa İngilizce açıklama. Dönem başına 28 gün × 0,5 sa ≈ 14 sa, yani Algorithms I/II/III'ün 15 saati.
3. İki ünite (~2 sa + ~2 sa). Üniteler iki farklı dersten **harmanlanır**.

**Hafif gün** (7. gün, 5 sa):
- Tekrar (30 dk) + algoritma (30 dk).
- ~3 sa haftalık ödev. Ödev, haftanın iki ana dersinin o hafta işlenen konularını kapsar.
- ~1 sa **hafta kapanışı**: kaymayı kapatmak ve haftanın hata kaydına toplu bakış.
- Yeni ünite yok.
- D1 ve D2'nin 4. haftasında ödevin yerini **ara sınav** alır (~3 sa). D3'te ara sınav yoktur, yerini Final haftası alır.
- Dönem rezervinin 5 saati 1–3. haftaların kapanış saatlerine gider.

**Haftalık hacim**: 6 gün × 2 = 12 ünite/hafta, dönem başına 48 ünite yuvası (~96 sa).

**Yuva dağılımı**: Bir dersin dönemdeki ünite sayısı, saatiyle orantılıdır. Gerektiğinde aynı dersten iki ünite aynı güne düşer.
- **D1**: ML Foundations ~14, DL Foundations ~18, LLMs I ~16. 1–2. haftalar ML 14 + DL 10, 3–4. haftalar DL 8 + LLMs I 16. Ön koşul kaydırması böyle sağlanır.
- **D2**: LLMs II ~22, ML Systems ~26. İki ders her gün yan yana gider.
- **D3**: ML System Design ~15, Bio-ML ~22. Kalan ~11 yuva (~20 sa, D3'ün fazla rezervi) **program geneli kayma tamponudur**: D1–D3'te biriken kayma burada kapatılır, artanı Hoca hata kaydındaki en zayıf alanlara verir.

**Dönem planı ve `/gun`**:
- Her dönem için bir **dönem planı** içerik üretiminde önceden yazılır (hafta × gün → ünite id'leri + ödev/sınav yuvaları).
- `/gun` planı ilerleme dosyasıyla birlikte okur.
- Bitmeyen ünite ertesi güne kayar, plan onunla birlikte ilerler. Kayma hafta kapanışında, sonra dönem rezervinde, en son D3 tamponunda kapatılır.
- Dönem sonunda hâlâ kayma varsa Hoca o dönemin bitmemiş ünitelerini listeler, atlanacakları öğrenen seçer.
- Dönem planının dosya yeri **Proje repo yapısı** biletine kalır.
- Ödev ve ara sınavın içeriği, Final haftasının tur sırası **Sınav ve ödev formatı** biletine kalır.
