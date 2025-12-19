import random

# =============================
# Fungsi invers modulo
# =============================
def mod_inverse(a, p):
    return pow(a, p - 2, p)

# =============================
# Enkripsi ElGamal (tabel)
# =============================
def elgamal_encrypt_table(plaintext, p, g, y):
    ciphertext = []

    print("\n=== TABEL ENKRIPSI ELGAMAL ===")
    print("No | Char | ASCII | k  | a=g^k mod p | y^k mod p | b=m*y^k mod p")
    print("-" * 75)

    for i, char in enumerate(plaintext, start=1):
        m = ord(char)
        k = random.randint(1, p - 2)
        a = pow(g, k, p)
        yk = pow(y, k, p)
        b = (m * yk) % p

        ciphertext.append((a, b))

        print(f"{i:2} |  {char:2}  |  {m:3}  | {k:2} |     {a:4}      |    {yk:4}     |      {b:4}")

    return ciphertext

# =============================
# Dekripsi ElGamal (tabel)
# =============================
def elgamal_decrypt_table(ciphertext, p, x):
    plaintext = ""

    print("\n=== TABEL DEKRIPSI ELGAMAL ===")
    print("No |   a   |   b   | s=a^x mod p | s^-1 mod p | m=b*s^-1 mod p | Char")
    print("-" * 85)

    for i, (a, b) in enumerate(ciphertext, start=1):
        s = pow(a, x, p)
        s_inv = mod_inverse(s, p)
        m = (b * s_inv) % p
        char = chr(m)
        plaintext += char

        print(f"{i:2} | {a:5} | {b:5} |    {s:5}     |    {s_inv:5}     |       {m:3}        |  {char}")

    return plaintext

# =============================
# MAIN PROGRAM
# =============================
p = 467       # bilangan prima
g = 2         # generator
x = 127       # kunci privat
y = pow(g, x, p)

print("=== PROGRAM ELGAMAL ===")
plaintext = input("Masukkan plaintext (huruf bebas): ").upper()

print("\nPARAMETER")
print("p =", p)
print("g =", g)
print("x =", x)
print("y =", y)

# Enkripsi
ciphertext = elgamal_encrypt_table(plaintext, p, g, y)

print("\nCiphertext (a, b):")
for c in ciphertext:
    print(c)

# Dekripsi
hasil = elgamal_decrypt_table(ciphertext, p, x)

print("\nHASIL DEKRIPSI :", hasil)