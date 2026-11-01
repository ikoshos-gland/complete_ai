# Ders listesi ve dönemlere dağılım

Type: grilling
Status: resolved
Blocked by: 02, 04
Map: ../map.md

## Question

Programın dersleri neler, hangi dönemde ve hangi sırayla yer alıyor, her derse kaç saat ayrılıyor? Ön koşul ilişkileri ve 450 saatlik bütçeye dağılım nasıl?

## Answer

**Dersler** (8 ders; Algorithms dönem başına bölündüğü için 10 ders kaydı). Her ders tek bir dönemin içinde başlar ve biter. İki döneme yayılan konular I / II / III diye ayrı derslere bölünür.

**Bütçe**: 450 sa = ~385 sa ders + ~65 sa **rezerv**. Rezerv dönemlere şöyle dağılır: D1 15 · D2 15 · D3 35. D3'ün payının büyük olmasının sebebi ~20 saatlik final mock haftası. Rezervin geri kalanı ara sınav, tekrar ve tampon için.

| Dönem | Ders | Saat | Alan (alt konular) |
|---|---|---|---|
| D1 | ML Foundations | 35 | Math, Classical ML |
| D1 | DL Foundations | 45 | DL Foundations |
| D1 | LLMs I: Architecture & Pretraining | 40 | Transformers & LLMs: Attention & Architecture, Positional Encoding, Tokenization, Pretraining & Data, Scaling Laws |
| D1 | Algorithms I | 15 | Algorithms: Arrays & Hashing, Two Pointers & Sliding Window, Binary Search |
| D2 | LLMs II: Post-training & Inference | 55 | Transformers & LLMs: Post-training, Evaluation, Inference & Decoding |
| D2 | ML Systems & Distributed Training | 65 | ML Systems & Distributed Training |
| D2 | Algorithms II | 15 | Algorithms: Trees & Graphs, Heaps & Greedy |
| D3 | ML System Design | 40 | ML System Design |
| D3 | Bio-ML | 60 | Bio-ML |
| D3 | Algorithms III | 15 | Algorithms: DP + karışık tekrar |

Hatlara göre pay (450 saat içinde): LLM %21 · Sistemler ve Tasarım %23 · Temeller %18 · Bio-ML %13 · Algorithms %10. Bio-ML'in ~%15 hedefinin altında kalan kısmını öğrenenin kendi projeleri kapatır.

**Ön koşullar**:
- ML Foundations → DL Foundations → LLMs I → LLMs II
- LLMs I → ML Systems
- LLMs II + ML Systems → ML System Design
- DL Foundations + LLMs I → Bio-ML
- Algorithms bağımsız.

D1'deki zincir derslerin haftalara kaydırılmasıyla çözülür: Foundations dersleri 1–2. haftalarda yoğun, LLMs I ise 3–4. haftalarda.

**Eşleme kuralı**: Bir sorunun hangi derste çalışılacağını, alanı ve alt konusu birlikte belirler (tablodaki son sütun).

**Inference sınırı**:
- LLMs II algoritma tarafını kapsar: sampling, KV cache kavramı, speculative decoding, MQA/GQA.
- ML Systems donanım ve performans tarafını kapsar: prefill/decode roofline, PagedAttention, bellek ve throughput hesabı, quantization.
- KV cache videosu iki derste de kullanılır.

**Video tavanı**: Bir dersin saatinin en fazla %35'i video izlemeye ayrılır. Çekirdek video listesi (~175 sa) her ders için bu tavana göre kırpılır. Kırpmanın kendisi içerik üretimine aittir.

**CS336 ödevleri**:
- Ödev 1 (tam), ödev 3 (hafif) ve ödev 4 (kısmi) → LLMs I
- Ödev 2 (profiling + Triton FA2, DDP kısmı hariç) → ML Systems
- Ödev 5 (SFT/RL) → LLMs II

Rig'in tek bir 3090'ı yalnızca tek-GPU ödevleri (kernel, profiling) için kullanılır. Dağıtık koşturma yok.

> Not: Rezerv dağılımı ve final mock'un yeri **Günlük ve haftalık çalışma şablonu** kararıyla güncellendi (D1 5 · D2 5 · D3 25 · Final haftası 30; bkz. [09](09-gunluk-ve-haftalik-calisma-sablonu.md)).
