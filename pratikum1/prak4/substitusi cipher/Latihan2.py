import math
from collections import Counter

# --- ATURAN SUBSTITUSI ---
ATURAN_SUBSTITUSI = {
    'U': 'X', 'N': 'Y', 'I': 'Z', 'K': 'W', 'A': 'B',
    'S': 'C', 'T': 'D', 'O': 'E', 'H': 'F', 'M': 'G'
    # Spasi dan karakter lain di luar ini akan tetap sama
}

def substitusi_cipher(plaintext, aturan):
    """Melakukan Substitusi Cipher."""
    ciphertext = ''
    # Pastikan plaintext diubah ke huruf kapital
    plaintext_upper = plaintext.upper()
    
    for char in plaintext_upper:
        # Menggunakan .get() agar karakter yang tidak ada dalam aturan (seperti spasi) tetap char asli
        ciphertext += aturan.get(char, char)
            
    return ciphertext

def transposisi_cipher(plaintext, n_kolom=4):
    """
    Melakukan Transposisi Cipher Kolom dengan n_kolom yang ditentukan.
    (Sama seperti kode yang kita analisis sebelumnya)
    """
    n = len(plaintext)
    part_length = n // n_kolom
    
    # Membagi plaintext menjadi bagian-bagian (part/baris)
    parts = [plaintext[i:i + part_length] for i in range(0, n, part_length)]
    
    ciphertext = ""
    
    # Membaca Ciphertext secara Kolom
    for col in range(n_kolom):
        for part in parts:
            if col < len(part):
                ciphertext += part[col]
                
    return ciphertext

def proses_enkripsi_lengkap(plaintext):
    
    # --- a. Input Plaintext ---
    P = plaintext.upper()
    print(f"a. Input Plaintext (P): {P}")
    
    # --- b. Proses Substitusi Cipher ---
    C1 = substitusi_cipher(P, ATURAN_SUBSTITUSI)
    print("\n   --- Proses Substitusi ---")
    print(f"   Ciphertext Substitusi (C1): {C1}")
    
    # --- b. Proses Transposisi Cipher ---
    N_KOLOM = 4
    C2 = transposisi_cipher(C1, N_KOLOM)
    
    # Menampilkan detail Transposisi
    n_part = len(C1) // N_KOLOM
    parts = [C1[i:i + n_part] for i in range(0, len(C1), n_part)]
    print(f"\n   --- Proses Transposisi ({len(C1)} karakter, {N_KOLOM} kolom, panjang baris {n_part}) ---")
    for i, part in enumerate(parts):
        print(f"   Baris {i+1}: '{part}'")
    print(f"   Ciphertext Transposisi (C2): {C2}")
    
    # --- c. Tampilkan Hasil Akhir ---
    print("\n================ HASIL AKHIR ===============")
    print(f"1. Input Plaintext         : {P}")
    print(f"2. Ciphertext Substitusi   : {C1}")
    print(f"3. Substitusi + Transposisi: {C2}")
    print("============================================")
    
    return P, C1, C2

# --- Eksekusi Program ---
INPUT_PLAINTEXT = "UNIKA SANTO THOMAS"
proses_enkripsi_lengkap(INPUT_PLAINTEXT)