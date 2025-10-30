# Program Menghitung Total Keuntungan Selama 8 Bulan

modal = 100000000  # modal awal 100 juta
total_laba = 0

print("=== Laporan Keuntungan Selama 8 Bulan ===")

for bulan in range(1, 9):
    if bulan <= 2:
        laba = 0
    elif bulan <= 4:
        laba = modal * 0.01 # 1%
    elif bulan <= 7:
        laba = modal * 0.05  # 5%
    else: 
        laba = modal * 0.03  # turun menjadi 3%

    total_laba += laba
    print(f"Laba bulan ke-{bulan} sebesar: Rp {int(laba)}")

# Total laba selama 8 bula
print(f"Total laba adalah: Rp {int(total_laba)}")