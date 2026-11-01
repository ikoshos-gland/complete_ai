# 13: /degerlendir ve /mock

Spec: [../spec.md](../spec.md) (user stories 61–63, 67–72, Modül 5)

**What to build:** Öğrenen tutarlı kod geri bildirimi ve dürüst mülakat provası alır. `/degerlendir` önce testleri koşar, sonra doğruluk, sayısal kararlılık/kenar durumlar, verim ve okunabilirliği 0–2 puanlar (herhangi bir test kalırsa doğruluk ≤1, toplam not yok); ödevin soru kısmını takip zinciri kuralıyla, Debug görevini Yerleştirilmiş hatalar listesine karşı değerlendirir. `/mock <tur>` mülakatçı moduna geçer: turun gerçek süresi, açıklama yok, gerçek mülakatçı düzeyinde ipucu; sorular zayıf alanlara ağırlıklı, çalışılmamış alt konulardan değil; kodlu mock'ta öğrenen dosyaya yazar, testler sonra koşar. Mock, sinyal başına güçlü/zayıf ve strong hire … no hire rubriğiyle biter, ardından öğretmen moduna dönülür ve her kırılma kaydedilir. Ara sınav ve Final haftası ayrı komut değildir; sınav klasöründeki tanımı okuyan `/mock` turları dizisidir ve sonunda `kayit/` altına sınav raporu yazılır. Kararlar [10](../../ml-mulakat-programi/issues/10-sinav-ve-odev-formati.md) biletinde.

**Blocked by:** 11 (Hoca ortak protokolleri ve /gun)

**Status:** ready-for-agent

- [ ] `/degerlendir` testleri önce koşar; dört ölçüt 0–2; test kalırsa doğruluk ≤1
- [ ] Debug değerlendirmesi bulunan ve kaçırılan hataları listeler
- [ ] `/mock` mülakatçı modunda açıklama yapmaz; sonda rubrik verir, sonra öğretmen moduna döner ve kırılmaları hata kaydına yazar
- [ ] Ara sınav, sınav havuzundan çekilen bir `/mock` turları dizisi olarak çalışır ve sınav raporu yazar
- [ ] Sınav soruları tekrar betiğine sınav kuralıyla eklenir
- [ ] Örnek bir kodlu soru, bir Debug görevi ve küçük bir sınav tanımıyla elle gösterilir
