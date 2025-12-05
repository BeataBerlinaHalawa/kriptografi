def transposisi_cipher(plaintext):
    # Menghitung panjang setiap bagian (membagi total panjang dengan 4)
    # Operator // (floor division) memastikan hasilnya bilangan bulat.
    part_length = len(plaintext) // 4
    
    # Membagi plaintext menjadi beberapa bagian (chunks)
    parts = [plaintext[i:i + part_length] for i in range(0, 
                                                        len(plaintext), part_length)]
    
    ciphertext = ""
    
    # Melakukan pembacaan secara kolom (col 0, col 1, col 2, col 3)
    for col in range(4):
        for part in parts:
            # Memastikan kolom yang ingin diakses ada dalam panjang bagian (part)
            if col < len(part):
                ciphertext += part[col]
                
    return ciphertext

# Mengambil input dari pengguna
plaintext = input("Masukkan plaintext: ")
ciphertext = transposisi_cipher(plaintext)

# Mencetak hasil
print(ciphertext)
