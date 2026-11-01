# Algorithms dersleri ile ML Coding turunun ilişkisi

Type: grilling
Status: resolved
Blocked by: —
Map: ../map.md

## Question

Algorithms I/II/III (dönem başına 15 sa, günlük ~30 dk'lık algoritma bloğu, yalnızca Practical Coding turu) ile ML Coding turundaki sorular (attention, sampling, KV cache gibi Implement/Derivation soruları) arasındaki ilişki ne olacak?

- İkisi ayrı mı tutulacak, yoksa algoritma bloğunun bir kısmı ML Coding problemlerine mi ayrılacak? Örnek: "top-k sampling'i heap ile yaz", "beam search", "BPE merge döngüsü".
- Algorithms alanı yalnızca Practical Coding turunda yer alır (**Soru kategori şeması** kararı). Bu sınır, bir algoritma problemi ML bağlamında sorulduğunda nasıl korunur? Hangi alana ve tura etiketlenir?
- ML Coding soruları şu anda dersin ünitelerinde pratik görev olarak geliyor. Algoritma bloğuna kayan bir problem ünite döngüsünü kullanır mı?
- Mock ve Final haftasındaki Practical Coding turları bu karardan nasıl etkilenir?

## Answer

**İki hat ayrı kalır.** Algoritma bloğu (günde ~30 dk, 1 problem, ünite döngüsü yok) yalnızca Practical Coding hattıdır. Algorithms I/II/III'ün 15 saatinden ML Coding'e pay ayrılmaz. ML Coding problemleri (attention, sampling, KV cache, BPE eğitimi vb.) ünitelerde pratik görev olarak kalır. Bunlar genelde 45–90 dk sürer, 30 dk'lık bloğa sığmaz.

**Etiketleme: "değerlendirilen beceri" testi.** Tur ve alan, problemin bağlamına göre değil, mülakatçının neyi puanladığına göre seçilir.
- ML bilgisi gerekmiyorsa (özü veri yapısı ve algoritma): **Practical Coding × Algorithms × Implement**. `ilgili alan` ML alanıdır (ör. Transformers & LLMs). Buna **kılıklı problem** denir.
- ML bilgisi gerekiyorsa (doğruluğu temperature/top-p semantiğine, length penalty'ye, maske mantığına bağlıysa): **ML Coding × ilgili ML alanı × Implement**. `ilgili alan` Algorithms'tir.
- Kararsız kalınan durumda sorulacak soru: "ML bilmeyen güçlü bir yazılımcı bunu tam puanla çözebilir mi?" Evet ise Practical Coding.
- Böylece "Algorithms alanı yalnızca Practical Coding turunda" kuralı korunur. Algorithms, ML Coding sorusunda yalnızca `ilgili alan` olarak görünür ve sayımlara girmez.

**Kılıklı problemler algoritma bloğunda:**
- Haftada ~1 tane (7 problemin 1'i), dönem başına ~4. O haftanın alt konusuna oturur. Örnekler:
  - Arrays & Hashing: BPE çift sayımı, n-gram dedup.
  - Heaps & Greedy: heap ile top-k, k-yollu merge, BPE merge kuyruğu.
  - Trees & Graphs: trie tokenizer, autograd grafının topolojik sırası.
  - DP: edit distance, Viterbi.
- Geri kalan problemler saf LeetCode tarzıdır.
- Blok formatını izler (problem, çözüm, test, kısa İngilizce açıklama). Ünite döngüsüne girmez.
- **30 dk sınırı**: Sığmayan problem algoritma bloğuna giremez. Ya küçültülür ya da ML Coding olarak üniteye gider.

**Kavramın iki yüzü iki ayrı soru olur.** Ör. "heap ile top-k" (Practical Coding, Algorithms) ve "temperature + top-p + top-k sampling'i JAX'te yaz" (ML Coding, LLMs II pratik görevi). Birbirlerini `anahtar kelime` ile bulurlar. Tek bir soru iki tura bölünmez, aynı soru iki hatta tekrar edilmez.

**Mock ve Final'e etkisi:**
- **Ara sınav (D1/D2) Practical Coding**: o dönemin alt konularından saf algoritma problemi, isteğe bağlı 1 kılıklı problem.
- **Final Gün 1 (Temeller)**: saf algoritma, genel SWE tarzı.
- **Final Gün 4 (Bio-ML lab)**: biyo kılıklı problem (sequence alignment DP, k-mer sayımı, genom aralıklarının kesişimi). Bunun için D3'te (DP haftaları) 2–3 biyo kılıklı problem üretilir, en az 2'si `havuz: sinav` olarak ayrılır.
- **ML Coding turları** (Final Gün 1 ve Gün 3) değişmez. Kaynakları ünite pratik görevleri tarzındaki `havuz: sinav` sorularıdır.

Terim: **Kılıklı problem** GLOSSARY'ye eklendi.
