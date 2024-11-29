import math

def l_persegi (sisi):
    luas = sisi * sisi
    keliling = sisi * sisi * sisi * sisi
    print(f'Luas persegi {sisi} * {sisi} = {luas}')
    print(f'Keliling persegi adalah {keliling}')

def persegi_panjang (panjang, lebar):
    luas = panjang * lebar
    print('Hasil luas persegi panjang dari', panjang * lebar, '=', luas)

def l_segitiga (alas, tinggi):
    luas = 1/2 * alas * tinggi 
    print(f'Luas segitiga {1.2} * {alas} * {tinggi} = {luas}')

def l_lingkaran (r1, r2):
    phi = 3.14
    luas = phi * r1 * r2
    print(f'Luas lingkaran adalah phi * {r1} * {r2} = {luas}')

def l_jajargenjang (alas, tinggi):
    luas = alas * tinggi
    print(f'Luas jajargenjang {alas} * {tinggi} = {luas}')