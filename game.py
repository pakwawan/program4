# Game Tebak Angka

angka_rahasia = 234
tebakan_benar = False

print("=" * 40)
print("   SELAMAT DATANG DI GAME TEBAK ANGKA")
print("=" * 40)
print("Saya memiliki angka rahasia antara 1-1000")
print("Bisakah kamu menebaknya?")
print()

while not tebakan_benar:
    try:
        tebakan = int(input("Masukkan tebakan Anda: "))
        
        if tebakan == angka_rahasia:
            print()
            print("🎉 " * 10)
            print("SELAMAT! TEBAKAN ANDA BENAR!")
            print("Angka rahasia adalah: " + str(angka_rahasia))
            print("🎉 " * 10)
            tebakan_benar = True
        elif tebakan < angka_rahasia:
            print("❌ Terlalu rendah! Coba lagi dengan angka yang lebih besar.")
        else:
            print("❌ Terlalu tinggi! Coba lagi dengan angka yang lebih kecil.")
    except ValueError:
        print("⚠️ Masukkan angka yang valid!")

