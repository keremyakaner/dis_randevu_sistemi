# Diş Hekimi Randevu ve Hasta Kayıt Sistemi

## 📋 Proje Hakkında

Bu Python projesi, **Tkinter** arayüzü kullanılarak oluşturulmuş bir **Diş Hekimi Hasta ve Randevu Takip Sistemi**dir.  
Sistem, kullanıcıların hasta bilgilerini kaydetmesini, randevu oluşturmasını ve belirli bir tarihe göre randevuları listelemesini sağlar.  
Ayrıca, randevu hatırlatmaları yaparak kullanıcıların randevularını unutmamalarını destekler.

## 🛠️ Kullanılan Teknolojiler

- Python
- Tkinter (GUI Arayüzü için)
- Pandas (CSV veritabanı yönetimi için)
- datetime (Tarih işlemleri ve hatırlatmalar için)

## 📁 Proje Yapısı

Proje klasöründe şu dosyalar bulunur:

- `main.py` → Arayüz ve uygulama mantığı
- `database.py` → Veritabanı işlemleri (CSV ile veri yönetimi)
- `veriler.csv` → Hasta ve randevu kayıtlarının saklandığı dosya
- `Ekran_Kaydi.mp4` → Projenin örnek videosu
- `README.md` → Proje açıklaması (bu dosya)

## 🚀 Nasıl Çalıştırılır?

1. Python bilgisayarınızda kurulu değilse, [Python'un resmi web sitesinden](https://www.python.org/) indirip yükleyin.
2. Gerekli kütüphaneyi kurmak için terminal veya komut satırında şu komutu çalıştırın:
   ```bash
   pip install pandas

3. Uygulamayı başlatmak için proje klasöründe aşağıdaki komutu yazın:
   ```bash
   python main.py

## ✨ Özellikler

- Yeni hasta ve randevu kaydı ekleme
- Kayıtlı randevuları listeleme
- Belirli bir tarihteki randevuları filtreleme (GG/AA/YYYY biçiminde)
- Randevu hatırlatmaları (Bugün veya yarın olan randevular için)
- Eksik bilgi uyarıları (Tüm alanların doldurulması gerektiğine dair mesaj)

## 🗄️ Notlar

- Tüm veriler `veriler.csv` dosyasında saklanır.
- Eğer CSV dosyası bulunamazsa, uygulama çalıştırıldığında otomatik olarak yeni bir `veriler.csv` dosyası oluşturur.

## 🌟 Ekstra Özellikler

- **Bugün Randevusu Olan Hastalar:** Hasta kaydederken, kaydedilen hastaların bugünkü randevuları varsa, sistem otomatik olarak hatırlatma yapar.
- **Randevu Hatırlatması:** Hasta eklenirken, eğer randevu tarihi bugün veya yarın ise, sistem kullanıcıyı bilgilendirir.

## 👨‍💻 Geliştiren
Kerem Yakaner
Yapay Zeka Operatörlüğü 1. Sınıf Öğrencisi – Karabük Üniversitesi
