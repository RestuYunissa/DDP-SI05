import math

def kubus (sisi):
    volume = sisi ** 3
    print(f'Volume kubus {sisi} * {sisi} * {sisi} = {volume}' )

def balok (panjang,lebar,tinggi):
    volume = panjang * lebar * tinggi
    print(f'Volume balok {panjang} * {lebar} * {tinggi} = {volume}')

def tabung (jari2,tinggi):
    volume = 22/7 * (jari2 ** 2) * tinggi 
    print(f'Volume tabung phi * {jari2} * {jari2} * {tinggi} = {volume}')

def kerucut (jari2,tinggi):
    volume = 1/3 *22/7 * (jari2 ** 2) * tinggi
    print(f'Volume kerucut 1/3 * phi * {jari2} * {jari2} * {tinggi} = {volume}')

def bola (jari2):
    volume = 4/3 * 22/7 * (jari2 ** 3)
    print(f'Volume bola 4/3 * phi * {jari2} * {jari2} * {jari2} = {volume}')