def substitusi_cipher(plaintext, aturan):
    """
    Melakukan substitusi karakter pada plaintext berdasarkan aturan yang diberikan.
    Semua input diubah menjadi huruf kapital untuk konsistensi.
    """
    ciphertext = ''
    # Pastikan plaintext diubah ke huruf kapital agar sesuai dengan aturan
    # yang diinputkan pengguna (yang juga kita paksa jadi kapital)
    plaintext_upper = plaintext.upper()

    for char in plaintext_upper:
        if char in aturan:
            # Jika karakter ada dalam aturan, substitusikan
            ciphertext += aturan[char]
        else:
            # Jika tidak ada dalam aturan, biarkan karakter asli
            ciphertext += char
            
    return ciphertext

def input_aturan_substitusi():
    """
    Meminta input aturan substitusi dari pengguna.
    Pengguna memasukkan pasangan 'Asli:Pengganti' sampai mengetik 'selesai'.
    """
    aturan = {}
    print("\n--- Input Aturan Substitusi (Ketik 'selesai' untuk mengakhiri) ---")
    
    while True:
        try:
            # Contoh format input: U=K, N=N, A=B
            input_line = input("Masukkan Aturan (e.g., A=B) atau 'selesai': ").strip()
            
            if input_line.lower() == 'selesai':
                break
            
            if '=' not in input_line or len(input_line) < 3:
                print("[Peringatan] Format tidak valid. Gunakan format 'Asli=Pengganti'.")
                continue
            
            # Memecah input menjadi karakter asli dan karakter pengganti
            asli, pengganti = input_line.split('=', 1)
            
            asli = asli.strip().upper()
            pengganti = pengganti.strip().upper()
            
            if len(asli) != 1 or len(pengganti) != 1:
                 print("[Peringatan] Hanya boleh 1 karakter untuk Asli dan 1 karakter untuk Pengganti.")
                 continue

            aturan[asli] = pengganti
            print(f"   [Aturan ditambahkan] {asli} akan dienkripsi menjadi {pengganti}")

        except Exception as e:
            print(f"[Error] Terjadi kesalahan saat memproses input: {e}")
            
    return aturan

# --- Program Utama ---

# 1. Input Plaintext
plaintext = input("Masukkan plaintext (pesan asli) yang akan dienkripsi: ").strip()

# 2. Input Aturan Substitusi
aturan_substitusi = input_aturan_substitusi()

# 3. Proses Enkripsi
if not aturan_substitusi:
    print("\nTidak ada aturan substitusi yang dimasukkan. Enkripsi dibatalkan.")
else:
    ciphertext = substitusi_cipher(plaintext, aturan_substitusi)

    # 4. Tampilkan Hasil
    print("\n================ HASIL ENKRIPSI ================")
    print(f"Plaintext Asli (Huruf Kapital): {plaintext.upper()}")
    print(f"Aturan Digunakan: {aturan_substitusi}")
    print(f"Ciphertext: {ciphertext}")
    print("================================================")
