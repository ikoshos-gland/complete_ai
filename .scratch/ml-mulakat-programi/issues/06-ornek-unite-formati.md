# Örnek ünite formatı

Type: prototype
Status: resolved
Blocked by: 02, 03
Map: ../map.md
Prototype: ../prototypes/unite-attention-PROTOTYPE/ (atılacak; README.md ünite sayfası, kod/ debug/ testleri doğrulandı)

## Question

Bir ünite nasıl görünmeli? Tek bir konu üzerinde (ör. attention) kaba bir ünite prototipi: seçilmiş video, üretilmiş video taslağı, Türkçe açıklama, sıfırdan kod görevi + testler, debug görevi, zor sorular, çizerek anlatma alıştırması. Bileşenlerin sırası ve oranları nasıl olmalı?

## Answer

Prototip (`../prototypes/unite-attention-PROTOTYPE/`) attention üzerine kurulmuş ~5,7 saatlik, NumPy tabanlı tam bir ünite. Aşağıdaki kararlar bu prototipe verilen tepkilerle alındı; prototipin kendisi bu kararlardan **önceki** hâli gösteriyor (büyüklük ve kod dili değişti).

**Ünite büyüklüğü**: Bir ünite 2–3 saattir ve günde ~2 ünite çalışılır. Bir konu 1–3 üniteden oluşur. Örneğin attention iki ünite olur: (1) videolar + Implement + S1–S3, (2) Debug + S4–S6.

**Her ünite küçük bir tam döngüdür**, sırası sabittir:
1. Soğuk deneme: ünitenin bir sorusuna, öğrenmeden önce 3 dakikalık yazılı cevap.
2. Seçilmiş video (sezgi).
3. Türkçe açıklama (kesin tanımlar, şekiller, eşitlikler; kısa).
4. **Tek** pratik görev: Implement ya da Debug. Aynı konunun ardışık ünitelerinde dönüşümlü gelir. Kod çıkmayan ünitelerde yerine Derivation gelir.
5. 2–3 zor soru: önce yazılı cevap, sonra Hoca takip zincirini halka halka açar.
6. *(İsteğe bağlı)* Üretilmiş video.
7. Çizerek anlat: 5 dk süre tutularak, öz değerlendirme listesiyle; fotoğrafı Hoca'ya verilir.
8. İngilizce sözlü prova: 2 dakikalık anlatım + bir soru. Geri bildirim dile değil, içerik ve yapıya verilir.
9. Hata kaydı: takılınan her nokta tek satır olarak yazılır ve Hoca'ya gider.

**Oranlar** tek tek ünitelere değil, bir konunun ünite grubunun toplamına uygulanan yaklaşık hedeflerdir: video %15–35 (ders düzeyindeki %35 tavanı geçerli) · kod %25–40 · sorular %15–25 · çizim + prova ≥%8.

**Kod**:
- Implement görevleri önce **JAX** ile yazılır; isteğe bağlı bir NumPy karşılığı olur.
- Debug görevleri JAX ve PyTorch arasında karışıktır.
- CS336 ödevleri olduğu gibi PyTorch ile yapılır.
- Testler pytest ile yazılır, testler davranışı sınar (naif referansa eşitlik, gelecek sızıntısı yok, head bağımsızlığı, sayısal kararlılık). Referans çözüm ayrı bir klasörde durur.
- Debug görevinde bir belirti senaryosu verilir, kodda birden çok hata bulunur ve her hata için mülakatta söylenecek bir İngilizce cümle yazılır.

**Üretilmiş video** önceden hazırlanmaz. Öğrenen istediğinde, sorularda takıldığı noktaya özel olarak üretilir (token ve üretim maliyeti yüzünden).

**Zor sorular** bankadaki sorulara referanstır, ünitede kopyalanmaz. Her sorunun Tur × Alan × Format × Zorluk etiketi, anahtar kelimesi ve takip zinciri vardır; model cevap katlanmış durur.

**Formül yazımı (LaTeX yok)**: Kısa formüller düz metin ve Unicode ile ya da kod biçiminde yazılır (`softmax(QKᵀ/√d_k + M)·V`, `q @ k.T / sqrt(d_k)`). Uzun türetimler kâğıtta yapılır, fotoğrafı Hoca'ya verilir. Bankadaki model cevaplar da aynı kurala uyar.
