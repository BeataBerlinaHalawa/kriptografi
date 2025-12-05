import math
from collections import Counter
import itertools

def faktorial(n):
    """Menghitung faktorial, menggunakan math.factorial."""
    if n < 0:
        return 0
    return math.factorial(n)

def hitung_permutasi_sebagian(n, r):
    """Menghitung jumlah permutasi P(n, r) = n! / (n-r)!"""
    if r < 0 or r > n:
        return 0
    return faktorial(n) // faktorial(n - r)

def hitung_permutasi_siklis(n):
    """Menghitung jumlah permutasi siklis Ps = (n - 1)!"""
    if n <= 1:
        return 1
    return faktorial(n - 1)

def hitung_permutasi_kelompok(data):
    """Menghitung jumlah permutasi unsur yang sama P = n! / (k1! * k2! * ...)"""
    n = len(data)
    
    # Menghitung frekuensi (jumlah kemunculan) setiap unsur
    frekuensi = Counter(data)
    
    pembilang = faktorial(n)
    
    # Menghitung penyebut: k1! * k2! * ...
    penyebut = 1
    for count in frekuensi.values():
        penyebut *= faktorial(count)
        
    return pembilang // penyebut

def generate_permutasi_sebagian(elemen, r):
    """Menghasilkan dan mencetak daftar permutasi sebagian."""
    # Menggunakan itertools untuk menghasilkan daftar susunan
    permutations = list(itertools.permutations(elemen, r))
    
    print("\n--- Daftar Permutasi Sebagian (P(n,r)) ---")
    print(f"n = {len(elemen)}, r = {r}")
    print(f"Total susunan: {len(permutations)} (dihitung: {hitung_permutasi_sebagian(len(elemen), r)})")
    for i, p in enumerate(permutations):
        print(f"{i+1}. {p}")


def main():
    print("=========================================")
    print("  KALKULATOR & GENERATOR JENIS PERMUTASI ")
    print("=========================================")
    print("Pilih Jenis Permutasi:")
    print("1. Permutasi Sebagian (P(n, r))")
    print("2. Permutasi Siklis (Ps(n))")
    print("3. Permutasi Unsur yang Sama/Kelompok (P_kelompok)")
    
    pilihan = input("Masukkan nomor pilihan (1/2/3): ")

    try:
        if pilihan == '1':
            print("\n--- Permutasi Sebagian (P(n, r)) ---")
            
            # Input Elemen
            elemen_str = input("Masukkan elemen (dipisahkan spasi/koma, e.g., A B C D): ")
            elemen = elemen_str.replace(',', ' ').split()
            n = len(elemen)
            
            # Input r
            r = int(input(f"Masukkan panjang urutan yang diambil (r, r <= {n}): "))

            if r > n or r < 0:
                print(f"\n[ERROR] Nilai r ({r}) harus antara 0 dan {n}.")
            else:
                jumlah = hitung_permutasi_sebagian(n, r)
                print(f"\n[HASIL JUMLAH] P({n}, {r}) = {jumlah}")
                
                # Opsi untuk menampilkan semua susunan
                tampil = input("Tampilkan semua susunan? (y/t): ").lower()
                if tampil == 'y':
                    generate_permutasi_sebagian(elemen, r)
        
        elif pilihan == '2':
            print("\n--- Permutasi Siklis (Ps(n)) ---")
            
            # Input n
            n_str = input("Masukkan jumlah objek total (n): ")
            n = int(n_str)
            
            if n < 0:
                print("\n[ERROR] Nilai n harus bilangan non-negatif.")
            else:
                jumlah = hitung_permutasi_siklis(n)
                print(f"\n[HASIL JUMLAH] Ps({n}) = ({n} - 1)! = {jumlah}")
                print("\n(Catatan: Untuk permutasi siklis, susunan hanya dihitung, tidak digenerate karena kompleksitas representasi melingkar.)")

        elif pilihan == '3':
            print("\n--- Permutasi Unsur yang Sama/Kelompok ---")
            
            # Input Data
            data_str = input("Masukkan urutan data (e.g., KATAKKU atau 1 1 2 3 3 3): ").replace(' ', '')
            
            jumlah = hitung_permutasi_kelompok(data_str)
            
            # Tampilkan detail kelompok
            frekuensi = Counter(data_str)
            print(f"\nTotal unsur (n): {len(data_str)}")
            print("Unsur yang sama:")
            for item, count in frekuensi.items():
                if count > 1:
                    print(f"- '{item}': {count} kali (k={count})")

            print(f"\n[HASIL JUMLAH] P_kelompok = {len(data_str)}! / ({' * '.join([f'{c}!' for c in frekuensi.values()])}) = {jumlah}")
        
        else:
            print("\nPilihan tidak valid. Silakan masukkan 1, 2, atau 3.")

    except ValueError:
        print("\n[ERROR] Masukkan harus berupa angka atau format yang benar.")
    except Exception as e:
        print(f"\n[ERROR] Terjadi kesalahan: {e}")

if __name__ == "__main__":
    main()
