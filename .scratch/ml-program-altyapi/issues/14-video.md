# 14: /video

Spec: [../spec.md](../spec.md) (user stories 64–66, Modül 5)

**What to build:** Üretim maliyeti yalnızca gerektiğinde ödenir. `/video <kavram>` önce seçilmiş video kataloğunda eşleşen bir kayıt önerir. Öğrenen yine de isterse Manim CE ile arka planda bir video üretir: `-ql` render → kare/kontakt sayfası → inceleme → düzeltme döngüsü, ses yerine altyazı. Kaynak ve seslendirme metni commit'lenir, render çıktısı commit'lenmez. Haftada 2'den fazla video, kayıttan sayılarak reddedilir. Üretim hattı araştırması [03](../../ml-mulakat-programi/research/03-manim-video-uretim-hatti.md) belgesinde.

**Blocked by:** 11 (Hoca ortak protokolleri ve /gun)

**Status:** ready-for-agent

- [ ] Önce `secilmis.yaml` taranır ve eşleşme varsa önerilir
- [ ] Üretim arka planda çalışır; ünite beklemez
- [ ] Render → kare inceleme → düzeltme döngüsü en az bir örnek kavramla uçtan uca çalışır (`video` grubu kuruluyken)
- [ ] Haftanın 3. video isteği kayda bakılarak reddedilir
- [ ] Manim kaynağı ve seslendirme metni commit'lenebilir yerde; render çıktısı gitignore'da
