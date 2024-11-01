print("======== SOAL NOMOR 1 ========")

kendaraan = ["BMW Z4 E89", "Mobil", 2996, "Hitam", 4]
print(kendaraan)

kendaraan.append(1880000000)
kendaraan.append("sport")
print(kendaraan)

kendaraan.insert(2, "BMW")
print(kendaraan)

print("======== SOAL NOMOR 2 ========")

pilih = int((input("""selamat datang di aplikasi
menghitung
1.untuk menghitung luas persegi
2.untuk menghitung luas lingkaran
3.untuk menghitung luas segitiga 
                  
masukan pilihan anda : """)))

match pilih:
    case 1:
        print("kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("masukan sisi persegi : "))
        luaspsg = sisi*sisi
        print("luas persegi yang sisinya ",sisi, "adalah", luaspsg)
    case 2:
        print ("kamu memilih 2 untuk menghitung luas lingkaran")
        jari2 = int(input("masukan jari-jari : "))
        luaslkr = 3.14 * jari2 *jari2
        print("luas lingkaran yang jari-jarinya ",jari2, "adalah",luaslkr )
    case 3:
        print ("kamu memilih 3 untuk menghitung luas segitiga")
        alas = int(input("masukan alas segitiga : "))
        tinggi = int(input("masukkan tinggi segitiga : "))
        LuasSegitiga = 0.5 * alas * tinggi
        print("luas segitiga yang alasnya", alas, "dan tingginya", tinggi, "adalah", LuasSegitiga)
    case _:
        print("Input yang anda masukkan salah!")