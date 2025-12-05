def hitung_nilai_akhir(sikap, tugas, uts, uas):
    # Bobot
    nilai_akhir = (sikap * 0.10) + (tugas * 0.30) + (uts * 0.25) + (uas * 0.35)

    # Tentukan huruf mutu & bobot
    if 81 <= nilai_akhir <= 100:
        huruf = "A"
        bobot = 4
    elif 76 <= nilai_akhir <= 80:
        huruf = "B+"
        bobot = 3.5
    elif 71 <= nilai_akhir <= 75:
        huruf = "B"
        bobot = 3
    elif 66 <= nilai_akhir <= 70:
        huruf = "C+"
        bobot = 2.5
    elif 56 <= nilai_akhir <= 65:
        huruf = "C"
        bobot = 2
    elif 46 <= nilai_akhir <= 55:
        huruf = "D"
        bobot = 1
    else:
        huruf = "E"
        bobot = 0

    # Keterangan lulus/tidak
    if nilai_akhir >= 56:
        status = "Lulus"
    else:
        status = "Tidak Lulus"

    return nilai_akhir, huruf, bobot, status


# Program utama
print("=== Program Hitung Nilai Akhir Akademik ===")
sikap = float(input("Masukkan nilai Sikap/Kehadiran: "))
tugas = float(input("Masukkan nilai Tugas: "))
uts = float(input("Masukkan nilai UTS: "))
uas = float(input("Masukkan nilai UAS: "))

nilai_akhir, huruf, bobot, status = hitung_nilai_akhir(sikap, tugas, uts, uas)

print("\n=== Hasil Perhitungan ===")
print(f"Total Nilai Akhir : {nilai_akhir:.2f}")
print(f"Nilai Huruf       : {huruf}")
print(f"Bobot             : {bobot}")
print(f"Keterangan        : {status}")
