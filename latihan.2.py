import itertools

def hitung_dan_cetak_distribusi_buku(n_buku, r_bagian):
    """
    Menghitung dan mencetak semua cara mengatur n_buku di r_bagian rak.
    Ini adalah masalah distribusi objek berbeda (buku) ke dalam kotak berbeda (rak).
    """
    
    print("==================================================================")
    print(f"DISTRIBUSI {n_buku} BUKU KE {r_bagian} BAGIAN RAK")
    print("==================================================================")
    
    if n_buku < 0 or r_bagian <= 0:
        print("[ERROR] Jumlah buku harus >= 0 dan jumlah bagian rak harus >= 1.")
        return

    # 1. Menghitung Jumlah Total Cara (Rumus: r^n)
    jumlah_cara = r_bagian ** n_buku
    print(f"Rumus: (Jumlah Bagian Rak)^(Jumlah Buku) = {r_bagian}^{n_buku} = {jumlah_cara}")
    
    if jumlah_cara > 1000:
         print("\n[PERINGATAN] Jumlah susunan sangat besar. Mencetak semua susunan akan memakan waktu dan ruang.")
         tampilkan = input("Apakah Anda yakin ingin mencetak semua susunan? (y/t): ").lower()
         if tampilkan != 'y':
             return

    # 2. Menyiapkan Data
    
    # Label untuk setiap buku (misalnya: Buku_1, Buku_2, ...)
    daftar_buku = [f"Buku_{i+1}" for i in range(n_buku)]
    
    # Label untuk setiap bagian rak (misalnya: Rak_A, Rak_B, ...)
    # Kita menggunakan abjad untuk representasi visual yang lebih baik
    daftar_rak = [chr(65 + i) for i in range(r_bagian)] # 'A', 'B', 'C', ...
    
    if r_bagian > 26:
         daftar_rak = [f"Rak_{i+1}" for i in range(r_bagian)]


    print(f"\nBuku (Objek): {daftar_buku}")
    print(f"Bagian Rak (Tujuan): {daftar_rak}")
    print("\n------------------------------------------------------------------")
    print("DAFTAR SEMUA SUSUNAN:")
    print("------------------------------------------------------------------")

    # 3. Mencetak Semua Susunan Menggunakan itertools.product (Produk Kartesius)
    # Setiap elemen dari produk adalah tuple yang menunjukkan penempatan setiap buku.
    # Contoh: (Rak_A, Rak_B, Rak_A) berarti Buku_1 di Rak_A, Buku_2 di Rak_B, Buku_3 di Rak_A.
    
    semua_susunan = list(itertools.product(daftar_rak, repeat=n_buku))
    
    for i, susunan in enumerate(semua_susunan):
        penempatan = []
        for buku_idx, rak_label in enumerate(susunan):
            penempatan.append(f"{daftar_buku[buku_idx]} -> {rak_label}")
        
        print(f"Cara {i+1:0{len(str(jumlah_cara))}d}: {', '.join(penempatan)}")

# --- Contoh Penggunaan ---

# Kasus Sederhana: 2 Buku di 3 Bagian Rak (3^2 = 9 cara)
hitung_dan_cetak_distribusi_buku(n_buku=2, r_bagian=3)

# Kasus Kompleks: 4 Buku di 2 Bagian Rak (2^4 = 16 cara)
# hitung_dan_cetak_distribusi_buku(n_buku=4, r_bagian=2)

# Kasus Besar: (n=5, r=5) akan menghasilkan 3125 cara, dihindari untuk output konsol.
# hitung_dan_cetak_distribusi_buku(n_buku=5, r_bagian=5)
