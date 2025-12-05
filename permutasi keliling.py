import math

def hitung_permutasi_siklis(n):
    """Menghitung jumlah permutasi siklis dari n objek."""
    if n <= 1:
        return 1
    # Permutasi Siklis = (n - 1)!
    return math.factorial(n - 1)

# Contoh penggunaan
n_orang = 5
hasil = hitung_permutasi_siklis(n_orang)

print(f"Jumlah orang (n): {n_orang}")
print(f"Permutasi Siklis P_s({n_orang}) = ({n_orang} - 1)! = {hasil}")
# Output: 24 (4*3*2*1)
