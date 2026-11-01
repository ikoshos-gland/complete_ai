# 08: Plan, ünite ve video referansları ve LaTeX taraması

Spec: [../spec.md](../spec.md) (user stories 31–34, 40, Veri sözleşmeleri)

**What to build:** `/gun` hiçbir zaman olmayan bir dosyayı göstermez. Dönem planı YAML şeması (hafta × gün → ünite id'leri + ödev/sınav yuvaları) ve seçilmiş video kataloğu biçimi (id, URL, başlangıç–bitiş, alt konular) tanımlanır. Doğrulayıcı plandaki her ünite, banka id, ödev ve sınavın; ünite sayfalarındaki her banka id ve video id'sinin var olduğunu kontrol eder. Plan ya da ünite tarafından referans verilen `draft` soru hatadır. Video URL'leri HTTP ile kontrol edilir, ağ bayrağıyla kapatılabilir. LaTeX taraması (`$`, `\frac` vb.) banka ve ünite sayfalarını kapsar.

**Blocked by:** 03 (Id kuralları), 04 (Soru gövdesi ve frontmatter yapısı)

**Status:** ready-for-agent

- [ ] Dönem planı ve seçilmiş video kataloğunun şeması doğrulayıcı tarafından kontrol edilir
- [ ] Planda ya da ünitede olmayan id hata verir
- [ ] `draft` soruya referans hata verir
- [ ] Ölü video URL'si hata verir; ağ kapalı bayrağıyla bu kontrol atlanır
- [ ] LaTeX içeren banka sorusu ya da ünite sayfası hata verir
- [ ] Testler ağ kapalı çalışır; HTTP kontrolü yerel sahte bir sunucuya karşı tek ayrı testle sınanır
- [ ] Testler: plan'da olmayan id, draft referansı, LaTeX varyantları
