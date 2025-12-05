import tkinter as tk
import subprocess
import sys
import os

# Fungsi untuk menjalankan file python lain
def run_script(script_name):
    python = sys.executable  # path ke python yang sedang dipakai
    script_path = os.path.join(os.getcwd(), script_name)
    subprocess.Popen([python, script_path])

# --- GUI MENU ---
root = tk.Tk()
root.title("📚 Menu Program Latihan")
root.geometry("400x300")
root.configure(bg="#e8f0fe")

# Judul
judul = tk.Label(root, text="Pilih Program Latihan", 
                 font=("Helvetica", 16, "bold"), bg="#1a73e8", fg="white", pady=10)
judul.pack(fill="x")

frame = tk.Frame(root, bg="white", bd=2, relief="groove")
frame.pack(pady=30, padx=30, fill="both", expand=True)

# Tombol menu
btn1 = tk.Button(frame, text="🧮 Latihan 1 - Operasi Aritmatika Dasar", 
                 font=("Arial", 11, "bold"), bg="#34a853", fg="white",
                 command=lambda: run_script("latihan1.py"), pady=5)
btn1.pack(pady=10, fill="x")

btn2 = tk.Button(frame, text="📟 Latihan 2 - Kalkulator Sederhana", 
                 font=("Arial", 11, "bold"), bg="#fbbc05", fg="black",
                 command=lambda: run_script("latihan2.py"), pady=5)
btn2.pack(pady=10, fill="x")

btn3 = tk.Button(frame, text="📘 Latihan 4 - Form Nilai Akhir Akademik", 
                 font=("Arial", 11, "bold"), bg="#4285f4", fg="white",
                 command=lambda: run_script("latihan4.py"), pady=5)
btn3.pack(pady=10, fill="x")

# Tombol keluar
btn_keluar = tk.Button(root, text="❌ Keluar", font=("Arial", 10, "bold"), 
                       bg="#ea4335", fg="white", command=root.quit)
btn_keluar.pack(pady=10)

root.mainloop()
