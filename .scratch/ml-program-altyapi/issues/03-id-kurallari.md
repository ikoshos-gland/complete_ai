# 03: Id kuralları

Spec: [../spec.md](../spec.md) (user stories 16–17, Modül 2)

**What to build:** Doğrulayıcı banka id'lerinin `<alan>-NNNN-<slug>` biçiminde ve bankada tekil olduğunu kontrol eder. Ayrıca son commit'teki id kümesini yeni kümeyle karşılaştırır, böylece bir soru başka alana taşınsa bile "id hiç değişmez" kuralı korunur.

**Blocked by:** 02 (Doğrulayıcı izleyici mermisi)

**Status:** ready-for-agent

- [ ] Biçime uymayan id `dosya · kural · açıklama` satırıyla raporlanır
- [ ] İki soruda aynı id hata verir
- [ ] Son commit'te olup yeni ağaçta olmayan ya da değişmiş id hata verir
- [ ] Git geçmişi olmayan (ilk commit öncesi) repoda bu kontrol hata üretmeden atlanır
- [ ] Testler: tekrarlanan id ve değişmiş id varyantları (geçici git reposu ile)
