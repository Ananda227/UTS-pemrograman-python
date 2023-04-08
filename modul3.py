#====================================================
#                      Tuple
#====================================================

#-------------------Membuat Tuple--------------------

#tuple kosong 
tuple1 = ()
print(tuple1)
#output : ()

#tuple 1 element
tuple1 = (1, )
print(tuple1)
#output : (1,)

#tuple 1 element
tuple1 = (1, )
print(tuple1)
#output : (1,)

#tuple berisi integer
tuple1 = (1,2,3)
print(tuple1)
#output : (1, 2, 3)

#tuple bersarang
tuple1 = ("hello", [1,2,3], (4,5,6))
print(tuple1)
#output : ('hello', [1, 2, 3], (4, 5, 6))

#tuple bisa juga tidak menggunakan tanda () berisi integer
tuple1 = 1,2,3
print(tuple1)
#output : (1, 2, 3)

#memasukkan anggota tuple ke variabel
a,b,c = tuple1
print(a,b,c)
#output : 1 2 3
#----------------------------------------------------

#---------------Mengakses Anggota Tuple--------------

tuple2 = ('p','y','t','h','o','n')
print(tuple2[0])
#output : p

print(tuple2[1])
#output : y

print(tuple2[-1])
#output : n

print(tuple2[-2])
#output : o

#index eror
# print(tuple2[6])

#___mengakses tuple dengan range___
print(tuple2[:3])
#output : ('p', 'y', 't')

print(tuple2[2:5])
#output :('t', 'h', 'o')

print(tuple2[2:])
#output : ('t', 'h', 'o', 'n')
#----------------------------------------------------

#---------------Mengubah Anggota Tuple---------------

# Setelah tuple dibuat, maka anggota tuple tidak bisa lagi diubah atau dihapus. Akan
# tetapi, bila anggota tuple-nya adalah tuple bersarang dengan anggota seperti list, maka
# item pada list tersebut dapat diubah.

tuple3 = (2,3,4,[5,6]) #hanya list "[]" didalam tuple yang dapat diubah

tuple3[3][0] = 7
print(tuple3)
#output : (2, 3, 4, [7, 6])

#tuple bisa diganti dengan penugasan kembali
tuple3 = ('p','y','t','h','o','n')
print(tuple3)
#output : ('p', 'y', 't', 'h', 'o', 'n')

#anggota tuple tidak bisa dihapus satu satu menggunakan del(),
# hanya bisa dihapus secara keseluruhan
del tuple3
# print(tuple3) => akan eror karena tuple3 sudah dihapus
#----------------------------------------------------

#---------------Menguji Anggota Tuple----------------

# Seperti halnya string dan list, kita bisa menguji apakah sebuah objek adalah anggota
# dari tuple atau tidak, yaitu dengan menggunakan operator in atau not in untuk
# kebalikannya.

tuple1 = (1, 2, 3, 'a', 'b', 'c')

#menggunakan in
print(3 in tuple1)
#output : True

print('3' in tuple1)
#output : False

print('c' in tuple1)
#output : True

#menggunakan not in
print('l' not in tuple1)
#output : True
#----------------------------------------------------

#------------------Iterasi pada Tuple----------------

#Kita bisa menggunakan for untuk melakukan iterasi pada tiap anggota dalam tuple.
nama = ('sistem', 'informasi')

for a in nama:
    print("hai",a)
#output : hai sistem
#         hai informasi

#----------------------------------------------------

#-----------Metode dan Fungsi Bawaan Tuple-----------
# Tuple hanya memiliki dua buah metode yaitu count() dan index().
# • Metode count(x) berfungsi mengembalikan jumlah item yang sesuai dengan x
# pada tuple.
# • Metode index(x) berfungsi mengembalikan indeks dari item pertama yang sama
# dengan x.
tuple1 = ('p','y', 't', 'h', 'o', 'n', 's','a', 'y', 'a')

#count
print(tuple1.count('a'))
#output : 2

#index
print(tuple1.index('n'))
#output : 5
#----------------------------------------------------
#====================================================
#                      Set
#====================================================

#-------------------Membuat Set----------------------
#set integer
set1 = {1,2,3}
print(set1)
#output : {1, 2, 3}

#set dengan menggunakan funsi set()
set1 = ([1,2,3])
print(set1)
#output :[1, 2, 3]

#set campuran 
set1 = {1,2.0,"python",(3,4,5)}
print(set1)
#output :{1, 2.0, (3, 4, 5), 'python'}

#bila terdapat duplikat set , set akan meghilangkan salah satu 
set1 = {1,1,1,2,2,2,3,3,3}
print(set1)
#output : {1, 2, 3}

#set kosong
set1 = set()
print(type(set1))
#output : <class 'set'>
#----------------------------------------------------

#----------------Mengubah angota set-----------------

#set tidak mendukung index dan slicing
#untuk menmanbah anggota kita bisa menggunakan fungsi add() dan update()

set_saya = {1,2,3}

#add() untuk menambah satu anggota
set_saya.add(4)
print(set_saya) 
#output : {1, 2, 3, 4}

#update() untuk menambah banyak anggota
set_saya.update([5,6,7,1,2,8])
print(set_saya) 
#output : {1, 2, 3, 4, 5, 6, 7, 8}


#----------------------------------------------------

#----------------Menghapus anggota set---------------
#membuat set baru
set_saya = {1,2,3,4,5,"Hallopython"}

#menghapus menggunakan fungsi discard()
set_saya.discard(4)
print(set_saya)
#output : {1, 2, 3, 5, 'Hallopython'}

#menghapus menggunakan fungsi remove()
set_saya.remove(3)
print(set_saya)
#output : {1, 2, 5, 'Hallopython'}

#menghapus dengan fungsi pop() "hapus random"
set_saya.pop()
print(set_saya)
#output : {2, 5, 'Hallopython'}   

#menghapus dengan funsi clear() "hapus all"
set_saya.clear()
print(set_saya)
#output : set()
#----------------------------------------------------

#--------------------Operasi set---------------------

#operasi gabungan(Union)
A = {1,2,3,4,5}
B = {4,5,6,7,8}

#menggunakan operator
print(A|B)
#output : {1, 2, 3, 4, 5, 6, 7, 8}

#menggunakan funsi union()
print(A.union(B))
print(B.union(A))

#operasi irisan(Intersection)
A = {1,2,3,4,5}
B = {4,5,6,7,8}

#menggunakan operator
print(A&B)
#output : {4, 5}

#menggunakan funsi intersection()
print(A.intersection(B))
print(B.intersection(A))
#output : {4, 5}
#         {4, 5}

#operasi selisih(Difference)
A = {1,2,3,4,5}
B = {4,5,6,7,8}

#menggunkan operator
print(A - B)
#output : {1, 2, 3}

#menggunakan fungsi difeerence()
print(A.difference(B))
print(B.difference(A))
#output : {1, 2, 3}
#         {8, 6, 7}

#operasi komplemen(symetric difference)
A = {1,2,3,4,5}
B = {4,5,6,7,8}

#menggunakan operator
print(A ^ B)
#output : {1, 2, 3, 6, 7, 8}

#menggunakan fungsi symetric_difference()
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))
#output : {1, 2, 3, 6, 7, 8}
#         {1, 2, 3, 6, 7, 8}
#----------------------------------------------------
#====================================================
#                    Dictionary
#====================================================

#----------------Membuat Dictionary------------------
# Dictionary dibuat dengan menempatkan anggotanya di dalam tanda kurung kurawal {},
# dipisahkan oleh tanda koma.
# Anggota dictionary terdiri dari pasangan kunci:nilai. Kunci harus bersifat unik, tidak
# boleh ada dua kunci yang sama dalam dictionary.

#dictionary kosong
dict1 = {}
print(dict1)

#dictionary dengan kunci integer
dict1 = {1:'sepatu', 2:'tas'}
print(dict1)
#output : {1: 'sepatu', 2: 'tas'}

#dictionary dengan kunci campuran 
dict1 = {'warna':'merah', 1 : [2,3,5]}
print(dict1)
#output : {'warna': 'merah', 1: [2, 3, 5]}

#dictionary menggunakan funsi dict()
dict1 = dict([(1,'sepatu'), (2,'bola')])
print(dict1)
#output : {1: 'sepatu', 2: 'bola'}
#----------------------------------------------------

#---------------Mengakses dictionary-----------------

dict_saya = {'nama' : 'budi', 'usia' : 27}

print(dict_saya['nama'])
#output : budi

#menggunakan get()
print(dict_saya.get('usia'))
#output : 27
#----------------------------------------------------

#-----------Mengubah anggota dictionary--------------

dict_saya = {'nama' : 'budi', 'usia' : 27}

#update
dict_saya['nama'] = 'Lelouch'
print(dict_saya)
#output : {'nama': 'Lelouch', 'usia': 27}

#menambah
dict_saya['agama'] = 'krislam'
print(dict_saya)
#output  : {'nama': 'Lelouch', 'usia': 27, 'agama': 'krislam'}
#----------------------------------------------------

#-----------Mengubah anggota dictionary--------------

dict_saya = {'nama': 'Lelouch', 'usia': 27, 'agama': 'islam', 'motto':'yang penting hidup'}

#menghapus anggota tertentu
print(dict_saya.pop('motto'))
#output  :yang penting hidup

#menghapus anggota acak
print(dict_saya.popitem())
#output : ('agama', 'islam')

print(dict_saya)
#output : {'nama': 'Lelouch', 'usia': 27}

del dict_saya['usia']
print(dict_saya)
#output : {'nama': 'Lelouch'}

#menghapus semua anggota
dict_saya.clear()
print(dict_saya)
#output = {}

#menghapus dictionary
del dict
