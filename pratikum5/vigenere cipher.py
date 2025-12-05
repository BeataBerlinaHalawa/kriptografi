# =====================================================
# Program GUI: Implementasi Vigenère Cipher
# Fitur: Enkripsi & Dekripsi + Detail Proses
# Desain GUI sederhana dengan Tkinter
# =====================================================

import tkinter as tk
from tkinter import ttk, messagebox

# ------------------------------
# Fungsi untuk membuat kunci sepanjang teks
# ------------------------------
def generate_key(text, key):
    key = list(key.upper())
    if len(text) == len(key):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)

# ------------------------------
# Fungsi Enkripsi
# ------------------------------
def vigenere_encrypt(plain_text, key):
    cipher_text = ""
    detail = []
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            p = ord(plain_text[i].upper()) - 65
            k = ord(key[i].upper()) - 65
            c = (p + k) % 26
            cipher_char = chr(c + 65)
            cipher_text += cipher_char
            detail.append(f"{i+1:03d}. {plain_text[i]} + {key[i]} → ({p}+{k})%26={c} → {cipher_char}")
        else:
            cipher_text += plain_text[i]
            detail.append(f"{i+1:03d}. {plain_text[i]} (bukan huruf, tidak berubah)")
    return cipher_text, detail

# ------------------------------
# Fungsi Dekripsi
# ------------------------------
def vigenere_decrypt(cipher_text, key):
    plain_text = ""
    detail = []
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            c = ord(cipher_text[i].upper()) - 65
            k = ord(key[i].upper()) - 65
            p = (c - k + 26) % 26
            plain_char = chr(p + 65)
            plain_text += plain_char
            detail.append(f"{i+1:03d}. {cipher_text[i]} - {key[i]} → ({c}-{k})%26={p} → {plain_char}")
        else:
            plain_text += cipher_text[i]
            detail.append(f"{i+1:03d}. {cipher_text[i]} (bukan huruf, tidak berubah)")
    return plain_text, detail

# ------------------------------
# Tombol Proses Enkripsi / Dekripsi
# ------------------------------
def proses(mode):
    text = entry_text.get().strip()
    key = entry_key.get().strip()

    if not text or not key:
        messagebox.showwarning("Peringatan", "Isi teks dan kunci terlebih dahulu!")
        return

    key_full = generate_key(text, key)

    if mode == "encrypt":
        hasil, detail = vigenere_encrypt(text, key_full)
        label_hasil.config(text="Hasil Enkripsi:")
    else:
        hasil, detail = vigenere_decrypt(text, key_full)
        label_hasil.config(text="Hasil Dekripsi:")

    text_output.delete(1.0, tk.END)
    text_output.insert(tk.END, f"Teks Asli/Kunci Dipanjang:\n{key_full}\n\n")
    text_output.insert(tk.END, "=== DETAIL PROSES ===\n")
    for d in detail:
        text_output.insert(tk.END, d + "\n")
    text_output.insert(tk.END, "\n=== HASIL AKHIR ===\n")
    text_output.insert(tk.END, hasil)

# ------------------------------
# DESAIN GUI
# ------------------------------
root = tk.Tk()
root.title("🔐 Program Vigenère Cipher")
root.geometry("800x600")
root.config(bg="#E8F0FE")

title = tk.Label(root, text="IMPLEMENTASI VIGENÈRE CIPHER", font=("Segoe UI", 16, "bold"), bg="#E8F0FE")
title.pack(pady=10)

frame_input = tk.Frame(root, bg="#E8F0FE")
frame_input.pack(pady=10)

tk.Label(frame_input, text="Masukkan Teks:", font=("Segoe UI", 11), bg="#E8F0FE").grid(row=0, column=0, sticky="w", padx=5)
entry_text = tk.Entry(frame_input, width=60, font=("Consolas", 11))
entry_text.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Masukkan Kunci:", font=("Segoe UI", 11), bg="#E8F0FE").grid(row=1, column=0, sticky="w", padx=5)
entry_key = tk.Entry(frame_input, width=60, font=("Consolas", 11))
entry_key.grid(row=1, column=1, padx=5, pady=5)

frame_button = tk.Frame(root, bg="#E8F0FE")
frame_button.pack(pady=10)

btn_encrypt = ttk.Button(frame_button, text="🔒 Enkripsi", command=lambda: proses("encrypt"))
btn_encrypt.grid(row=0, column=0, padx=10)

btn_decrypt = ttk.Button(frame_button, text="🔓 Dekripsi", command=lambda: proses("decrypt"))
btn_decrypt.grid(row=0, column=1, padx=10)

label_hasil = tk.Label(root, text="Hasil:", font=("Segoe UI", 12, "bold"), bg="#E8F0FE")
label_hasil.pack(pady=5)

frame_output = tk.Frame(root, bg="#E8F0FE")
frame_output.pack(fill="both", expand=True, padx=20, pady=10)

text_output = tk.Text(frame_output, wrap="word", height=20, width=90, font=("Consolas", 10))
text_output.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_output, command=text_output.yview)
scrollbar.pack(side="right", fill="y")
text_output.config(yscrollcommand=scrollbar.set)

footer = tk.Label(root, text="© 2025 - Implementasi Vigenère Cipher | By Beata Berlina", font=("Segoe UI", 9), bg="#E8F0FE")
footer.pack(pady=5)

root.mainloop()
