# 11: Hoca ortak protokolleri ve /gun

Spec: [../spec.md](../spec.md) (user stories 51–54, 75–78, Modül 5)

**What to build:** Öğrenen ne çalışacağına hiç karar vermez. Hoca'nın ortak protokolleri (takip zinciri puanlaması, hata kaydı satır biçimi `tarih | ünite | alan/alt konu | tek satır | durum`, tekrar kuralları ve tekrar betiğinin kullanımı, mock protokolü ve rubriği, dosya haritası) tek bir referans klasöründe durur; skill'ler kuralları kopyalamaz, adıyla başvurur. `/gun` dönem planı ve ilerlemeden günün planını (tekrar bloğu, algoritma bloğu, iki harmanlanmış ünite ya da hafif gün işleri) çıkarır, bitmemiş üniteleri ertesi güne taşır, hafif günde hafta kapanışını yürütür ve Üretici'yi tetiklemeyi hatırlatır, dönem sonunda atlanacak üniteleri öğrenene seçtirir. Gün kapanışında `kayit/` ve `calisma/` tek otomatik commit'le kaydedilir. Davranış kararları [07](../../ml-mulakat-programi/issues/07-hoca-sistemi.md) ve [09](../../ml-mulakat-programi/issues/09-gunluk-ve-haftalik-calisma-sablonu.md) biletlerinde.

**Blocked by:** 08 (Plan, ünite ve video referansları), 10 (Tekrar betiği: kalan kurallar)

**Status:** ready-for-agent

- [ ] Ortak protokol referans klasörü var; her protokol tek yerde yazılı
- [ ] `/gun` skill'i tekrar listesini yalnızca tekrar betiği üzerinden alır
- [ ] Ünite günü, hafif gün ve dönem sonu davranışları küçük bir örnek plan ve ilerleme ile elle gösterilir
- [ ] Hoca yalnızca `kayit/` ve `calisma/`'ya yazar
- [ ] Gün kapanışında `D1-H2-G3` mesajlı tek commit atılır, push yapılmaz
- [ ] Otomatik test yok (spec gereği); kabul, örnek içerikle yapılan bir elle gösterimdir
