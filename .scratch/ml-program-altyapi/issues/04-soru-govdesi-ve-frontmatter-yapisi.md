# 04: Soru gövdesi ve frontmatter yapısı

Spec: [../spec.md](../spec.md) (user stories 18–22, Veri sözleşmeleri)

**What to build:** Hoca hiçbir zaman yarım doldurulmuş bir soruyla karşılaşmaz. Doğrulayıcı her banka sorusunda zorunlu gövde başlıklarını (Soru, Model cevap, Takip zinciri), `H<n> · L<k>` biçimindeki 0–4 halkayı, format başına zorunlu bölümleri (Design/Estimation için Değerlendirme ölçütleri, Whiteboard için Çizim kontrol listesi, Debug için Yerleştirilmiş hatalar) ve zorunlu frontmatter alanlarını kontrol eder. Alanlar ve gövde düzeni [08](../../ml-mulakat-programi/issues/08-soru-bankasi-fiziksel-formati.md) cevabındaki gibidir, artı `havuz` ve `proje`; yeni alan eklenmez.

**Blocked by:** 02 (Doğrulayıcı izleyici mermisi)

**Status:** ready-for-agent

- [ ] Eksik zorunlu başlık ya da biçimi bozuk / 4'ten fazla halka hata verir
- [ ] Format başına zorunlu bölüm eksikse hata verir
- [ ] koken, kaynaklar, hedef_halka, sure_dk, durum zorunludur; kodlu sorularda `cerceve` de zorunludur
- [ ] hedef_halka var olmayan bir halkayı gösterirse hata verir
- [ ] makale, proje, havuz alanları varsa izin verilen değerlere karşı kontrol edilir
- [ ] Zorunlu bölüm listeleri `schema.yaml`'dan okunur
- [ ] Testler: eksik bölüm, olmayan hedef halka, bozuk opsiyonel değer varyantları
