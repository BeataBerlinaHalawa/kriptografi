# Kalkulator Sederhana (perbaikan, lebih aman dan informatif)
def minta_angka(prompt):
    """Minta input angka sampai user memasukkan angka valid atau 'keluar'."""
    while True:
        s = input(prompt).strip()
        if s.lower() in ("keluar", "exit"):
            raise KeyboardInterrupt  # kita gunakan untuk keluar dari program
        try:
            # terima integer atau float
            if "." in s:
                return float(s)
            else:
                return int(s)
        except ValueError:
            print("Input bukan angka. Ketik angka (contoh: 3 atau 2.5) atau 'keluar' untuk berhenti.")

def minta_operator(prompt):
    """Minta operator valid dari user."""
    valid = {"+", "-", "*", "/", "%", "**"}  # tambah operator opsional
    while True:
        op = input(prompt).strip()
        if op in valid:
            return op
        print("Operator tidak dikenali. Pilih salah satu dari: +  -  *  /  %  **")

def kalkulasi(a, b, op):
    """Lakukan operasi dan kembalikan hasil atau pesan error."""
    try:
        if op == "+":
            return a + b
        if op == "-":
            return a - b
        if op == "*":
            return a * b
        if op == "/":
            if b == 0:
                return "Error: pembagian dengan nol"
            return a / b
        if op == "%":
            if b == 0:
                return "Error: modulus dengan nol"
            return a % b
        if op == "**":
            return a ** b
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

def main():
    print("=== Kalkulator Sederhana ===")
    print("Ketik 'keluar' saat diminta angka untuk menghentikan program.")
    ulang = True
    try:
        while ulang:
            # input angka
            a = minta_angka("Masukkan nilai a: ")
            b = minta_angka("Masukkan nilai b: ")

            # input operator
            op = minta_operator("Masukkan operator (+, -, *, /, %, **): ")

            # hitung
            hasil = kalkulasi(a, b, op)

            # tampilkan hasil dalam format rapi
            print(f"Hasil: {a} {op} {b} = {hasil}")

            # tanya ulang, terima Y/T dalam berbagai variasi (ya, tidak)
            jaw = input("Ingin menghitung lagi? (Y/T): ").strip().lower()
            if jaw not in ("y", "ya", "yes"):
                ulang = False

    except KeyboardInterrupt:
        # terjadi jika user ketik 'keluar' atau Ctrl+C
        print("\nPengguna menghentikan program.")

    print("Program selesai. Terima kasih.")

if __name__ == "__main__":
    main()
