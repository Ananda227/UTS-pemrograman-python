#===========================================
#                 Percabangan
# ==========================================

#if
angka = 4 
if angka > 0 :
    print(angka, "adalah bilangan positif")
# output : 4 adalah bilangan positif

#if else
angka = -4
if angka > 0 :
    print(angka, "adalah bilangan positif")
else : 
    print(angka, "adalah bilangan negatif")
# output : -4 adalah bilangan negatif

#if....elif....else
angka = 3.2
if angka > 0 :
    print(angka, "adalah bilangan positif")
elif angka == 0 :
    print("Nol")
else : 
    print(angka, "adalah bilangan negatif")
# output : 3.2 adalah bilangan positif

# if bersarang 
gaji = 2000000
berkeluarga = True
punya_rumah = True

if gaji > 3000000 :
    print("Gaji diatas UMR")
    if berkeluarga : 
        print("wajib ikut asuransi")
    else :
        print("sunnah ikut asuransi")
    if punya_rumah :
        print("wajib bayar pajak rumah")
    else :
        print("rumah aja gak punya gimana mau bayar pajak rumah")
else :
    print("Gaji belum UMR")
    
#percabangan indeks nilai statis
nilai = 80

if nilai >= 85 and nilai <= 100 :
    print("Nilai A")
elif nilai >= 70 and nilai <= 84 :
    print("Nilai B")
elif nilai >= 55 and nilai <= 69 :
    print("Nilai C")
else :
    print("Nilai D") 
#output : Nilai B

#percabangan nilai dinamis
nilai = int(input("Masukkan Nilai Mahasiswa : "))

if nilai >= 85 and nilai <= 100 :
    print("Nilai A")
elif nilai >= 70 and nilai <= 84 :
    print("Nilai B")
elif nilai >= 55 and nilai <= 69 :
    print("Nilai C")
else :
    print("Nilai D") 
    
#===========================================
#                 Perulangan
# ==========================================

# for
nomor = [5,5,2]
jumlah = 0

for i in nomor :
    jumlah += i

print("Jumlah Sumuanya : ", jumlah)
#output : 12

# for dengan range
for hitung in range(5):
    print("Hitung : ",hitung)
    
#output : # Hitung :  0
          # Hitung :  1
          # Hitung :  2
          # Hitung :  3
          # Hitung :  4


# while
hitung = 0

while (hitung < 5) :
    print("Hitung : ", hitung)
    hitung += 1
#output : # Hitung :  0
          # Hitung :  1
          # Hitung :  2
          # Hitung :  3
          # Hitung :  4
          
#contoh program kelipatan  bilangan genap
i = 0
n = int(input("Masukkan batas : "))

for i in range(n) :
    if i % 2 == 0 :
        print("Bilangan : ", i)
    i = i + 1
    
#latihan 
n = int(input("Masukkan batas : "))

i = 0
hitung = 0

while hitung < n :
    if i % 2 == 0 :
        print(i, end=' ')
        hitung += 1
    
    i += 1
        
#===========================================
#                 Fungsi
# ==========================================
def sapa(nama):
    print("Hai " + nama + " Apa kabar")
    
#memanggil fungsi
sapa('armando')
#output : Hai armando Apa kabar

#docstring
def sapa(nama):
    "contoh cetak keterangan"
    print("Hai " + nama + " Apa kabar")
    return nama

sapa('armando')
print(sapa.__doc__)

# contoh program Luas persegi panjang dengan fungsi
#statis
def persegipanjang(panjang,lebar):
    luas = panjang * lebar
    print("Luas : ",luas)
    return luas

print("Menghitung luas persegi panjang")
persegipanjang(4,5)

#dinamiis
def persegipanjang(panjang,lebar):
    luas = panjang * lebar
    print("Luas : ",luas)
    return luas

print("Menghitung luas persegi panjang")
a = int(input("Masukkan panjang : "))
b = int(input("Masukkan Lebar   : "))
persegipanjang(a,b)

#latihan
def hitung_luas(panjang=None, lebar=None, sisi=None):
    "Menghitung Luas Persegi Panjang & Persegi"
    if panjang and lebar:
        luas = panjang * lebar
        print("Luasnya=", luas,"\n")
    elif sisi:
        luas = sisi ** 2
        print("Luasnya =", luas,"\n")
    else:
        print("Masukkan panjang dan lebar untuk menghitung luas persegi panjang atau sisi untuk menghitung luas persegi.")


print(hitung_luas.__doc__)
#luas persegi panjang
print("Persegi Panjang")
a = int(input("Masukkan panjang : "))
b = int(input("Masukkan lebar : "))
hitung_luas(panjang = a,lebar = b)

# luas persegi
print("Persegi")
c = int(input("Masukkan sisi : "))
hitung_luas(sisi=c)
