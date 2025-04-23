import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import database
import datetime

def kayit_ekle():
    ad = entry_ad.get()
    soyad = entry_soyad.get()
    dogum_tarihi = entry_dogum.get()
    telefon = entry_telefon.get()
    randevu = entry_randevu.get()

    if not ad or not soyad or not dogum_tarihi or not telefon or not randevu:
        messagebox.showwarning("Eksik Bilgi", "Lütfen tüm alanları doldurun.")
        return

    # Yeni hastayı veritabanına ekle
    database.hasta_ekle(ad, soyad, dogum_tarihi, telefon, randevu)
    messagebox.showinfo("Başarılı", "Kayıt eklendi.")

    # Kaydedilen hastaların randevularını kontrol et
    kayitlar = database.hasta_listesi()
    today = datetime.datetime.today().strftime("%d.%m.%Y")
    
    # Bugün randevusu olan hastaları hatırlat
    randevular_bugun = kayitlar[kayitlar["Randevu Tarihi"] == today]
    if not randevular_bugun.empty:
        for _, satir in randevular_bugun.iterrows():
            ad = satir["Ad"]
            soyad = satir["Soyad"]
            randevu_tarihi = satir["Randevu Tarihi"]
            messagebox.showinfo("Hatırlatma", f"{ad} {soyad}, bugün randevunuz var: {randevu_tarihi}")

    temizle()

def temizle():
    entry_ad.delete(0, tk.END)
    entry_soyad.delete(0, tk.END)
    entry_dogum.delete(0, tk.END)
    entry_telefon.delete(0, tk.END)
    entry_randevu.delete(0, tk.END)

def listele():
    for row in tree.get_children():
        tree.delete(row)

    kayitlar = database.hasta_listesi()
    for _, satir in kayitlar.iterrows():
        tree.insert("", tk.END, values=tuple(satir))

def tarih_filtrele():
    aranan_tarih = entry_tarih_ara.get()
    if not aranan_tarih:
        messagebox.showwarning("Uyarı", "Lütfen bir tarih girin.")
        return

    for row in tree.get_children():
        tree.delete(row)

    kayitlar = database.hasta_listesi()
    filtreli = kayitlar[kayitlar["Randevu Tarihi"] == aranan_tarih]

    if filtreli.empty:
        messagebox.showinfo("Bilgi", f"{aranan_tarih} tarihinde randevu bulunamadı.")
        return

    for _, satir in filtreli.iterrows():
        tree.insert("", tk.END, values=tuple(satir))

# Arayüz
pencere = tk.Tk()
pencere.title("Diş Randevu Sistemi")

# Giriş alanları
tk.Label(pencere, text="Ad").grid(row=0, column=0)
entry_ad = tk.Entry(pencere)
entry_ad.grid(row=0, column=1)

tk.Label(pencere, text="Soyad").grid(row=1, column=0)
entry_soyad = tk.Entry(pencere)
entry_soyad.grid(row=1, column=1)

tk.Label(pencere, text="Doğum Tarihi").grid(row=2, column=0)
entry_dogum = tk.Entry(pencere)
entry_dogum.grid(row=2, column=1)

tk.Label(pencere, text="Telefon").grid(row=3, column=0)
entry_telefon = tk.Entry(pencere)
entry_telefon.grid(row=3, column=1)

tk.Label(pencere, text="Randevu Tarihi (GG.AA.YYYY)").grid(row=4, column=0)
entry_randevu = tk.Entry(pencere)
entry_randevu.grid(row=4, column=1)

tk.Button(pencere, text="Kaydet", command=kayit_ekle).grid(row=5, column=0, pady=10)
tk.Button(pencere, text="Listele", command=listele).grid(row=5, column=1)

# Tarihe göre arama
tk.Label(pencere, text="Tarih Ara (GG.AA.YYYY)").grid(row=6, column=0)
entry_tarih_ara = tk.Entry(pencere)
entry_tarih_ara.grid(row=6, column=1)

tk.Button(pencere, text="Tarihe Göre Ara", command=tarih_filtrele).grid(row=7, column=0, columnspan=2, pady=10)

# Kayıtları listelemek için tablo
tree = ttk.Treeview(pencere, columns=("Ad", "Soyad", "Doğum Tarihi", "Telefon", "Randevu Tarihi"), show="headings")
for col in tree["columns"]:
    tree.heading(col, text=col)
tree.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

pencere.mainloop()
