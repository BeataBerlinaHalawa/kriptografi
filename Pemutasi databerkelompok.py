import math
from collections import Counter

def hitung_permutasi_kelompok(data):
    """Menghitung jumlah permutasi dengan unsur yang sama."""
    n = len(data)
    
    # Menghitung frekuensi (jumlah kemunculan) setiap unsur
    frekuensi = Counter(data)
    
    # Menghitung n!
    pembilang = math.factorial(n)
    
    # Menghitung k1! * k2! * ... * kt! (penyebut)
    penyebut = 1
    for count in frekuensi.values():
        penyebut *= math.factorial(count)
        
    # P = n! / (k1! * k2! * ...)
    jumlah_permutasi = pembilang // penyebut
    
    return jumlah_permutasi

# Contoh penggunaan: Kata "KATAKKU"
kata = "KATAKKU"
hasil = hitung_permutasi_kelompok(kata)

print(f"Kata: {kata}")
print(f"Total huruf (n): {len(kata)}")
print(f"Jumlah Permutasi: {hasil}")
# Output: 210 (7! / (3! * 2! * 1! * 1!) = 5040 / 24 = 210)
