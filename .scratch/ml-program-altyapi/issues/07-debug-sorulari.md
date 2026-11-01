# 07: Debug soruları

Spec: [../spec.md](../spec.md) (user stories 25–27, Modül 2)

**What to build:** Hiçbir yerleştirilmiş hata görünmez değildir. `## Yerleştirilmiş hatalar` bölümündeki her madde, doğrulayıcının onu cozum.py üzerinde tek başına uygulayabileceği kadar kesin tanımlanır (örn. hata başına küçük bir diff bloğu; kesin biçim bu bilette belirlenir, yeni frontmatter alanı eklenmez). Doğrulayıcı her hatayı tek başına uygular ve en az bir testin düştüğünü, sessiz hatanınkinin exception değil assertion ile düştüğünü kontrol eder. Kullanılan her hata kataloğu id'si katalogda bulunmalıdır.

**Blocked by:** 05 (Kodlu sorular), 06 (Kaynak listesi ve hata kataloğu)

**Status:** ready-for-agent

- [ ] Yerleştirilmiş hata biçimi karar olarak belgelenir ve şemada / format notunda yer alır
- [ ] Uygulanamayan hata tanımı hata verir
- [ ] Hiç test düşürmeyen yerleştirilmiş hata hata verir
- [ ] Sessiz hatanın testi exception ile düşerse hata verir
- [ ] Katalogda olmayan hata id'si hata verir
- [ ] Testler: test düşürmeyen hata, exception ile düşen sessiz hata, olmayan katalog id varyantları
