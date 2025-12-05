# Program Kalkulator Sederhana dengan Pengulangan Y/T

ulang = "Y"
while ulang.upper() == "Y":
    print("===== Kalkulator Sederhana =====")
    
    # Input nilai a dan b
    a = float(input("Masukkan nilai a: "))
    b = float(input("Masukkan nilai b: "))
    
    # Pilih operator
    print("Pilih operator: +, -, *, /")
    operator = input("Masukkan operator: ")
    
    # Proses perhitungan
    if operator == "+":
        hasil = a + b
    elif operator == "-":
        hasil = a - b
    elif operator == "*":
        hasil = a * b
    elif operator == "/":
        if b != 0:
            hasil = a / b
        else:
            hasil = "Error (pembagian dengan nol)"
    else:
        hasil = "Operator tidak dikenali!"
    
    # Tampilkan hasil
    print(f"Hasil dari {a} {operator} {b} = {hasil}")
    
    # Tanya apakah ingin ulang
    ulang = input("Apakah ingin melakukan perhitungan lagi? (Y/T): ")

print("Program selesai. Terima kasih!")
