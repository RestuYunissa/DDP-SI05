print("\n----- Mengubah Celcius ke Fahrenheit -----")
def celcius_ke_fahrenheit (celcius):
    print (celcius * 9/5 + 32)

celcius_ke_fahrenheit(0)
celcius_ke_fahrenheit(100)

print("\n----- Mengubah Celcius ke Fahrenheit -----")
def is_genap (genap):
    print (genap %2 == 0)

is_genap(4)
is_genap(7)

print("\n----- Mengubah Celcius ke Fahrenheit -----")
def skor (nilai):
    if nilai >= 70:
        print ("lulus")
    else:
        print ("gagal")   

skor (80) 
skor (60)

print("\n----- Mengubah Celcius ke Fahrenheit -----")
def bil_ganjil (ganjil):
    for i in range (1, ganjil+1, 2):
        print(i, end=",")

bil_ganjil(20)