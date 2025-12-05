import tkinter as tk
from tkinter import messagebox

# --- Fungsi ---
def hitung_nilai_akhir(sikap, tugas, uts, uas):
    total = (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)
    return total

def tentukan_grade(nilai):
    if 81 <= nilai <= 100:
        return "A", 4
    elif 76 <= nilai <= 80:
        return "B+", 3.5
    elif 71 <= nilai <= 75:
        return "B", 3
    elif 66 <= nilai <= 70:
        return "C+", 2.5
    elif 56 <= nilai <= 65:
        return "C", 2
    elif 46 <= nilai <= 55:
        return "D", 1
    else:
        return "E", 0

def proses_hitung():
    try:
        sikap = float(entry_sikap.get())
        tugas = float(entry_tugas.get())
        uts = float(entry_uts.get())
        uas = float(entry_uas.get())

        total = hitung_nilai_akhir(sikap, tugas, uts, uas)
        grade, bobot = tentukan_grade(total)
        status = "Lulus ✅" if total >= 56 else "Tidak Lulus ❌"

        hasil.set(f"Total Nilai : {total:.2f}\nGrade : {grade} (Bobot {bobot})\nKeterangan : {status}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

# --- GUI ---
root = tk.Tk()
root.title("📘 Form Hitung Nilai Akhir Akademik")
root.geometry("500x500")
root.configure(bg="#e8f0fe")  # background biru muda

# Judul
judul = tk.Label(root, text="Form Hitung Nilai Akhir Akademik", 
                 font=("Helvetica", 16, "bold"), bg="#1a73e8", fg="white", pady=10)
judul.pack(fill="x")

# Frame utama
frame = tk.Frame(root, bg="white", bd=2, relief="groove")
frame.pack(pady=20, padx=20, fill="both", expand=True)

# Input fields
tk.Label(frame, text="Nilai Sikap/Kehadiran (0-100):", font=("Arial", 11), bg="white").pack(pady=5, anchor="w")
entry_sikap = tk.Entry(frame, font=("Arial", 11))
entry_sikap.pack(pady=5, fill="x")

tk.Label(frame, text="Nilai Tugas (0-100):", font=("Arial", 11), bg="white").pack(pady=5, anchor="w")
entry_tugas = tk.Entry(frame, font=("Arial", 11))
entry_tugas.pack(pady=5, fill="x")

tk.Label(frame, text="Nilai UTS (0-100):", font=("Arial", 11), bg="white").pack(pady=5, anchor="w")
entry_uts = tk.Entry(frame, font=("Arial", 11))
entry_uts.pack(pady=5, fill="x")

tk.Label(frame, text="Nilai UAS (0-100):", font=("Arial", 11), bg="white").pack(pady=5, anchor="w")
entry_uas = tk.Entry(frame, font=("Arial", 11))
entry_uas.pack(pady=5, fill="x")

# Tombol Hitung
btn_hitung = tk.Button(frame, text="⚡ Hitung Nilai Akhir", 
                       font=("Arial", 12, "bold"), bg="#34a853", fg="white", 
                       activebackground="#0f9d58", activeforeground="white", 
                       command=proses_hitung, padx=10, pady=5)
btn_hitung.pack(pady=15)

# Label hasil
hasil = tk.StringVar()
tk.Label(frame, textvariable=hasil, font=("Arial", 12, "bold"), fg="#1a73e8", bg="white", justify="left").pack(pady=10)

# Tombol Keluar
btn_keluar = tk.Button(root, text="❌ Keluar", font=("Arial", 10, "bold"), 
                       bg="#ea4335", fg="white", command=root.quit)
btn_keluar.pack(pady=10)

root.mainloop()
