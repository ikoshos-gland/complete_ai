# PROTOTYPE · Ünite: Self-Attention & Multi-Head Attention

> Atılacak bir prototip. Amaç: bir ünitenin **formatını**, yani bileşenlerin sırasını ve oranlarını görüp tepki vermek. İçerik kaba.
> Ders: **LLMs I: Architecture & Pretraining** (D1, 3. hafta) · Alan: Transformers & LLMs · Alt konu: Attention & Architecture
> Ön koşul: DL Foundations, backprop ve softmax. Toplam: **~6 sa** (dersin 40 saatinin ~%15'i)

## Akış ve süre

| # | Bileşen | Süre | Pay | Çıktı |
|---|---|---|---|---|
| 0 | Hedefler + soğuk deneme | 10 dk | %3 | S1'e öğrenmeden önce verilmiş 3 dakikalık yazılı cevap |
| 1 | Seçilmiş video (sezgi) | 75 dk | %21 | — |
| 2 | Türkçe açıklama (kesin tanım, şekiller) | 30 dk | %8 | — |
| 3 | Üretilmiş video (boşluk kapatma) | 5 dk | %1 | — |
| 4 | Sıfırdan kod (Implement) | 75 dk | %21 | `kod/` testleri yeşil |
| 5 | Debug | 40 dk | %11 | `debug/` testleri yeşil + 3 İngilizce cümle |
| 6 | Zor sorular + Hoca'nın takip zinciri | 60 dk | %17 | yazılı cevaplar + Hoca puanı |
| 7 | Çizerek anlat | 20 dk | %6 | fotoğraf/çizim + öz değerlendirme |
| 8 | İngilizce sözlü prova | 15 dk | %4 | 2 dakikalık kayıt ya da yazılı transkript |
| 9 | Kapanış: hata kaydı | 10 dk | %3 | zayıf noktalar listesi → Hoca |
| | **Toplam** | **~5,7 sa** | | Video toplamı %22 (tavan %35) |

Akışın mantığı: **önce dene → sezgi → kesinlik → elle yap → kır ve onar → mülakat koşulunda sınan → çiz → İngilizce söyle**.

---

## 0 · Hedefler + soğuk deneme (10 dk)

Ünite sonunda şunları yapabilmelisin:
- Causal multi-head attention'ı 15 dakikada NumPy ile, test geçirecek şekilde yazmak.
- Her tensörün şeklini tahtaya çizerek anlatmak.
- √d_k, maske ve sayısal kararlılık sorularına takip zinciriyle birlikte cevap vermek.

**Soğuk deneme:** Videoya geçmeden önce **S1**'i 3 dakikada yaz. Puanlanmaz; sonda kendi cevabınla karşılaştırırsın.

## 1 · Seçilmiş video (75 dk)

1. **3Blue1Brown, *Attention in transformers, step-by-step* (DL6, 26 dk)**: sorgu/anahtar/değer sezgisi ve maske. Hızı 1×, durdurarak izle.
2. **Karpathy, *Let's build GPT*: yalnızca self-attention bölümü (~45 dk)** [zaman damgaları doğrulanmalı]: "matematiksel hile" kısmından tek head'li ve çok head'li attention kodlanana kadar. Kodu yazma, sadece izle; yazmayı 4. adımda kendin yapacaksın.

## 2 · Türkçe açıklama (30 dk)

**Tanım.** Girdi `X ∈ R^{T×d}`. Projeksiyonlar `Q = XW_Q`, `K = XW_K`, `V = XW_V`.

```
Attention(Q, K, V) = softmax(QKᵀ / √d_k + M) V
```

`M`, causal maskedir: `j > i` için `-∞`, diğer yerlerde `0`. Maske **softmax'tan önce** eklenir. Sonra eklenirse satırlar 1'e toplanmaz (bkz. Debug).

**Şekiller** (B batch, T uzunluk, H head, d_h = d/H):

| Tensör | Şekil |
|---|---|
| X | (B, T, d) |
| Q, K, V → head'lere bölünmüş | (B, T, d) → (B, T, H, d_h) → **transpose** → (B, H, T, d_h) |
| QKᵀ (skorlar) | (B, H, T, T) |
| ağırlıklar × V | (B, H, T, d_h) |
| birleştir + W_O | (B, T, d) |

**Neden √d_k?** `q` ve `k` bileşenleri bağımsız, ortalaması 0 ve varyansı 1 ise `q·k`'nin varyansı `d_k` olur. Bölmezsen skorlar büyür, softmax tek bir token'a yığılır (doygunluk) ve gradyan neredeyse sıfıra iner. √d_k'ye bölmek varyansı tekrar 1'e çeker.

**Maliyet.** Skor matrisi T×T boyutunda olduğu için zaman ve bellek O(T²·d). Bu, sonraki ünitelerin (FlashAttention, KV cache) çıkış noktası.

**Permütasyon.** Maskesiz attention permütasyona eşdeğişkendir: token'ların sırası karışırsa çıktıların sırası da aynı şekilde karışır. Sıra bilgisini positional encoding verir (sonraki ünite).

## 3 · Üretilmiş video taslağı (5 dk izleme)

> Attention'ın ana fikri 3B1B'de çok iyi anlatıldığı için uzun bir video gerekmiyor. Burada yalnızca **tek bir boşluğu** kapatan kısa bir video var. Bu, formatın kendisini göstermek için.

**"√d_k: softmax neden doyar?"** · Manim CE · ~2 dk · altyazılı, seslendirme yok

| Sahne | Görüntü | Altyazı (TR) |
|---|---|---|
| 1 | d_k=4 ve d_k=512 için rastgele q·k histogramları yan yana; ikincisi çok geniş | "Boyut büyüdükçe nokta çarpımın varyansı d_k kadar büyür." |
| 2 | Bu skorlardan çıkan softmax çubukları: d_k=512'de tek çubuk ~1, diğerleri ~0 | "Softmax doyar: neredeyse one-hot olur." |
| 3 | Softmax Jacobian'ının ısı haritası sönüyor | "Doygun softmax'ın gradyanı neredeyse sıfırdır; öğrenme durur." |
| 4 | Skorlar √d_k'ye bölünür, histogram daralır, çubuklar yayılır | "√d_k'ye bölmek varyansı 1'e çeker." |

## 4 · Sıfırdan kod (75 dk)

`kod/attention.py` içindeki `softmax`, `scaled_dot_product_attention` ve `multi_head_attention` fonksiyonlarını doldur.

```bash
uv run pytest kod/        # başta 11 test düşer; hepsi geçince biter
```

Kurallar: yalnızca NumPy; T üzerinde döngü yok. İlk 45 dakikada Hoca'ya soru sorma. Takılırsan önce testin adını oku: hangi özelliği beklediğini söylüyor.
Bitirince referansla karşılaştır: `cozumler/attention_cozum.py`.

## 5 · Debug (40 dk)

`debug/buggy_mha.py`: loss düşüyor ama üretimler anlamsız, uzun dizilerde ise NaN çıkıyor. Kodda 3 hata var. Hepsini düzelt (`uv run pytest debug/`) ve her hata için mülakatta söyleyeceğin bir İngilizce cümle yaz:

> "The bug was ___, which causes ___ because ___."

## 6 · Zor sorular (60 dk)

Önce hepsini yazılı cevapla. Sonra Hoca her soruda takip zincirini sırayla açar; sen cevap verdikçe bir sonraki halkaya geçer. Model cevaplar katlanmış durumda, en son aç.

**S1** · ML Depth · Conceptual · L2 · *anahtar kelime: scaling, softmax saturation*
Why do we divide by √d_k in scaled dot-product attention?
- ↳ L2: What happens to the gradients at initialization if you don't?
- ↳ L3: Why √d_k and not d_k? Under µP, attention uses 1/d_k. Why?

<details><summary>Model cevap</summary>
q·k'nin varyansı d_k'dir, bölünmezse softmax doyar ve gradyanlar söner. √d_k varyansı 1'e normalize eder. µP'de genişlik büyüdükçe q ile k, eğitim sırasında birbirleriyle korelasyonlu hâle gelir; bu durumda q·k, √d_k ile değil d_k ile büyür. Bu yüzden µP 1/d_k kullanır.
</details>

**S2** · ML Depth · Estimation · L2 · *ilgili alan: ML Systems & Distributed Training* · *anahtar kelime: FLOPs, quadratic*
For one layer with d=4096 and T=8192, estimate the forward FLOPs of the attention score/value matmuls vs. the linear layers (QKVO + 4× MLP). At what T does attention dominate?
- ↳ L3: How does this change the case for FlashAttention, given that FlashAttention doesn't reduce FLOPs?

<details><summary>Model cevap</summary>
Lineer katmanlarda token başına ~12d² parametre var, bu da ~24·T·d² FLOP eder. QKᵀ ve AV birlikte ~4·T²·d FLOP. Oran T/(6d) olduğu için attention T ≈ 6d ≈ 24.6k civarında baskın olur. T=8192'de oran ~1/3. FlashAttention FLOP'u azaltmaz; T×T matrisini HBM'e yazmayı ortadan kaldırır, yani bellek ve IO darboğazını çözer.
</details>

**S3** · ML Coding · Implement · L2 · *anahtar kelime: causal MHA*
Implement causal multi-head self-attention in NumPy in 15 minutes. (= 4. adımdaki görev, bu sefer süre tutularak ve testlere bakmadan)
- ↳ L3: Now add a KV cache so that decoding one new token costs O(T·d) instead of O(T²·d). → *LLMs II'ye köprü*

**S4** · ML Debugging · Debug · L2 · *anahtar kelime: fp16, mask, NaN*
Training in fp16, loss becomes NaN only for batches that contain heavily padded sequences. The mask uses `scores.masked_fill(mask, -1e9)`. Diagnose.
- ↳ L3: What happens to a row where *every* key is masked, and how do you make that safe?

<details><summary>Model cevap</summary>
fp16'nın en küçük değeri ~-65504'tür; -1e9 burada -inf'e taşar. Kısmen maskeli satırlarda bu zararsızdır, çünkü exp(-inf)=0. Sorun, padding pozisyonlarındaki **tamamen maskeli** sorgu satırlarındadır: max -inf olur ve exp(-inf − (-inf)) NaN verir. Loss bu pozisyonları maskelese bile NaN·0 = NaN olduğu için NaN geriye yayılır. Düzeltme: `torch.finfo(dtype).min` kullanmak (tamamen maskeli satır NaN yerine düzgün dağılım olur), softmax'ı fp32'de hesaplamak, o satırların çıktısını açıkça sıfırlamak ya da bunları hazır SDPA kernel'ine bırakmak.
</details>

**S5** · ML Depth · Conceptual · L3 · *anahtar kelime: permutation equivariance, NoPE*
Show that self-attention without positional encoding is permutation-equivariant. Then explain why a *decoder-only* model with no positional encoding can still learn position.
- ↳ L3: Could a bidirectional encoder with no positional encoding distinguish "dog bites man" from "man bites dog"?

<details><summary>Model cevap</summary>
Permütasyon matrisi P için Attn(PX) = P·Attn(X). Causal maske bu simetriyi kırar: i. token yalnızca i tane token görür, örneğin ortalamanın varyansı i'ye bağlıdır. Model konumu buradan çıkarabilir (NoPE). Maskesiz encoder'da cümle düzeyindeki havuzlanmış temsil iki cümle için aynıdır; dolayısıyla ayırt edemez.
</details>

**S6** · Research Discussion · Paper Discussion · L3 · *anahtar kelime: attention sinks, StreamingLLM*
StreamingLLM (Xiao et al., 2023) found that models dump attention onto the first token. Why does softmax force this behaviour, and what fixes have been proposed?

<details><summary>Model cevap</summary>
Softmax her satırın 1'e toplanmasını zorunlu kılar. "Hiçbir şeye bakma" seçeneği olmadığı için model fazla ağırlığı her zaman görünen bir token'a (ilk token'a) yığar. Önerilen çözümler: sink token'ı KV cache'te tutmak, öğrenilebilir bir sink ya da softmax paydasına +1 eklemek ("off-by-one" / softmax₁), gated attention.
</details>

## 7 · Çizerek anlat (20 dk)

Kâğıda ya da tablete, **5 dakika süre tutarak** çiz:
1. X'ten çıktıya kadar causal MHA'nın veri akışı, her okun üstünde tensör şekliyle.
2. T=4 için skor matrisi; maskeli hücreler taralı.
3. Head'lere bölme adımında reshape ile transpose'un farkı.

Öz değerlendirme listesi: ☐ Bütün şekiller doğru ☐ Maske softmax'tan önce ☐ √d_k nerede belli ☐ W_O unutulmamış ☐ Çizerken yüksek sesle anlattım.
Çizimin fotoğrafını Hoca'ya ver; eksikleri işaretlesin.

## 8 · İngilizce sözlü prova (15 dk)

"Explain multi-head attention to an interviewer in 2 minutes, then answer S1." Kaydet ya da yazıya dök. Hoca dil açısından değil, **içerik ve yapı** açısından geri bildirim verir: ilk cümle cevap mı, şekiller söylendi mi, örnek var mı?

## 9 · Kapanış (10 dk)

- Soğuk denemedeki cevabını (0. adım) son cevabınla karşılaştır.
- Takıldığın her noktayı tek satır olarak yaz (ör. "S2: MLP FLOP sayımında 2× unuttum"). Bu liste Hoca'nın tekrar planına girer.
