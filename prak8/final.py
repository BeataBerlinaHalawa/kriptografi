import tkinter as tk
from tkinter import messagebox, filedialog
from tkinter.scrolledtext import ScrolledText

# -------------------- AES core functions (sama dengan kode Anda) --------------------

def text_to_hex(text):
    return [format(ord(c), '02X') for c in text]

def to_matrix_4x4(hex_list):
    matrix = [[0]*4 for _ in range(4)]
    for i in range(16):
        row = i % 4
        col = i // 4
        matrix[row][col] = hex_list[i]
    return matrix

def xor_matrices(m1, m2):
    result = [[0]*4 for _ in range(4)]
    for r in range(4):
        for c in range(4):
            v1 = int(m1[r][c], 16)
            v2 = int(m2[r][c], 16)
            result[r][c] = format(v1 ^ v2, '02X')
    return result

SBOX = [
    0x63,0x7C,0x77,0x7B,0xF2,0x6B,0x6F,0xC5,0x30,0x01,0x67,0x2B,0xFE,0xD7,0xAB,0x76,
    0xCA,0x82,0xC9,0x7D,0xFA,0x59,0x47,0xF0,0xAD,0xD4,0xA2,0xAF,0x9C,0xA4,0x72,0xC0,
    0xB7,0xFD,0x93,0x26,0x36,0x3F,0xF7,0xCC,0x34,0xA5,0xE5,0xF1,0x71,0xD8,0x31,0x15,
    0x04,0xC7,0x23,0xC3,0x18,0x96,0x05,0x9A,0x07,0x12,0x80,0xE2,0xEB,0x27,0xB2,0x75,
    0x09,0x83,0x2C,0x1A,0x1B,0x6E,0x5A,0xA0,0x52,0x3B,0xD6,0xB3,0x29,0xE3,0x2F,0x84,
    0x53,0xD1,0x00,0xED,0x20,0xFC,0xB1,0x5B,0x6A,0xCB,0xBE,0x39,0x4A,0x4C,0x58,0xCF,
    0xD0,0xEF,0xAA,0xFB,0x43,0x4D,0x33,0x85,0x45,0xF9,0x02,0x7F,0x50,0x3C,0x9F,0xA8,
    0x51,0xA3,0x40,0x8F,0x92,0x9D,0x38,0xF5,0xBC,0xB6,0xDA,0x21,0x10,0xFF,0xF3,0xD2,
    0xCD,0x0C,0x13,0xEC,0x5F,0x97,0x44,0x17,0xC4,0xA7,0x7E,0x3D,0x64,0x5D,0x19,0x73,
    0x60,0x81,0x4F,0xDC,0x22,0x2A,0x90,0x88,0x46,0xEE,0xB8,0x14,0xDE,0x5E,0x0B,0xDB,
    0xE0,0x32,0x3A,0x0A,0x49,0x06,0x24,0x5C,0xC2,0xD3,0xAC,0x62,0x91,0x95,0xE4,0x79,
    0xE7,0xC8,0x37,0x6D,0x8D,0xD5,0x4E,0xA9,0x6C,0x56,0xF4,0xEA,0x65,0x7A,0xAE,0x08,
    0xBA,0x78,0x25,0x2E,0x1C,0xA6,0xB4,0xC6,0xE8,0xDD,0x74,0x1F,0x4B,0xBD,0x8B,0x8A,
    0x70,0x3E,0xB5,0x66,0x48,0x03,0xF6,0x0E,0x61,0x35,0x57,0xB9,0x86,0xC1,0x1D,0x9E,
    0xE1,0xF8,0x98,0x11,0x69,0xD9,0x8E,0x94,0x9B,0x1E,0x87,0xE9,0xCE,0x55,0x28,0xDF,
    0x8C,0xA1,0x89,0x0D,0xBF,0xE6,0x42,0x68,0x41,0x99,0x2D,0x0F,0xB0,0x54,0xBB,0x16
]

RCON = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0x1B,0x36]

def rot_word(word):
    return word[1:] + word[:1]

def sub_word(word):
    return [SBOX[b] for b in word]

def key_expansion(key_matrix):
    key_words = []
    for col in range(4):
        key_words.append([key_matrix[row][col] for row in range(4)])
    for i in range(4, 44):
        temp = key_words[i-1].copy()
        if i % 4 == 0:
            temp = rot_word(temp)
            temp = sub_word(temp)
            temp[0] ^= RCON[(i//4)-1]
        new_word = [temp[j] ^ key_words[i-4][j] for j in range(4)]
        key_words.append(new_word)
    return key_words

def words_to_matrix(words):
    matrix = [[0]*4 for _ in range(4)]
    for col in range(4):
        for row in range(4):
            matrix[row][col] = words[col][row]
    return matrix

# -------------------- Utility formatting --------------------

def matrix_to_str_hex(matrix):
    lines = []
    for row in matrix:
        lines.append(" ".join(f"{x}" if isinstance(x,str) else f"{x:02X}" for x in row))
    return "\n".join(lines)

def matrix_to_str_hex_bytes(matrix):
    lines = []
    for row in matrix:
        lines.append(" ".join(f"{x:02X}" for x in row))
    return "\n".join(lines)

# -------------------- GUI handlers --------------------

def generate_keys():
    out_text.delete("1.0", tk.END)
    pt = entry_plain.get()
    ck = entry_key.get()

    if len(pt) != 16 or len(ck) != 16:
        messagebox.showerror("Error", "Plaintext dan Cipherkey harus tepat 16 karakter.")
        return

    out_text.insert(tk.END, f"Plaintext: {pt}\nCipherkey: {ck}\n\n")

    # konversi ke hex
    hex_plain = text_to_hex(pt)
    hex_key = text_to_hex(ck)

    out_text.insert(tk.END, "=== Konversi ke HEX ===\n")
    out_text.insert(tk.END, "Plaintext (HEX):\n" + " ".join(hex_plain) + "\n")
    out_text.insert(tk.END, "Cipherkey (HEX):\n" + " ".join(hex_key) + "\n\n")

    # matriks 4x4
    mat_plain = to_matrix_4x4(hex_plain)
    mat_key = to_matrix_4x4(hex_key)

    out_text.insert(tk.END, "=== Matriks 4x4 (kolom-per-kolom) ===\n")
    out_text.insert(tk.END, "Plaintext Matrix (HEX):\n" + matrix_to_str_hex(mat_plain) + "\n\n")
    out_text.insert(tk.END, "Cipherkey Matrix (HEX):\n" + matrix_to_str_hex(mat_key) + "\n\n")

    # XOR / AddRoundKey
    mat_xor = xor_matrices(mat_plain, mat_key)
    out_text.insert(tk.END, "=== XOR (AddRoundKey / K0) ===\n")
    out_text.insert(tk.END, matrix_to_str_hex(mat_xor) + "\n\n")

    # Prepare key0 as integer matrix for expansion
    key0 = [[int(mat_xor[r][c], 16) for c in range(4)] for r in range(4)]
    all_keys = key_expansion(key0)

    # Print K0..K10
    out_text.insert(tk.END, "=== Round Keys (K0..K10) ===\n")
    for r in range(11):
        start = r * 4
        keymat = words_to_matrix(all_keys[start:start+4])
        out_text.insert(tk.END, f"K{r}:\n")
        # keymat currently integer matrix; format as hex bytes
        for row in keymat:
            out_text.insert(tk.END, " ".join(f"{val:02X}" for val in row) + "\n")
        out_text.insert(tk.END, "\n")

def clear_all():
    entry_plain.delete(0, tk.END)
    entry_key.delete(0, tk.END)
    out_text.delete("1.0", tk.END)

def save_result():
    content = out_text.get("1.0", tk.END)
    if not content.strip():
        messagebox.showinfo("Info", "Tidak ada hasil untuk disimpan.")
        return
    path = filedialog.asksaveasfilename(defaultextension=".txt",
                                        filetypes=[("Text files","*.txt"),("All files","*.*")],
                                        title="Save result as...")
    if path:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        messagebox.showinfo("Saved", f"Hasil disimpan ke:\n{path}")

# -------------------- Build GUI --------------------

root = tk.Tk()
root.title("AES Key Expansion - GUI")
root.geometry("820x620")
root.resizable(False, False)

frame_top = tk.Frame(root, padx=10, pady=8)
frame_top.pack(fill=tk.X)

lbl_plain = tk.Label(frame_top, text="Plaintext (16 chars):")
lbl_plain.grid(row=0, column=0, sticky="w")
entry_plain = tk.Entry(frame_top, width=30)
entry_plain.grid(row=0, column=1, padx=6)
entry_plain.insert(0, "PRATIKUMKRIPTOGA")  # contoh default

lbl_key = tk.Label(frame_top, text="Cipherkey (16 chars):")
lbl_key.grid(row=1, column=0, sticky="w", pady=6)
entry_key = tk.Entry(frame_top, width=30)
entry_key.grid(row=1, column=1, padx=6, pady=6)
entry_key.insert(0, "UNIKASANTOTHOMAS")  # contoh default

btn_generate = tk.Button(frame_top, text="Generate Keys", width=16, command=generate_keys)
btn_generate.grid(row=0, column=2, rowspan=2, padx=12)

btn_clear = tk.Button(frame_top, text="Clear", width=10, command=clear_all)
btn_clear.grid(row=0, column=3, rowspan=2, padx=6)

btn_save = tk.Button(frame_top, text="Save Result", width=12, command=save_result)
btn_save.grid(row=0, column=4, rowspan=2, padx=6)

# Output area
frame_out = tk.Frame(root, padx=10, pady=6)
frame_out.pack(fill=tk.BOTH, expand=True)

out_text = ScrolledText(frame_out, wrap=tk.WORD, font=("Courier", 10))
out_text.pack(fill=tk.BOTH, expand=True)

# Help / footer
footer = tk.Label(root, text="Masukkan plaintext dan cipherkey tepat 16 karakter. Klik Generate Keys.", anchor="w")
footer.pack(fill=tk.X, padx=10, pady=4)

root.mainloop()
