#OUTPUT

print(1, 3, 5, 7)
#output : 1  3 5 7

print(1, 3, 5, 7, sep='*')
#output : 1*3*5*7

print(1, 3, 5, 7, sep='*', end='&')
#output : 1*3*5*7&

#INPUT 
# contoh 1 :
a = input("Masukkan Nilai A : ")
b = input("Masukkan Nilai B : ")

c = print(a,b)

#Bila kita menginput bilangan, misalnya integer lewat fungsi input(), maka hasil inputan
# tersebut adalah string dan bukan integer. Kita harus mengubahnya terlebih dahulu
# menjadi tipe integer menggunakan fungsi int().
#contoh 1:
a = int(input("masukkan nilai A : "))
b = int(input("masukkan nilai B : "))

c = a + b
print(c)

#contoh 2:
a = input("Masukkan angka A : ")
b = input("Masukkan angka B : ")

c = int(a) + int(b)
print(c)

#Kemudian ada juga float() untuk menginput bilangan pecahan.
#contoh : 
a = input("Masukkan angka A : ")
b = input("Masukkan angka B : ")

c = float(a) + float(b)
print(c)


#abs(). Dengan menggunakan fungsi abs() kita bisa hilangkan tipe data yang ada minusnya .
a = -5
c = abs(a)

print(c)

#pow(). Adalah fungsi untuk menghitung pangkat.
#contoh pow() statis :
c = pow(3,3)
print(c)

#contoh pow() dinamis
a = int(input("Masukkan Nilai : "))
b = int(input("Masukkan Nilai pangkat : "))

c = pow(a,b)
print(c)

#sqrt(). Fungsi untuk mencari akar kuadrat dari suatu pangkat.
#contoh sqrt() statis :
import math 

c = math.sqrt(36)
print(c)

#contoh sqrt() dinamis :
import math

a = input("Masukkan nilai : ")

c = math.sqrt(int(a))
print(c)

# Kemudian ada fungsi lain seperti max(), untuk menampilkan nilai paling akhir. min(),
# menampilkan nilai paling awal. round() atau ceil() untuk pembulatan keatas. Dan
# floor() untuk pembulatan kebawah.
print(max(5,1,2)) #output-nya 5

print(min(5,1,2)) #output-nya 1

print(round(5.8)) #output-nya 6

print(math.floor(5.8)) #output-nya 5

print(math.ceil(5.8)) #output-nya 6

#len(). Berfungsi untuk mengembalikan panjang (jumlah anggota) dari suatu objek
string = "Hello World"

print(len(string))

#index(). Mencari posisi suatu nilai.
kata = "Hello World"

print(kata.index("o"))

# count(). Menghitung kemunculan nilai tertentu.
# upper(). Mengubah string menjadi huruf kapital.
# lower(). Mengubah string menjadi huruf kecil.
# split(). Memisah string menjadi item

kata = "Hello World"

print(kata.count("o"))
print(kata.upper())
print(kata.lower())

kata_baru = kata.split(" ")
print(kata_baru)

# Range Slice.
# Range Slice menampilkan range karakter dari a mendekati b (limit b), yang
# diformulasikan dengan.
# nama_variabel[a:b]
# a = index karakter yang mulai dicetak.
# b = batas akhir karakter yang dicetak, b tidak dicetak atau kosongkan untuk mencetak
# sampai karakter terakhir.
kata = "HelloWorld"

print(kata[1:6])
print(kata[7:])

#List
# list kosong
my_list = []

# list berisi integer
my_list = [1,2,3,4,5]

# list berisi tipe campuran
my_list = [1, 3.5, "Hello"]

# list bersarang
my_list = ["hello", [2,4,6], ['a','b']]

# Mengakses Anggota List
# Kita bisa mengakses anggota list dengan menggunakan indeksnya dengan format
# namalist[indeks]. Indeks list dimulai dari 0. List yang memiliki 5 anggota akan
# memiliki indeks mulai dari 0 s/d 4. Mencoba mengakses anggota list di luar itu akan
# menyebabkan error IndexError.

my_list = ["saya","belajar","python","programing",2023]
#output saya
print(my_list[0])

#output python
print(my_list[2])

#list dalam list
your_list = ["hello",[1,2,3], "python"]

#output 1
print(your_list[1][0])

#output 3
print(your_list[1][2])

#output hello
print(your_list[0])

#indexError
print(my_list[6])

#list dengan indeks negatif 
# Python mendukung indeks negatif, yaitu urutan dimulai dari anggota terakhir. Indeks
# anggota paling belakang adalah -1, kemudian -2, dan seterusnya.
my_list = ['p','y','t','h','o','n']

#output n 
print(my_list[-1])

#output h
print(my_list[-3])

# Memotong (Slicing) List
# Kita bisa mengakses anggota list dari range tertentu dengan menggunakan operator
# slicing titik dua ( : ).
my_list = ['p','y','t','h','o','n','s','a','y','a']

#anggota list dari 3 s/d 5 (h s/d n)
print(my_list[3:6])

#anggota list dari 4 s/d terakhir
print(my_list[4:])

#anggota list dari 0 s/d 5
print(my_list[:6])

# Mengubah Anggota List
# List adalah tipe data yang bersifat mutable, artinya anggotanya bisa diubah. Ini berbeda
# dengan string dan tuple yang bersifat immutable.

#misal ada nilai yang salah 
ganjil = [1,3,4,7,9]
print("item awal : ", ganjil)

ganjil = [1,3,4,7,9]
print("item awal : ", ganjil)

#ubah item ke 3 (indeks ke-2)
ganjil[2] = 5
print("item yang diubah : ", ganjil)

#mengubah banyak item dengan satu baris kode
ganjil[2:5] = [11,12,13]
print("item ke-2 yang diubah : ",ganjil)

# Menambahkan Anggota List
# Fungsi append() berguna untuk menambahkan anggota ke dalam list. Selain itu, ada
# metode extend() untuk menambahkan anggota list ke dalam list.
# Kita juga bisa menggunakan operator + untuk menggabungkan dua list, dan operator *
# untuk melipatgandakan list.
ganjil = [1,3,5,7]

ganjil.append(9)
print(ganjil)
#output [1, 3, 5, 7, 9]

ganjil.extend([11,13,15])
print(ganjil)
#output [1, 3, 5, 7, 9, 11, 13, 15]

#menggabungkan list dengan operator
genap = [2,4,6]
print(genap + [8,10,12])
#output [2, 4, 6, 8, 10, 12]

print(['p','y'] * 2)
#output ['p', 'y', 'p', 'y']

# Menyisipkan Anggota List
# Fungsi insert() berfungsi untuk menyisipkan anggota list pada indeks tertentu.
ganjil = [5,7,11,13,15]

#emnyisipkan 9 setelah angka 7
ganjil.insert(2,9)
print(ganjil)
#output [5, 7, 9, 11, 13, 15]

# Kita bisa menggunakan metode remove(), pop(), atau kata kunci del untuk menghapus
# anggota list. Selain itu kita bisa menggunakan clear() untuk mengosongkan list.
# Fungsi pop() selain menghapus anggota list, juga mengembalikan nilai indeks anggota
# tersebut. Hal ini berguna bila kita ingin memanfaatkan indeks dari anggota yang
# terhapus untuk digunakan kemudian.

my_list = ['p','y','t','h','o','n','s','a','y','a']

my_list.remove('p')
print(my_list)
#output ['y', 't', 'h', 'o', 'n', 's', 'a', 'y', 'a']

my_list.remove('a') #remove hanya menghapus element pertama yang dijumpai
print(my_list)
#output ['y', 't', 'h', 'o', 'n', 's', 'y', 'a']

print(my_list.pop(1))
#output t

del my_list[2]
print(my_list)
#output ['y', 't', 'o', 'n', 's', 'y', 'a']

my_list.clear()
print(my_list)
#output []

# Mengurutkan Anggota List
# Pada saat kita perlu mengurutkan atau menyortir anggota list, kita bisa menggunakan
# metode sort(). Untuk membalik dengan urutan sebaliknya bisa dengan menggunakan
# argumen reverse=True.

alfabet = ['a','b','d','f','e','c','h','g','i']
alfabet.sort()
print(alfabet)
#output : ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

alfabet.sort(reverse=True)
print(alfabet)
#output : ['i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

# Membalik Urutan List
# Selain mengurutkan, kita juga bisa membalikkan urutan list dengan menggunakan
# metode reverse().

alfabet = ['d','a','c','b']
alfabet.reverse()
print(alfabet)
#output : ['b', 'c', 'a', 'd']