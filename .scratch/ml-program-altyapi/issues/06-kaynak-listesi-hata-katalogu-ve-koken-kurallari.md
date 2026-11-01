# 06: Kaynak listesi, hata kataloğu ve köken kuralları

Spec: [../spec.md](../spec.md) (user stories 28–30, 35–36, Modül 3)

**What to build:** Hiçbir soru yoktan türetilmez. Kaynak listesi (alan → kaynaklar: kısa id, URL/konum; Bio-ML altında ayrı `proje` grubu) ve hata kataloğu (`hk-NNN` id'li maddeler: kategori, açıklama, çapa) iki YAML dosyası olarak tanımlanır ve doğrulayıcı onları da kontrol eder. Her `kaynaklar` girdisi kaynak listesindeki bir kaynağa ya da bir banka id'sine çözülür. L3 sorularında `koken: original` reddedilir, türetilmiş soruların halkaları `Çapa:` satırıyla biter, `rewritten` sorular kayıtlı kaynak metnin birebir kopyası olamaz. Altyapı yalnızca biçimi ve testler için küçük bir tohum getirir; asıl doldurma içerik üretimine aittir.

**Blocked by:** 02 (Doğrulayıcı izleyici mermisi)

**Status:** ready-for-agent

- [ ] Kaynak listesi ve hata kataloğu dosyaları küçük bir tohumla repoda; id biçimi, zorunlu alanlar ve çapa doğrulanır
- [ ] Çözülemeyen `kaynaklar` girdisi hata verir
- [ ] L3 + `koken: original` hata verir
- [ ] Türetilmiş soruda `Çapa:` satırı olmayan halka hata verir
- [ ] Kayıtlı kaynak metnin birebir kopyası olan `rewritten` soru hata verir
- [ ] Testler: çözülmeyen kaynak, L3 original, eksik çapa, birebir kopya, bozuk katalog maddesi varyantları
