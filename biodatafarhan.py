import sys
import time
import argparse

Nama = "Muhammad Farhan"
NIM = 1202407022
Alamat = "Sambi, Kabupaten Boyolali"
Jurusan = "Teknik Informatika"
Tempat_Lahir = "Boyolali"
Tanggal_Lahir = "23 Maret 2004"
Agama = "Islam"
Status = "Mahasiswa"
Motivasi = (
    "Kebaikan bukan untuk diliat orang lain, tetapi atas dasar tolong menolong sesama manusia. "
    "Jika kebaikanmu diragukan oleh orang lain, Hanya Allah yang berhak untuk menilai seberapa tulus perbuatanmu."
)
Ketik = [
    f"Nama           : {Nama}",
    f"NIM            : {NIM}",
    f"Alamat         : {Alamat}",
    f"Jurusan        : {Jurusan}",
    f"Tempat Lahir   : {Tempat_Lahir}",
    f"Tanggal Lahir  : {Tanggal_Lahir}",
    f"Agama          : {Agama}",
    f"Status         : {Status}",
    "",
    "Motivasi       :",
]

max_len = 70
mot_words = Motivasi.split()
mot_lines = []
cur = ""
for w in mot_words:
    if len(cur) + 1 + len(w) <= max_len:
        cur = (cur + " " + w).strip()
    else:
        mot_lines.append(cur)
        cur = w
if cur:
    mot_lines.append(cur)
Ketik.extend([f"  {line}" for line in mot_lines])
Ketik.append("")
COLOR_TITLE = "\033[1;36m"   
COLOR_KEY   = "\033[1;33m"   
COLOR_RESET = "\033[0m"

def type_write(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def fancy_line(line, delay, use_color=True):
    if not use_color or ":" not in line:
        type_write(line, delay)
        return

    key, val = line.split(":", 1)
    for ch in COLOR_KEY + key + COLOR_RESET + ":":
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    if val.startswith(" "):
        sys.stdout.write(" ")
        sys.stdout.flush()
        time.sleep(delay)
        val = val[1:]
    for ch in val:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()

def main():
    parser = argparse.ArgumentParser(description="Ketik Biodata Muhammad farhan.")
    parser.add_argument("--speed", type=float, default=0.03, help="Delay per karakter (detik)")
    parser.add_argument("--no-color", action="store_true", help="Matikan warna ANSI")
    parser.add_argument("--fast", action="store_true", help="Mode cepat (speed = 0.005)")
    args = parser.parse_args()

    delay = 0.005 if args.fast else max(0.0, args.speed)
    use_color = not args.no_color

    bIODATA = "== Biodata Muhammad Farhan =="

    if use_color:
        for ch in COLOR_TITLE + bIODATA + COLOR_RESET:
            sys.stdout.write(ch)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n\n")
        sys.stdout.flush()
    else:
        type_write(bIODATA, delay)
        sys.stdout.write("\n")

    for line in Ketik:
        fancy_line(line, delay, use_color)
        time.sleep(delay * 6)

    type_write("Terimakasih semua", delay * 1.0)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.stdout.write("\n[Dibatalkan]\n")
        sys.exit(0)
