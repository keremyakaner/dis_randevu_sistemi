import pandas as pd
import os
import datetime

# Veritabanı dosyasının yolu
veritabani_dosyasi = "veriler.csv"

# Veritabanı dosyası yoksa yeni dosya oluştur
if not os.path.exists(veritabani_dosyasi):
    df = pd.DataFrame(columns=["Ad", "Soyad", "Doğum Tarihi", "Telefon", "Randevu Tarihi"])
    df.to_csv(veritabani_dosyasi, index=False)

def hasta_ekle(ad, soyad, dogum_tarihi, telefon, randevu):
    # Veritabanı dosyasını oku
    df = pd.read_csv(veritabani_dosyasi)

    # Yeni hasta kaydını oluştur
    yeni_kayit = pd.DataFrame([{
        "Ad": ad,
        "Soyad": soyad,
        "Doğum Tarihi": dogum_tarihi,
        "Telefon": telefon,
        "Randevu Tarihi": randevu
    }])

    # Yeni kaydı DataFrame'e ekle
    df = pd.concat([df, yeni_kayit], ignore_index=True)

    # Güncellenmiş veriyi CSV dosyasına kaydet
    df.to_csv(veritabani_dosyasi, index=False)

    # Yeni kaydın ardından tüm hastalar için randevu hatırlatması yap
    randevu_hatırlat(ad, soyad, randevu)

def hasta_listesi():
    # Veritabanı dosyasını oku
    df = pd.read_csv(veritabani_dosyasi)
    return df

def randevu_hatırlat(ad, soyad, randevu_tarihi):
    try:
        randevu_date = datetime.datetime.strptime(randevu_tarihi, "%d.%m.%Y")
        today = datetime.datetime.today()
        difference = randevu_date - today

        # Eğer randevu yarınsa veya bugüne yakınsa hatırlatma yap
        if difference.days == 1:
            print(f"{ad} {soyad}, yarın randevunuz var: {randevu_tarihi}")
        elif difference.days == 0:
            print(f"{ad} {soyad}, bugün randevunuz var: {randevu_tarihi}")
    except ValueError:
        print("Geçersiz tarih formatı, lütfen GG.AA.YYYY formatında girin.")
