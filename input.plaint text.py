def substitusi_cipher(plaintext, aturan):
    """
    Melakukan substitusi karakter pada plaintext (huruf kapital)
    berdasarkan aturan yang diberikan.
    """
    ciphertext = ''
    # Mengubah seluruh plaintext menjadi huruf kapital sebelum iterasi
    for char in plaintext.upper():
        if char in aturan:
            # Jika karakter ada dalam aturan, substitusikan
            ciphertext += aturan[char]
        else:
            # Jika tidak ada dalam aturan, biarkan karakter asli
            ciphertext += char
    return ciphertext

# Mendefinisikan aturan substitusi (sebagai kamus/dictionary)
aturan_substitusi = {
    'U': 'K',
    'N': 'N',
    'I': 'I',
    'K': 'K',
    'A': 'B'
}

# Mengambil input dari pengguna dan mengubahnya menjadi huruf kapital
plaintext = input("Masukkan plaintext: ").upper()
ciphertext = substitusi_cipher(plaintext, aturan_substitusi)

# Mencetak hasil
print(f'Plaintext: {plaintext}')
print(f'Ciphertext: {ciphertext}')
