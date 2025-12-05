import itertools

# Daftar elemen yang akan dihitung permutasinya
elemen = ['A', 'B', 'C']

# Menghasilkan semua permutasi dari elemen
semua_permutasi = list(itertools.permutations(elemen))

# Menampilkan hasil
print(f"Elemen: {elemen}")
print(f"Jumlah total permutasi: {len(semua_permutasi)}")
print("Daftar permutasi:")
for p in semua_permutasi:
    print(p)
