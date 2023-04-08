#SINTAX DASAR

#1.1 Identifier
# Identifier adalah identitas atau nama yang telah diberikan kepada function, variabel,
# obyek, class, namespace dan lain-lain.
# • Identifier bisa terdiri dari kombinasi huruf kecil (a-z) atau huruf besar (A-Z), angka ( 0-9 ), dan underscore ( _ ).
# • Identifier tidak bisa dimulai menggunakan angka, misalnya 1variabel.
# • Kata kunci tidak bisa digunakan sebagai identifier.
# • Tidak bisa menggunakan karakter spesial seperti @, $, and %.
# • Python bersifat case sensitive, variable dan Variabel adalah 2 identifier berbeda.

#1.2 Baris dan identansi
# Python tidak menggunakan tanda { } untuk menandai blok/grup kode. 
# Blok kode di python menggunakan tanda indentasi (spasi). 
# Jumlah spasi untuk setiap baris yang ada dalam satu blok kode harus sama.
#CONTOH :

print("BARIS")
print("IDENTANSI")

#1.3 Pernyataan Multibaris
# Di Python, akhir dari sebuah statement adalah karakter baris baru (newline). Kita dapat
# membuat sebuah statement terdiri dari beberapa baris dengan menggunakan tanda
# backslash ( \ ).
#contoh : 
angka1 = 2
a = angka1 + 4 + \
    7 + \
    5

print(a)

# Statement yang ada di dalam tanda kurung [ ], { }, dan ( ) tidak memerlukan tanda \.
#contoh :
namaHari = ['senin','selasa','rabu'
'kamis','jumat','sabtu','minggu']

print(namaHari)

#1.4 Tanda Kutip
# Python menggunakan tanda kutip tunggal (‘), ganda (“), maupun triple (‘’’ atau “””)
# untuk menandai string, sepanjang stringnya diawali oleh tanda kutip yang sama di awal
# dan akhir string. Tanda kutip tiga digunakan untuk string multibaris.
#contoh :

kutip1 = 'BELAJAR PYTHON'
kutip2 = "BELAJAR PYTHON DASAR"
kutip3 = """BELAJAR PYTHON
SIANG MALAM"""
kutip4 = """Eat
Code
Sleep
Repeat"""

print(kutip1)
print(kutip2)
print(kutip3)
print(kutip4)

# 1.5 Komentar
# Tanda pagar ( # ) digunakan untuk menandai komentar di python. Komentar tidak akan
# diproses oleh interpreter Python. Komentar hanya berguna untuk programmer untuk
# memudahkan memahami maksud dari kode.

# 1.6 Dua Pernyataan Dalam Satu Baris
# Titik koma dapat digunakan ketika terdapat 2 pernyataan dalam 1 baris kode.
# contoh :

print("TITIK KOMA"); print("TITIK KOMA KEDUA")

#TYPE DATA

#Kita bisa menggunakan fungsi type() untuk mengetahui tipe data suatu objek di python.
# Contoh :
x = 5
print(x, "type datanya adalah :", type(x))

y = 2.0
print(y, "type datanya adalah :", type(y))

#VARIABEL, OPERATOR, DAN EKSPRESI 

a = 2 #a merupakan variabel

#multi penugasan variabel  
x=y=z=3 
a = x+y+z
print(a)

a,b,c=1,3.4,"umar"
print("nama :",c)
print("semester :",a)
print("ipk :",b)
#x,y, dan z merupakan variabel begitu juga a,b dan c

