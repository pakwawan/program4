def kalkulator():
    print("=" * 40)
    print("        KALKULATOR SEDERHANA")
    print("=" * 40)
    
    while True:
        print("\nPilihan Operasi:")
        print("1. Penjumlahan (+)")
        print("2. Pengurangan (-)")
        print("3. Perkalian (*)")
        print("4. Pembagian (/)")
        print("5. Keluar")
        
        pilihan = input("\nMasukkan pilihan (1/2/3/4/5): ").strip()
        
        if pilihan == '5':
            print("\nTerima kasih telah menggunakan kalkulator!")
            break
        
        if pilihan not in ['1', '2', '3', '4']:
            print("Pilihan tidak valid! Silakan coba lagi.")
            continue
        
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
            
            if pilihan == '1':
                hasil = angka1 + angka2
                operasi = "+"
            elif pilihan == '2':
                hasil = angka1 - angka2
                operasi = "-"
            elif pilihan == '3':
                hasil = angka1 * angka2
                operasi = "*"
            elif pilihan == '4':
                if angka2 == 0:
                    print("Tidak bisa membagi dengan angka 0!")
                    continue
                hasil = angka1 / angka2
                operasi = "/"
            
            print(f"\nHasil: {angka1} {operasi} {angka2} = {hasil}")
        
        except ValueError:
            print("Input tidak valid! Masukkan angka dengan benar.")

if __name__ == "__main__":
    kalkulator()