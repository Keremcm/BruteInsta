import itertools

def generate_passwords(info, symbols=None, max_combo=3):
    if symbols is None:
        symbols = ['', '_', '.', '-', '@', '!']

    values = [info['ad'], info['soyad'], info['dogum'], info['sehir'], info['takim']]
    all_combos = set()

    for r in range(1, max_combo+1):
        for combo in itertools.permutations(values, r):
            for sym_pattern in itertools.product(symbols, repeat=r-1 if r > 1 else 1):
                merged = ''
                for i in range(r):
                    merged += combo[i]
                    if i < r - 1:
                        merged += sym_pattern[i]

                # Varyasyonlar
                all_combos.update([
                    merged,
                    merged.lower(),
                    merged.upper(),
                    merged.capitalize(),
                    merged[::-1],  # reverse
                    merged + info['dogum'],
                    info['dogum'] + merged
                ])

    return list(all_combos)

def save_to_txt(passwords, filename="wordlist.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for pw in passwords:
            f.write(pw + "\n")
    print(f"[+] {len(passwords)} adet şifre '{filename}' dosyasına kaydedildi.")

# Kullanıcı bilgileri
info = {
    "ad": "Semanur",
    "soyad": "Sema",
    "dogum": "1987",
    "sehir": "Trabzon",
    "takim": "TS"
}

# Üret ve kaydet
passwords = generate_passwords(info)
save_to_txt(passwords)
