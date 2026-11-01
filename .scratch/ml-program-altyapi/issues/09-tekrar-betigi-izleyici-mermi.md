# 09: Tekrar betiği izleyici mermisi

Spec: [../spec.md](../spec.md) (user stories 41–43, 46, 49, Modül 4, Testing Seam 2)

**What to build:** Hoca tekrar dosyasını elle düzenlemez; tekrar YAML'ının tek yazarı bu betiktir. Bu bilet banka sorusu kartları için uçtan uca yolu açar: `ekle` bir banka sorusunu kart olarak ekler, `sonuc` ulaşılan en derin halkayı kaydeder ve kartı Leitner'e göre taşır (hedef halkaya ulaşan bir kutu ilerler, kırılan 1. kutuya döner; aralıklar 1 → 3 → 7 → 14 → 30 gün), `bugun` zamanı gelen kartları listeler. Hedef halka ve halka yapısı bankadan id ile okunur. Bugünün tarihi parametre olarak verilebilir.

**Blocked by:** 04 (Soru gövdesi ve frontmatter yapısı)

**Status:** ready-for-agent

- [ ] `ekle`, `sonuc`, `bugun` işlemleri çalışır
- [ ] Hedef halkaya ulaşan kart bir kutu ilerler; kırılan kart 1. kutuya döner; aralık tablosu 1/3/7/14/30
- [ ] "Geçti" sorunun kendi hedef_halka'sına göre değerlendirilir (son halka bonus L3 ise önceki halka)
- [ ] Bugünün tarihi parametre olarak verilebilir
- [ ] Tekrar YAML'ı insan tarafından okunabilir kalır
- [ ] Testler bir tekrar YAML'ı ve küçük bir banka verir, tarihi sabitler, yazılan YAML'ı ya da günün listesini kontrol eder
