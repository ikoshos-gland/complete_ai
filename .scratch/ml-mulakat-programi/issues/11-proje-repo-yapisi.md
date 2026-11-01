# Proje repo yapısı

Type: grilling
Status: resolved
Blocked by: 09, 10
Map: ../map.md

## Question

Program repo'sunun klasör yapısı nedir? Her parça nerede duracak:
- dersler ve ünite dosyaları (README, notebook'lar),
- `banka/` (iç düzeni **Soru bankası fiziksel formatı** kararında sabit),
- ünitenin kodlu görevleri kopyaladığı çalışma alanı,
- seçilmiş video bağlantıları ve üretilmiş videolar (Manim kaynağı + render),
- Hoca skill'leri ve slash komutları,
- durum dosyaları: ilerleme, hata kaydı, tekrar YAML'ı,
- `/gun`'un okuduğu dönem/hafta planı,
- ödev ve sınav dosyaları, ara sınav sonrası yazılan sınav raporu.

Python ortamı tek mi olacak (uv, JAX + PyTorch + NumPy), yoksa ayrı ortamlar mı? Git geçmişinde durum dosyaları nasıl tutulacak? Çalışma alanındaki kopyalar commit'lenecek mi?

## Answer

**Ayrı repo**: Program kendi git reposunda yaşar (ör. `~/Claude/ml-program/`). `complete_ai` yalnızca planlama reposu olarak kalır (harita, spec). Yeni repo içerik üretimine başlangıç noktası olarak devredilir.

**Üç grup**:
- **İçerik**: içerik üretiminde yazılır, öğrenme sırasında değişmez, Hoca yalnızca okur.
- **Kayıt**: yalnızca Hoca yazar.
- **Çalışma alanı**: öğrenenin kopyaları.

Öğrenme sırasında yapılan her değişiklik ya `kayit/`'a ya da `calisma/`'ya yazılır.

```
ml-program/
  CLAUDE.md                   Hoca kişiliği, dil kuralları, dosya haritası
  .claude/skills/
    gun/ unite/ sifirdan/ soru/ degerlendir/ video/ mock/   (komut başına bir skill)
    <ortak referans klasörü>/  takip zinciri puanlaması, hata kaydı satır biçimi,
                               tekrar kuralları, dosya haritası
  pyproject.toml, uv.lock
  banka/                      iç düzen: Soru bankası fiziksel formatı kararı
  dersler/<ders-kodu>/<NN>-<slug>/   README.md (ünite sayfası), notebook'lar
  plan/D1.yaml D2.yaml D3.yaml final.yaml   dönem planları (/gun okur)
  odevler/D1-H1/              birleşik görev + soru listesi
  sinavlar/ara-D1/ ara-D2/ final/
  videolar/
    secilmis.yaml             seçilmiş video kataloğu
    uretilmis/<kavram>/       sahne.py, seslendirme metni, render/ (gitignore)
  calisma/
    <unite-id>/<banka-id>/
    odev-D1-H1/  ara-D1/
  kayit/
    ilerleme.md
    hata-kaydi.md
    tekrar.yaml
    mock/<tarih>-<tur>.md     mock dökümü + rubrik
    sinav-raporlari/ara-D1.md
```

**Hoca komutları**: 7 komutun her biri ayrı bir skill'dir. Ortak protokoller tek bir referans klasöründe tutulur ve skill'ler bunlara adıyla başvurur, böylece hiçbir kural kopyalanmaz. Kişilik ve dil kuralları kökteki `CLAUDE.md`'de durur.

**Ünite id'si**: Klasör yolu `dersler/<ders-kodu>/<NN>-<slug>/` biçimindedir (ör. `dersler/llm1/04-attention/`). Kısa id `llm1-04` değişmez. Dönem planı, ilerleme dosyası ve çalışma alanı üniteye bu id ile başvurur. Ünite README'si pratik görevi ve soruları banka id'siyle anar, kopyalamaz.

**Seçilmiş videolar**: Hepsi tek bir katalogda, `videolar/secilmis.yaml` dosyasında tutulur. Her kayıt şunları içerir: id, URL, başlangıç–bitiş zaman damgası, karşıladığı alt konu(lar). Üniteler videolara id ile başvurur. `/video`'nun "bunu karşılayan seçilmiş video var mı" kontrolü bu kataloğu tarar.

**Üretilmiş videolar**: Her video `videolar/uretilmis/<kavram>/` altında durur. Manim kaynağı (`sahne.py`) ve seslendirme metni commit'lenir. `.mp4` render'ları `.gitignore`'a girer. Manim sürümü sabit olduğu için video kaynaktan yeniden render edilebilir. Git LFS kullanılmaz.

**Çalışma alanı**: Ünite görevleri `calisma/<unite-id>/<banka-id>/` altına kopyalanır. Ödevler `calisma/odev-D1-H1/`, sınavlar `calisma/ara-D1/` gibi klasörlere gider. Çalışma alanı commit'lenir. Böylece her deneme ve `/degerlendir`'in neye puan verdiği git geçmişinde kalır.

**Git**: Hoca günü kapatırken `kayit/` ve `calisma/` değişikliklerini tek bir otomatik commit'le kaydeder. Commit mesajı `D1-H2-G3` biçimindedir. Push otomatik yapılmaz. Bir kayıt dosyası bozulursa önceki güne dönülür.

**Python ortamı**: Tek bir uv projesi vardır. Varsayılan kurulum JAX, PyTorch, NumPy ve pytest'in CPU sürümleridir. İki ek dependency group bulunur:
- `video`: Manim ve Cairo/Pango bağımlılıkları.
- `gpu`: rig'deki tek 3090 için CUDA'lı JAX ve PyTorch.

Sözlük güncellendi: içerik, kayıt, çalışma alanı.
