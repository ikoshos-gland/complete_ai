# Kaynağı olmayan alanlarda soru türetme yöntemi

Type: grilling
Status: resolved
Blocked by: 12
Map: ../map.md

## Question

Hazır zor soru kaynağı olmayan alanlarda (bio-ML, ML Debugging turu / "training loop'u debug et", LLM pretraining ve RLHF teorisi, dağıtık eğitim) Üretici zor soruları ve takip zincirlerini nasıl türetecek?

- Girdi ne olacak: makale, repo, kitap bölümü, bilinen hata/olay raporları? Her alan için kaç tane ve hangi tür kaynak?
- Debug görevlerindeki hatalar nereden gelir: gerçek repo hataları/issue'ları mı, bilinen hata kataloğu mu (ör. yanlış maske, softmax ekseni, gradyan birikimi), yoksa ikisinin karışımı mı?
- Bio-ML'de L3 halkası ne demek (ör. AF2/AF3 mimari ayrıntısı, ESM sıfır-atış skorunun varsayımları)?
- Türetilmiş bir sorunun "doğru" olduğunu kalite kapısının 6. adımı (doğrulayıcı ajan) neye dayanarak denetler: kaynağa geri izlenebilirlik mi, bağımsız ikinci türetim mi?
- `köken` alanı türetilmiş sorularda nasıl doldurulur?

Not (**İçerik üretim sırası ve devri** kararı): Sorular dilimle birlikte, yalnızca o haftanın istediği kadar üretilir. Sınav havuzu dönem paketinde topluca üretilir ve öğrenenden gizli kalır.

## Answer

**Çapa kuralı**: Türetilmiş her soru en az bir **çapa kaynağa** dayanır: makale bölümü, kitap bölümü, `repo/dosya:satır` ya da olay raporu. Çapasız türetme yapılmaz. Çapalar alan başına sabit bir **kaynak listesinden** seçilir. Başlangıç listesi:
- **Bio-ML**: AF2 makalesi ve Supplement, AF3, ESM-2, ESM-1v (sıfır-atış skoru), ESM3, Evo/Evo2, AlphaMissense, dmol.pub, scverse/scanpy dokümanları, bir segmentasyon makalesi (Cellpose ya da LSD).
- **Debug**: nanoGPT, bankadaki doğrulanmış Implement çözümleri, stas00/ml-engineering (debugging ve instabilities bölümleri), olay raporları (OPT-175B logbook, BLOOM chronicles, Llama 3 raporundaki eğitim kesintileri).
- **Pretraining/RLHF teorisi**: CS336 ders notları, Kaplan, Chinchilla, InstructGPT, PPO, DPO, DeepSeekMath (GRPO), Tülu 3 raporu.
- **Dağıtık eğitim**: How to Scale Your Model (çalışılmış problemleriyle), Ultra-Scale Playbook, ZeRO, Megatron-LM (TP/PP).

**Debug görevleri**: Hatalı kod, bankadaki **doğrulanmış bir Implement sorusunun** `cozum.py`'sine hata enjekte edilerek üretilir. Böylece doğru sürüm ve testler baştan hazırdır. Hatalar id'li bir **hata kataloğundan** seçilir. Kategoriler:
- shape/broadcast, mask, softmax ekseni,
- sayısal kararlılık, gradyan birikimi ve ölçekleme, optimizer state,
- train/eval modu, detach/stop_gradient, dtype/mixed precision,
- LR schedule, veri karıştırma ve sızıntı,
- JAX'a özgü: PRNG key tekrarı, `jit` içinde yan etki.

Her katalog maddesi bir olay raporuna ya da gerçek bir issue'ya çapalanır. Görev başına 2–4 hata bulunur, en az biri **sessizdir** (çökmez, yalnızca loss ya da metrik yanlış çıkar). `## Yerleştirilmiş hatalar` bölümü her hatanın katalog id'sini yazar.

**Taban Implement yoksa**: Üretici aynı dilimde önce taban Implement sorusunu normal bir banka sorusu olarak üretir ve kapıdan geçirir. Debug görevi bu soru doğrulandıktan sonra üretilir. Hoca bu Implement sorusunu Debug ile aynı hafta Implement olarak getirmez.

**L3 tanımı** (bütün alanlar için):
- **L1**: Bileşen ne yapar?
- **L2**: Mekanizma ve neden.
- **L3**: Ya yalnızca makalenin Methods/Supplement kısmında bulunan bir ayrıntı, ya da tek bir ders kitabı cevabı olmayan gerekçeli bir trade-off, varsayım veya başarısızlık analizi.

Bio-ML'den L3 örnekleri:
- triangle multiplicative update neden var,
- AF3 neden IPA'dan diffusion'a geçti,
- ESM sıfır-atış skorunun "evrimsel uygunluk ≈ patojenite" varsayımı ve epistaziyi yok sayması,
- homoloji yoluyla train/test sızıntısı.

Sözlükteki Zorluk tanımı buna göre güncellendi.

**Doğrulayıcı (kapı adımı 6)** iki aşamada çalışır:
1. **Kör ikinci türetim**: Doğrulayıcı soruyu ve halka sorularını görür, model cevapları görmez. Kendi cevabını yazar ve model cevapla karşılaştırır. Uyuşmayan halka işaretlenir.
2. **Çapa izlenebilirliği**: Türetilmiş sorularda her halkanın model cevabı bir `Çapa:` satırıyla biter. Doğrulayıcı çapayı açar ve kaynağa özgü iddiaları (sayılar, mimari ayrıntılar) orada kontrol eder.

Debug görevleri için kapı adımı 2'ye iki otomatik kontrol eklenir:
- Her yerleştirilmiş hata en az bir testi düşürür.
- Sessiz hatanın düşürdüğü test exception ile değil, assertion ile kalır.

Uyuşmazlıkta mevcut kural geçerlidir: en fazla 2 düzeltme turu, geçemeyen öğe dilimden çıkar.

**`koken` ve `kaynaklar`**:
- **`derived`**: Kaynak girişi tam yeri gösterir (bölüm, denklem ya da `dosya:satır`). "AF2 makalesi" yetmez; "AF2 Supp. §1.6.5, Alg. 11" gibi yazılır.
- **`rewritten`**: Hazır bir sorudan ya da çalışılmış problemden yeniden yazılan sorular.
- **Debug görevleri**: `derived` olur. `kaynaklar` alanına taban Implement'in banka id'si ve kullanılan katalog maddelerinin çapaları girer; katalog id'leri yalnızca `## Yerleştirilmiş hatalar` bölümünde yer alır.
- **`original`**: Çapası olmayan sorular. Yalnızca L1–L2'de izinlidir; L3 soru `original` olamaz.

Yeni frontmatter alanı eklenmez.

**İki yeni dosya**:
- `banka/kaynak_listesi.yaml`: alan → kaynaklar; her kaynağın kısa id'si ve URL'si.
- `banka/hata_katalogu.yaml`: `hk-NNN` id'li maddeler; her madde için kategori, açıklama ve çapa.

İkisi de **sıfırıncı dilimde** yazılır; katalog ~25–40 maddeyle başlar. Yeni kaynak ya da katalog maddesi yalnızca dönem paketinde, bilinçli bir kararla eklenir.

`dogrula.py`'ye eklenen kontroller:
- Her `kaynaklar` girişi listedeki bir kaynağa ya da bir banka id'sine çözülür.
- Her katalog id'si katalogda vardır.
- L3 sorularda `koken: original` kullanılmaz.

Sözlüğe eklenenler: çapa kaynak, kaynak listesi, hata kataloğu, sessiz hata.
