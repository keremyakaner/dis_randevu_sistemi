Diş Hekimi Randevu ve Hasta Kayıt Sistemi

• Proje Hakkında

Bu Python projesi, Tkinter arayüzü kullanılarak oluşturulmuş bir diş hekimi hasta ve randevu takip sistemidir. Sistem, kullanıcıların hasta bilgilerini kaydetmesini, randevu oluşturmasını ve belirli bir tarihe göre randevuları listelemesini sağlar. Ayrıca, randevu hatırlatmaları yaparak kullanıcıların randevularını unutmamalarını sağlar.




• Kullanılan Teknolojiler

Python

Tkinter (GUI)

Pandas (CSV veritabanı için)

datetime (Tarih işlemleri ve hatırlatmalar için)




• Proje Yapısı

Proje klasörü içinde şu dosyalar bulunur:

main.py # Arayüz ve uygulama mantığı

database.py # Veritabanı işlemleri (CSV ile)

veriler.csv # Hasta ve randevu kayıtları

README.md # Projenin açıklaması (bu dosya)




• Nasıl Çalıştırılır?

Python yüklü değilse, Python'un resmi sitesinden Python'u indirip kurun.

"pip install pandas" komutuyla Pandas kütüphanesini kurun.

Ardından main.py dosyasını çalıştırarak programı başlatın:
python main.py




• Özellikler

Yeni hasta ve randevu kaydı ekleme

Kayıtlı randevuları listeleme

Belirli bir tarihteki randevuları filtreleme (GG/AA/YYYY biçiminde)

Randevu hatırlatmaları (Yarın veya Bugün randevu hatırlatması)

Eksik bilgi uyarısı: Tüm alanların doldurulması gerektiği mesajı




• Not

Veriler veriler.csv dosyasında saklanır. CSV dosyası eksikse, uygulama otomatik olarak oluşturur.




• Ekstra Özellikler

Bugün Randevusu Olan Hastalar: Hasta kaydederken, kaydedilen hastaların bugünkü randevuları varsa, sistem otomatik olarak bu hastalara hatırlatma yapar.

Randevu Hatırlatması: Hasta ekledikçe, eğer randevu tarihi bugün veya yarınsa, sistem kullanıcıyı randevular hakkında bilgilendirir.




• Geliştiren

Kerem Yakaner
Yapay Zeka Operatörlüğü 1. Sınıf Öğrencisi – Karabük Üniversitesi