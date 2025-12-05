import tkinter as tk
from tkinter import messagebox

def tambah(a, b): 
    return a + b 
def kurang(a, b): 
    return a - b 
def kali(a, b): 
    return a * b 
def bagi(a, b): 
    if b != 0: 
        return a / b 
    else: 
        return None

def hitung():
    try:
        a = float(entry_angka1.get())
        b = float(entry_angka2.get())
        hasil = (f"Penjumlahan: {tambah(a, b)}\n"
                 f"Pengurangan: {kurang(a, b)}\n"
                 f"Perkalian  : {kali(a, b)}\n"
                 f"Pembagian  : {bagi(a, b) if b != 0 else 'Error: Bagi 0'}")
        result.set(hasil)
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# GUI
root = tk.Tk()
root.title("🧮 Latihan 1 - Operasi Aritmatika Dasar")
root.geometry("400x350")
root.configure(bg="#f1f8e9")

tk.Label(root, text="Masukkan Angka Pertama:", bg="#f1f8e9").pack(pady=5)
entry_angka1 = tk.Entry(root, font=("Arial", 11))
entry_angka1.pack(pady=5)

tk.Label(root, text="Masukkan Angka Kedua:", bg="#f1f8e9").pack(pady=5)
entry_angka2 = tk.Entry(root, font=("Arial", 11))
entry_angka2.pack(pady=5)

tk.Button(root, text="Hitung Semua Operasi", font=("Arial", 11, "bold"), 
          bg="#4caf50", fg="white", command=hitung).pack(pady=10)

result = tk.StringVar()
tk.Label(root, textvariable=result, font=("Arial", 12), fg="blue", bg="#f1f8e9", justify="left").pack(pady=10)

tk.Button(root, text="Keluar", font=("Arial", 10, "bold"), bg="#e53935", fg="white", command=root.quit).pack(pady=10)

root.mainloop()
