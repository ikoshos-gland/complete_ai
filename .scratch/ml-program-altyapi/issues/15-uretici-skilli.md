# 15: Üretici skill'i

Spec: [../spec.md](../spec.md) (user stories 79–90, Modül 6)

**What to build:** Öğrenen hafta kapanışında tek bir komutla Üretici'yi tetikler ve üretim arka planda çalışır. Üretici Hoca'dan ayrı, 7 komuta eklenmeyen tek skill'dir ve iki giriş noktası vardır: **dilim üret** (hafta N kapanışında N+2; öğrenen gerideyse bekler) ve **dönem paketi üret** (dönem planı, CS336 dilimlemesi, alt konu başına ≥2 L2–L3 sorulu sınav havuzu). Üretmeden önce dönem planını, ilerlemeyi, hata kaydını ve sınav raporunu okur; ünite listesini sabit tutar, yalnızca vurguyu kaydırır. Kalite kapısını yürütür: her sorudan sonra ve dilim sonunda doğrulayıcı, ardından taze bağlamlı doğrulayıcı ajan (her model cevabın kör ikinci türetimi + her Çapa satırının kaynağa karşı kontrolü). Debug için taban Implement önce üretilip kapıdan geçirilir, sonra 2–4 katalog hatası (≥1 sessiz) yerleştirilir. Başarısız öğe için en fazla 2 düzeltme turu; geçemeyen ünite dilimden çıkar, aynı dersin sonraki ünitesi öne alınır, çıkarılanlar hafta kapanışında tek satırla (havuz için yalnızca sayı) bildirilir. Yeni kaynak listesi / katalog maddeleri yalnızca dönem paketinde eklenir; D3 paketinde öğrenen projesi belgelerinin dondurulmuş kopyaları kaynak yolu ve commit/tarih başlığıyla alınır. Kararlar [12](../../ml-mulakat-programi/issues/12-icerik-uretim-sirasi-ve-devri.md), [13](../../ml-mulakat-programi/issues/13-kaynagi-olmayan-alanlarda-soru-turetme.md), [15](../../ml-mulakat-programi/issues/15-bio-ml-ogrenen-projeleri.md) biletlerinde.

**Blocked by:** 03 (Id kuralları), 05 (Kodlu sorular), 07 (Debug soruları), 08 (Plan, ünite ve video referansları)

**Status:** ready-for-agent

- [ ] İki giriş noktası (dilim üret, dönem paketi üret) ayrı tanımlı; tetikleme tek komut ve arka planda
- [ ] Doğrulayıcı her sorudan sonra ve dilim sonunda çalışır; dilim ancak sıfır çıkış koduyla açılır
- [ ] Doğrulayıcı ajan taze bağlamda çalışır ve kör ikinci türetim + çapa kontrolü yapar
- [ ] En fazla 2 düzeltme turu; çıkarma ve öne alma kuralı uygulanır; bildirim tek satır, havuz yalnızca sayı
- [ ] Debug üretim sırası: taban Implement kapıdan geçmeden hata yerleştirilmez
- [ ] Kaynak listesi / katalog ekleme yalnızca dönem paketi giriş noktasında yapılır
- [ ] Küçük bir örnek dilimin üretimiyle elle gösterilir (asıl içerik üretimi kapsam dışı)
