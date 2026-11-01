# 10: Tekrar betiği: kalan kurallar

Spec: [../spec.md](../spec.md) (user stories 44–45, 47–48, 50, Modül 4)

**What to build:** Tekrar betiği programın bütün kart türlerini ve korumalarını taşır. Hata kartı bir banka id'sine bağlanabilir ya da kendi mini soru metnini taşıyabilir. Sınavda kullanılan sorular sınav kuralıyla eklenir (kırılan 1. kutudan, geçen 2. kutudan). `havuz: sinav` sorusu sınavda kullanılmadan eklenemez. `bugun`, `sure_dk` toplamı ~30 dakikayı aşmayacak biçimde sınırlanır, taşanlar ertesi güne kalır. Bilinmeyen id ve bozuk girdi açık bir hata verir ve dosyaya dokunulmaz. Soğuk denemeler ve çizim alıştırmaları kart olmaz.

**Blocked by:** 09 (Tekrar betiği izleyici mermisi)

**Status:** ready-for-agent

- [ ] Banka id'ye bağlı ve mini sorulu hata kartları eklenebilir ve aynı takvimde yaşar
- [ ] Sınav sonrası ekleme: kırılan 1. kutudan, geçen 2. kutudan başlar
- [ ] Sınavda kullanılmamış havuz sorusu reddedilir
- [ ] `bugun` ~30 dakikayı aşmaz; taşan kartlar ertesi gün listelenir
- [ ] Bilinmeyen id ya da bozuk sonuçta hata verilir ve tekrar YAML'ı bayt bayt değişmeden kalır
- [ ] Testler: mini sorulu hata kartı, sınav sonrası başlangıç, 30 dk sınırı ve taşma, havuz reddi, bozuk girdide dosyanın değişmemesi
