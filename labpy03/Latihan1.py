import random

# Meminta input jumlah bilangan acak
n = int(input("Masukkan jumlah bilangan acak (n): "))
print(f"\nMenampilkan {n} bilangan acak yang lebih kecil dari 0.5:\n")

i = 0
while i < n:
    # gunakan for untuk menghasilkan beberapa angka acak
    for j in range(5):  # misalnya mencoba 5 kali setiap putaran while
        angka = random.random()
        if angka < 0.5:
            print(f"Bilangan ke-{i+1}: {angka}")
            i += 1
            if i == n:  # jika sudah cukup n bilangan, hentikan
                break
print("===========================================")
print("Program selesai menampilkan", n, "bilangan acak yang lebih kecil dari 0.5.")