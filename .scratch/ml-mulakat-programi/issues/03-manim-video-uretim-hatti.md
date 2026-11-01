# Manim ile video üretim hattı

Type: research
Status: resolved
Blocked by: —
Map: ../map.md

## Question

Programın kendi animasyon videolarını (3Blue1Brown tarzı) üretmesi için uygulanabilir hat nedir? Manim Community ile ManimGL farkı, bir LLM ajanının Manim kodu yazmasının güvenilirliği (bilinen projeler/deneyimler), render gereksinimleri (yerel Linux makine), seslendirme seçenekleri (yok / TTS / altyazı) ve videonun ders ünitesine nasıl bağlanacağı. Kavram başına makul üretim süresi nedir?

## Answer

- **Motor:** Manim Community Edition, sürüm sabitlenmiş halde (v0.22.1, Ekim 2026, aktif bakımda). ManimGL'in son sürümü Aralık 2024'te çıktı ve kırıcı değişiklikleri belgelenmiyor. LLM'lerin en sık hatası iki API'yi karıştırmak.
- **Render:** Omarchy'de `pacman -S base-devel cairo pango` + `uv add manim` yeterli. Cairo CPU'da çalışır, GPU gerekmez. LaTeX yalnızca formül için gerekli, Türkçe metin `Text` (Pango) ile yazılır. Kurulum sorun çıkarırsa yedek yol Docker imajı.
- **LLM güvenilirliği:** Tek atışta düşük, döngüyle yüksek. TheoremExplainAgent'ta başarı düzeltme döngüsü olmadan %3–7, en fazla 5 denemeyle %91–96. ManiBench'te Claude-Sonnet-4 tek atışta %66.7 render edebildi. Kodu çalışan videolarda bile layout hataları kalıyor.
- **Önerilen döngü:** script/storyboard → kod → `-ql` render → kare/kontakt sayfası → Claude incelemesi → düzeltme. Teknik doğruluğu öğrenci kontrol etmeli: kod çalışsa da animasyon yanlış olabilir.
- **Ses:** Altyazı (`add_subcaption`) en ucuz seçenek. TTS için manim-voiceover kullanılabilir: Azure (tr-TR Emel/Ahmet, ücretsiz kota), Gemini Flash TTS, ElevenLabs ya da yerelde Chatterbox/XTTS. Maliyet video başına birkaç sent.
- **Gömme:** Ünite klasöründe `media/<kavram>.mp4` ve kaynak `.py` dosyası, markdown'da `<video>` veya `![[...]]`, notebook'ta `%%manim`.
- **Süre (tahmin):** Video başına ilk örneklerde ≈2–4 saat, şablonlar oturunca ≈1–2 saat. Bu yüzden video sayısı sınırlı tutulmalı. Önce tek videoluk bir prototiple süre ölçülmeli.
- Ayrıntılar, kaynaklar ve riskler: [../research/03-manim-video-uretim-hatti.md](../research/03-manim-video-uretim-hatti.md)
