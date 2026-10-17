
import tkinter as tk
from tkinter import messagebox

# Ana pencereyi oluştur
pencere = tk.Tk()
pencere.title("Kişisel Bilgi Formu")
pencere.geometry("400x300")

# İsim etiketi
isim_etiketi = tk.Label(pencere, text="Adınızı girin:")
isim_etiketi.pack(pady=5)

# İsim giriş kutusu
isim_kutusu = tk.Entry(pencere)
isim_kutusu.pack(pady=5)


# Butona basılınca çalışacak fonksiyon
def bilgileri_goster():
    isim = isim_kutusu.get().strip()

    if isim:
        sonuc_etiketi.config(text=f"Merhaba, {isim}!")
    else:
        messagebox.showwarning(
            "Eksik Bilgi",
            "Lütfen adınızı girin."
        )


# Bilgileri göster butonu
bilgi_butonu = tk.Button(
    pencere,
    text="Bilgileri Göster",
    command=bilgileri_goster
)
bilgi_butonu.pack(pady=15)

# Sonuç etiketi
sonuc_etiketi = tk.Label(pencere, text="")
sonuc_etiketi.pack(pady=5)

# Pencereyi çalıştır
pencere.mainloop()


