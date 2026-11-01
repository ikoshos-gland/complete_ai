# 02: Doğrulayıcı izleyici mermisi: şema ve taksonomi

Spec: [../spec.md](../spec.md) (user stories 9–15, 37, 38, Modül 2, Testing Seam 1)

**What to build:** Üretici tek bir komutla repo kökünü, bir dilimi ya da tek bir banka sorusunu doğrular. Herhangi bir ihlalde komut sıfırdan farklı kodla çıkar ve her ihlali `dosya · kural · açıklama` satırıyla bildirir. Bu bilet uçtan uca ilk yolu açar: `schema.yaml`'da veri olarak duran kurallar (tur/alan/format/zorluk değerleri, tur–format geçerlilik matrisi, "Algorithms alanı yalnızca Practical Coding turunda" kuralı, alan başına alt konu listeleri, alan kısaltmaları, `proje` ve `havuz` değerleri) her banka sorusuna uygulanır. Yeni bir alt konu ya da matris değişikliği kod değil şema değişikliğidir. `havuz: sinav` soruları çıktıda yalnızca sayı olarak görünür.

**Blocked by:** 01 (Repo iskeleti ve ortam)

**Status:** ready-for-agent

- [ ] Tek komut; hedef olarak repo kökü (varsayılan), bir dilim ya da tek bir soru yolu alır; ağ kontrollerini kapatan bir bayrağı vardır
- [ ] Çıkış kodu temizde 0, herhangi bir ihlalde 1; her ihlal `dosya · kural · açıklama` satırı
- [ ] tur, alan, format, zorluk ve alt_konu değerleri `schema.yaml`'a karşı kontrol edilir
- [ ] Geçerlilik matrisi ve Algorithms kuralı uygulanır; matris ve listeler kodda sabit değildir
- [ ] ilgili_alanlar 0–2 öğedir ve ana alandan farklıdır
- [ ] Çıktı, havuz sorularının başlığını ya da metnini hiç içermez; yalnızca sayılarını gösterir
- [ ] Testler geçici dizinde bir altın repo kurar; altın repo temiz geçer, her kural için yalnızca o kuralı bozan bir varyant beklenen ihlal satırını üretir
- [ ] Testler yalnızca çıkış kodunu ve çıktı satırlarını kontrol eder, iç fonksiyonlara bakmaz
