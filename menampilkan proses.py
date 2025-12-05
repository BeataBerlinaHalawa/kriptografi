def transposisi_cipher(plaintext):
    # Menghitung panjang setiap bagian dengan pembagian lantai (floor division)
    part_length = len(plaintext) // 4
    
    # Membagi plaintext menjadi beberapa bagian (chunks)
    parts = [plaintext[i:i + part_length] for i in range(0, 
                                                        len(plaintext), part_length)]
    
    print("Bagian plaintext:")
    # Mencetak setiap bagian plaintext
    for i, part in enumerate(parts):
        print(f"Bagian {i + 1}: '{part}'")
    
    ciphertext = ""
    
    # Melakukan pembacaan secara kolom (col 0, col 1, col 2, col 3)
    for col in range(4):
        for part in parts:
            # Memastikan kolom yang ingin diakses ada dalam panjang bagian (part)
            if col < len(part):
                ciphertext += part[col]
                # Menambahkan langkah debugging (membutuhkan parts.index(part) untuk mendapatkan nomor bagian)
                # Catatan: parts.index(part) lambat dan berbahaya jika ada bagian yang identik.
                # Namun, kita mengikuti kode persis dari gambar.
                print(f"Menambahkan '{part[col]}' dari Bagian {parts.index(part) + 1} ke ciphertext.")
                
    return ciphertext

# Mengambil input dari pengguna
plaintext = input("Masukkan plaintext: ")
ciphertext = transposisi_cipher(plaintext)

# Mencetak hasil akhir
print(f"Ciphertext: '{ciphertext}'")
