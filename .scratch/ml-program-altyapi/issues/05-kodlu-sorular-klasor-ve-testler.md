# 05: Kodlu sorular: klasör ve testler

Spec: [../spec.md](../spec.md) (user stories 23–24, Modül 2)

**What to build:** Kodlu bir soru hiçbir zaman çözülmüş ya da çözülemez halde gönderilmez. Doğrulayıcı kodlu soruların klasör şeklini (soru.md, gorev.py, test_gorev.py, cozum.py, opsiyonel cozum_numpy.py) kontrol eder ve testleri alt süreçte, sorunun kendi klasöründe, önce çözüme sonra göreve bağlayarak koşturur: çözümde geçmeli, görevde kalmalı. Test tarzı planlama reposundaki ünite prototipinin davranış testlerini izler.

**Blocked by:** 04 (Soru gövdesi ve frontmatter yapısı)

**Status:** ready-for-agent

- [ ] Eksik zorunlu dosya hata verir; cozum_numpy.py yokluğu hata değildir
- [ ] Testler çözüme bağlanınca kalırsa hata verir
- [ ] Testler göreve bağlanınca geçerse hata verir
- [ ] Testler ayrı alt süreçte koşar; bir sorunun çökmesi doğrulayıcıyı durdurmaz, ihlal olarak raporlanır
- [ ] Testler: görevde geçen test ve çözümde kalan test varyantları
