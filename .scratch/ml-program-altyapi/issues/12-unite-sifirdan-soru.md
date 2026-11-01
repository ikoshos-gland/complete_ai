# 12: /unite, /sifirdan, /soru

Spec: [../spec.md](../spec.md) (user stories 55–60, 73–74, Modül 5)

**What to build:** Her ünite aynı hissettirir. `/unite <id>` 9 adımlı döngüyü yürütür (soğuk deneme → seçilmiş video → Türkçe açıklama → pratik görev → 2–3 soru → opsiyonel video → çizim → İngilizce prova → hata kaydı), pratik görevi çalışma alanına kopyalar ve bankadaki asla değişmez, vurguyu hata kaydına göre uyarlar ama önceden üretilmiş içeriği yeniden yazmaz. `/sifirdan <kavram>` kavramı hiçbir ön bilgi varsaymadan anlatır. `/soru` çalışılmış konulardan, `verified` ve havuz dışı bir soruyu (alan, alt konu, format, makale, proje filtreleriyle) getirir; Hoca takip zincirini halka halka açar, 0–2 puanlar, 0'da durur, yalnızca o halkanın model cevabını açar ve kaydeder. voxtype dikte cevaplara içerik ve yapı geri bildirimi, çizim fotoğraflarına çizim kontrol listesine göre geri bildirim verilir. Ünite formatı [06](../../ml-mulakat-programi/issues/06-ornek-unite-formati.md) biletinde.

**Blocked by:** 11 (Hoca ortak protokolleri ve /gun)

**Status:** ready-for-agent

- [ ] Üç skill ayrı; ortak kurallara adıyla başvurur, kopyalamaz
- [ ] `/unite` pratik görevi `calisma/` altına kopyalar; banka dosyası değişmez
- [ ] `/soru` yalnızca `verified`, havuz dışı ve çalışılmış alt konulardan soru getirir
- [ ] Halka puanlaması 0'da durur ve yalnızca kırılan halkanın model cevabını açar; sonuç hata kaydına ve tekrar betiğine gider
- [ ] Örnek bir ünite ve birkaç örnek soruyla elle gösterilir
