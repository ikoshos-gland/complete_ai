# complete_ai

Tek bir öğrenenin, 3 ayda, orta düzeyden frontier-lab Research Engineer mülakatlarını geçecek düzeye çıkması için tasarlanan yoğun ML/AI programı.

## Language

**Öğrenen**:
Programın tek kullanıcısı (Mert). Program onun seviyesine ve zayıf noktalarına göre ayarlanır.
_Avoid_: öğrenci, kullanıcı, kitle

**Hedef rol**:
Frontier lab Research Engineer, biyoinformatik (biyolojik veri için ML) uzantısıyla. Soruların zorluk çıtası bu role göre belirlenir.
_Avoid_: ML engineer, data scientist

**Program**:
3 ay, günde ~5 saat süren, bir lisans bölümü gibi kurgulanmış öğrenme yolunun tamamı.
_Avoid_: kurs, müfredat (müfredat programın içeriğidir, kendisi değil)

**Başlangıç seviyesi**:
Programın varsaydığı orta-ileri düzey. Seviye tespit sınavı yapılmaz; eksik kalan temel konular Hoca'dan istenerek kapatılır.

**Kod perspektifi**:
Bir konuyu sıfırdan kodlayabilmek (öncelikle JAX) ve hatalı ML kodunu debug edebilmek.

**Görsel perspektif**:
Bir konuyu interaktif görsel/video ile sezgisel kavramak ve mülakatta çizerek anlatabilmek.

## Program yapısı

**Dönem**:
Programın 4 haftalık bölümü. Program 3 dönemden oluşur.

**Ders**:
Bir dönem boyunca paralel yürüyen konu hattı (ör. LLM'ler, Sistemler, Bio-ML, Algoritmalar). Bir ders tek bir dönemin içinde başlar ve biter; iki döneme yayılan konular "I / II / III" diye ayrı derslere bölünür.
_Avoid_: modül, kurs

**Ünite**:
Bir dersin, tek oturumda bitirilebilen 2–3 saatlik birimi. Bir günde yaklaşık iki ünite çalışılır.
_Avoid_: modül, ders (ders, ünitelerden oluşan dönemlik hattır)

**Proje ünitesi**:
Bio-ML dersinde öğrenenin kendi projelerinden birini işleyen ünite. Normal ünite döngüsünü izler; seçilmiş videonun yerine öğrenenin proje raporu gelir.
_Avoid_: proje dersi, vaka ünitesi

**Soğuk deneme**:
Ünitenin başında, konu öğrenilmeden önce bir soruya verilen kısa yazılı cevap. Puanlanmaz; ünite sonunda son cevapla karşılaştırılır.
_Avoid_: ön test, seviye tespit

**Pratik görev**:
Ünitedeki tek elle yapılan iş: Implement ya da Debug, kod çıkmayan ünitelerde Derivation.
_Avoid_: ödev (ödev haftalık değerlendirmedir)

**Hata kaydı**:
Ünite sonunda öğrenenin takıldığı noktaların tek satırlık listesi; Hoca'nın tekrar planına girdi olur.
_Avoid_: not, günlük

**Final haftası**:
Üç dönemden sonra gelen 13. hafta. Final mock mülakatları ve son tampon burada yer alır; hiçbir dönemin parçası değildir.

**Ünite günü**:
Haftanın 1–6. günleri: tekrar bloğu, algoritma bloğu ve iki farklı dersten birer ünite.

**Hafif gün**:
Haftanın 7. günü. Yeni ünite yoktur: tekrar, algoritma bloğu, haftalık ödev (dönemin son haftasında ara sınav) ve hafta kapanışı.
_Avoid_: tatil, boş gün

**Algoritma bloğu**:
Her günün tekrar bloğundan sonra gelen ~30 dakikalık, tek problemlik Algorithms çalışması. Ünite değildir, ünite döngüsünü kullanmaz.
_Avoid_: algoritma ünitesi

**Kılıklı problem**:
ML ya da biyoloji bağlamında sorulan, ama çözmek için o alanın bilgisini gerektirmeyen algoritma problemi (ör. heap ile top-k, sequence alignment DP). Practical Coding × Algorithms sorusudur, algoritma bloğunda çalışılır. Alan bilgisi gerekiyorsa problem ML Coding sorusudur, kılıklı problem değildir.
_Avoid_: ML algoritma sorusu, hibrit soru

**Hafta kapanışı**:
Hafif günün sonundaki ~1 saat: kaymanın kapatılması ve haftanın hata kaydına toplu bakış.

**Harmanlama**:
Bir günün iki ünitesinin iki farklı dersten gelmesi.
_Avoid_: karışık çalışma

**Dönem planı**:
Bir dönemin hafta × gün → ünite takvimi. Önceden yazılır; günün planı ondan ve ilerlemeden çıkar.
_Avoid_: müfredat, ders programı

**Kayma**:
Dönem planının gerisinde kalınan ünitelerin birikimi. Plan kayar; kayma hafta kapanışında, dönem rezervinde, en son program geneli kayma tamponunda kapatılır.
_Avoid_: gecikme, borç

**Rezerv**:
Program saatinin derslere dağıtılmayan kısmı: ara sınavlar, Final haftası ve kayma tamponu. Tekrar bloğu rezervden değil, ders saatinden sayılır.
_Avoid_: boş zaman

**Sınav**:
Öğretmek için yapılan değerlendirme (ara sınav, final mock mülakat). Başarı ölçütü değil, eksik bulma ve pekiştirme aracı.
_Avoid_: başarı testi, sertifikasyon

**Haftalık ödev**:
Hafif günde yapılan ~3 saatlik değerlendirme: haftanın konularını bağlayan bir birleşik görev ve takip zinciriyle cevaplanan birkaç banka sorusu.
_Avoid_: pratik görev (pratik görev ünitenin içindedir)

**Birleşik görev**:
Haftalık ödevin kod kısmı. Haftanın birkaç konusunu tek bir testli işte birleştirir. CS336 haftalarında yerini CS336 ödevinin bir dilimi alır.

**Ara sınav**:
D1 ve D2'nin son hafif gününde yapılan, o dönemin turlarından oluşan üç mock mülakat turu.
_Avoid_: dönem sonu sınavı

**Loop**:
Final haftasında bir güne yerleştirilmiş, gerçek bir onsite mülakat gününü taklit eden üç mock turluk dizi.

**Sınav havuzu**:
Bankada yalnızca ara sınav ve Final haftasına ayrılmış sorular. Ünitede, tekrarda ve `/soru`'da kullanılmazlar; böylece öğrenen onları sınavda ilk kez görür.
_Avoid_: gizli sorular, test seti

**İçerik**:
İçerik üretiminde önceden yazılıp doğrulanan program malzemesi: banka, üniteler, dönem planları, ödevler, sınavlar, videolar. Öğrenme sırasında değişmez; Hoca yalnızca okur.
_Avoid_: materyal, kaynak (kaynak bir sorunun türetildiği dış eserdir)

**Kayıt**:
Öğrenme sırasında yalnızca Hoca'nın yazdığı durum: ilerleme, hata kaydı, tekrar durumu, mock dökümleri, sınav raporları.
_Avoid_: log, durum dosyası

**Çalışma alanı**:
Öğrenenin bir banka sorusunun (ya da ödev/sınavın) kopyası üzerinde çalıştığı yer. Asıl banka sorusu hiç değişmez; denemeler burada birikir.
_Avoid_: sandbox, workspace

**Sınav raporu**:
Ara sınavın tur başına rubrik özeti. Hoca sonraki dönemde zayıf alanlara ağırlık verirken bu rapora bakar.

**Seçilmiş video**:
Dış kaynaktan (3Blue1Brown, Karpathy, Stanford vb.) bir derse bağlanan video.

**Üretilmiş video**:
Program için üretilen animasyon videosu (Manim tarzı). Önceden hazırlanmaz; öğrenen istediğinde, takıldığı kavram için üretilir.

**Hoca**:
Claude'un program içindeki öğretme rolü: önceden üretilmiş içeriği yürütür, ders anlatır, istendiğinde konuyu sıfırdan açıklar, mock mülakat yapar, ödevleri değerlendirir, ilerlemeyi takip eder. Dilim üretmez; bunu Üretici yapar.
_Avoid_: asistan, bot

**Tekrar bloğu**:
Her günün başında yapılan ~30 dakikalık aralıklı tekrar oturumu. Zamanı gelmiş tekrar kartları burada çalışılır.
_Avoid_: revizyon, gözden geçirme

**Tekrar kartı**:
Tekrar takviminde yer alan tek bir öğe: ya üzerinde çalışılmış bir banka sorusu ya da bir hata kartı.
_Avoid_: flashcard, kart (yalnız başına)

**Hata kartı**:
Hata kaydındaki bir satırdan doğan tekrar kartı. Satır bir banka sorusuna bağlanabiliyorsa o soruya bağlanır, bağlanamıyorsa Hoca satırdan tek bir mini soru üretir.
_Avoid_: hata notu

**Mock mülakat**:
Hoca'nın mülakatçı moduna geçtiği, gerçek tur süresinde ve ipucu vermeden yürüyen mülakat provası. Sonunda rubrik değerlendirme yapılır, ardından öğretmen moduna dönülür. Ara sınav ve Final haftası bu provalardan kurulur.
_Avoid_: deneme mülakatı, simülasyon

**Mülakatçı modu / Öğretmen modu**:
Hoca'nın iki duruşu. Mülakatçı modunda açıklama yapmaz ve yalnızca değerlendirir. Öğretmen modunda anlatır, hataları açar ve hata kaydına yazar.

## Soru bankası

**Alan**:
Bir sorunun ait olduğu bilgi alanı (8 değer: Math, Classical ML, DL Foundations, Transformers & LLMs, ML Systems & Distributed Training, ML System Design, Algorithms, Bio-ML). Derslerden bağımsızdır; bir ders birden çok alana dokunabilir.
_Avoid_: konu, ders (ders programın yapısıdır, alan bilginin)

**Format**:
Sorunun öğrenenden istediği bilişsel görev (Conceptual, Derivation, Implement, Debug, Estimation, Design, Whiteboard, Paper Discussion).
_Avoid_: soru tipi, tür

**Zorluk**:
Hedef role göre tanımlı üç seviye: L1 Warm-up (bilmemek eleyici), L2 Standard (tipik ana soru), L3 Frontier (takip zincirinin en derini; yalnızca makalenin Methods/Supplement kısmında bulunan bir ayrıntı ya da tek bir ders kitabı cevabı olmayan gerekçeli bir trade-off, varsayım veya başarısızlık analizi). Kaynakların kendi zorluk etiketleri bu ölçeğe çevrilmez, yeniden etiketlenir.

**Tur**:
Sorunun mülakatta geldiği oturum (Practical Coding, ML Coding, ML Debugging, ML Depth, System Design, Research Discussion). Her tur yalnızca belirli formatlara izin verir.
_Avoid_: round, aşama

**Alt konu**:
Bir alanın altındaki, kontrollü listeden seçilen konu. Yeni alt konu yalnızca bilinçli kararla eklenir; serbest kavramlar anahtar kelime olarak tutulur.
_Avoid_: etiket, başlık

**Takip zinciri**:
Bir sorunun ardından, cevaba göre sırayla açılan ve giderek derinleşen alt sorular. En derin halka genelde L3'tür.
_Avoid_: follow-up listesi, ek sorular

**İlgili alan**:
Bir sorunun ait olmadığı ama dokunduğu ikincil alan (en fazla 2). Alan sayımlarına girmez.

**Halka puanı**:
Takip zincirinin her halkasına verilen 0–2 puan (0 bilmiyor, 1 kısmi, 2 mülakatta geçer). 0 alınan halkada zincir durur. Bir sorunun sonucu, ulaşılan en derin halkadır.

**Banka sorusu**:
Soru bankasındaki, değişmez bir id'si olan ve doğrulanmış tek soru. Ünitelerin pratik görevleri de banka sorusudur; üniteler, tekrar ve mock mülakat ona id ile başvurur.
_Avoid_: kart (kart tekrar takvimindeki öğedir)

**Model cevap**:
Bir banka sorusunun ve takip zincirinin her halkasının beklenen cevabı. Halka halka ayrı yazılır, böylece kırılan halkanın cevabı tek başına açılabilir.
_Avoid_: çözüm (çözüm, kodlu sorulardaki referans koddur)

**Hedef halka**:
Bir sorunun tekrarda "geçti" sayılması için ulaşılması gereken halka. Varsayılanı son halkadır; son halka bonus L3 ise daha önceki bir halka seçilir.

**Köken**:
Bir banka sorusunun nereden geldiği: hazır bir sorudan kendi cümlelerimizle yeniden yazılmış, bir makale, repo ya da kitaptan türetilmiş ya da özgün.
_Avoid_: kaynak (kaynak, kökenin işaret ettiği belgedir)

**Öğrenen projesi**:
Öğrenenin kendi yürüttüğü araştırma işi (KIF13A atlası, AcRLSD, pdnph-bench). Proje soruları ve proje üniteleri bu işleri tartışır; belgelerinin dondurulmuş kopyaları kaynak listesinde çapa olarak yer alır.
_Avoid_: kişisel proje, portfolyo

**Proje derin dalışı**:
Mülakatçının öğrenen projelerinden birini seçip yöntem, alternatifler ve sınırlamalar üzerinden en derin halkaya kadar zorladığı Research Discussion turu.
_Avoid_: project deep dive (İngilizce kullanım yalnızca mülakat provasında), Behavioral

**Mini soru**:
Hata kartı bir banka sorusuna bağlanamadığında Hoca'nın hata kaydı satırından ürettiği tek soru. Bankaya girmez, kartın içinde yaşar; iyi çıkarsa bilinçli bir kararla bankaya alınabilir.

## İçerik üretimi

**Dilim**:
Öğrenene tek seferde açılan bir haftalık içerik: o haftanın üniteleri, algoritma problemleri, ödevi ya da ara sınavı ve bunların istediği banka soruları.
_Avoid_: parti, paket (paket dönem başında üretilir)

**Dönem paketi**:
Bir dönem başlamadan önce bir kerede üretilen içerik: dönem planı, CS336 ödev dilimlemesi ve o dönemin sınav havuzu.
_Avoid_: dönem dilimi

**Kalite kapısı**:
Bir dilimin ya da dönem paketinin öğrenene açılmadan önce geçmesi gereken otomatik kontroller ve ayrı bir doğrulayıcı ajanın teknik denetimi. Öğrenen içeriği önceden onaylamaz.
_Avoid_: onay, review

**Üretici**:
Dilimleri ve dönem paketlerini üreten, Hoca'dan ayrı rol. Hoca içeriği yürütür, Üretici yazar.
_Avoid_: Hoca (Hoca üretim yapmaz; yalnızca /sifirdan ve /video'yu anında üretir)

**Çapa kaynak**:
Türetilmiş bir banka sorusunun dayandığı belirli yer: makale bölümü, kitap bölümü, repo dosyası ya da olay raporu. Çapasız türetme yapılmaz.
_Avoid_: referans, ilham

**Kaynak listesi**:
Alan başına sabit tutulan, çapa kaynakların seçilebileceği belgeler listesi. Listeye ekleme bilinçli bir karardır ve dönem paketinde gözden geçirilir.
_Avoid_: okuma listesi (okuma listesi öğrenene yöneliktir)

**Hata kataloğu**:
Debug görevlerine enjekte edilebilecek hata türlerinin id'li sabit listesi (ör. softmax ekseni, PRNG key tekrarı). Her madde gerçek bir olaya ya da issue'ya çapalanır.
_Avoid_: bug listesi

**Sessiz hata**:
Çökme üretmeyen, yalnızca loss'u ya da metriği yanlış çıkaran hata. Her Debug görevinde en az bir tane bulunur.
_Avoid_: mantık hatası
