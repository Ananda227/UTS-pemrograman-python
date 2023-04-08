#=======================================
#      object oriented programing
#=======================================

#---------------- Kelas ----------------
class Marvel :
    pass

#object 
marvel1 = Marvel()
marvel2 = Marvel()
marvel3 = Marvel()

marvel1.name = "Iron Man"
marvel1.health = "1000"

marvel2.name = "Thor"
marvel2.health = "800"

marvel3.name = "Captain America"
marvel3.health = "900"

#pemanggilan
print(marvel1)
print(marvel1.__dict__)
print(marvel1.name)
#output : 
# <__main__.Marvel object at 0x00000189D78CE550>
# {'name': 'Iron Man', 'health': '1000'}
# Iron Man

#-------kelas dan objek sederhana-------
class Marvel :
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        
marvel1 = Marvel("Iron Man", 100, 10, 90)
marvel2 = Marvel("Thor", 90, 15, 100)
marvel3 = Marvel("Captain America", 120, 5, 150)

print(marvel1.name)
print(marvel2.health)
print(marvel3.__dict__)
#output :
# Iron Man
# 90
# {'name': 'Captain America', 'health': 120, 'power': 5, 'armor': 150}

#----variabel dan kelas sederhana ------
class Marvel :
    #class variabel
    jumlah = 0
    
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Marvel.jumlah += 1
        print("Hero Marvel dengan nama : " + inputName)
        
marvel1 = Marvel("Iron Man", 100, 10, 90)
print(Marvel.jumlah)
marvel2 = Marvel("Thor", 90, 15, 100)
print(Marvel.jumlah)
marvel3 = Marvel("Captain America", 120, 5, 150)
print(Marvel.jumlah)
#output :
# Hero Marvel dengan nama : Iron Man
# 1
# Hero Marvel dengan nama : Thor
# 2
# Hero Marvel dengan nama : Captain America
# 3

#-----------------Method---------------- 

class Marvel :
  
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        #instance variabel
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
    
    #void function
    def siapa(self):
        print("Namaku adalah " + self.name)
        
    #method dengan argumen
    def healthTambah(self, tambah):
        self.health += tambah
        
    #method dengan return
    def getHealth(self):
        return self.health
    
marvel1 = Marvel("Iron Man", 100, 10, 90)
marvel2 = Marvel("Thor", 90, 15, 100)
marvel3 = Marvel("Captain America", 120, 5, 150)

#pemanggilan method
marvel1.siapa()

#pemakaian method dengan argumen
marvel1.healthTambah(10)
print(marvel1.health)

#mengembalikan nilai dengan method
print(marvel1.getHealth())

#output :
# Namaku adalah Iron Man
# 110
# 110

#Game dengan OOP
class Marvel :
    
    def __init__(self, name, health, attackPower, armor) -> None:
        self.name = name
        self.health = health
        self.attckPower = attackPower
        self.armor = armor
        
    def serang(self, lawan):
        print(self.name + " menyerang " + lawan.name)
        lawan.diserang(self, self.attckPower)
        
    def diserang(self, lawan, attackPower_lawan) :
        print(self.name + " diserang " + lawan.name)
        attackDiterima = attackPower_lawan
        print("Serangan terasa : " + str(attackDiterima))
        self.health -= attackDiterima
        print("Health " + self.name + " tersisa  " + str(self.health))
        
marvel1 = Marvel("Iron Man", 100, 10, 90)
marvel2 = Marvel("Thor", 90, 15, 100)

marvel1.serang(marvel2)
#output :
# Iron Man menyerang Thor
# Thor diserang Iron Man
# Serangan terasa : 10
# Health Thor tersisa  80