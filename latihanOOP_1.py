
import os 
#eksekusi 
class Hero : 
    count1 = 0 

    plus_attack = 0 

    def __init__(self,name,health,attackPower,Armorpower) -> None : 
        self.name = name 
        self.health = health
        self.attackPower = attackPower 
        self.armor = Armorpower 
    
    def serang(self,lawan) : 
        print(f"{self.name} menyerang {lawan.name}\n====================")
        lawan.diserang(self,self.attackPower)
        

    def diserang (self,lawan,attackPower_lawan) : 
        print(f"{self.name} diserang {lawan.name}\n====================")
        attack_diterima = attackPower_lawan/self.armor
        print(f"serangan yang diterima dari {lawan.name} = {attack_diterima:.2f}\n")
        self.health-= attack_diterima 
        print(f"sisa darah {self.name} = {self.health:.2f}\n")


 #input nama hero dari user       
os.system("cls")
hero1 = input("berikan nama untuk hero 1 di game ini = ")
hero2 = input("berikan nama untuk hero 2 di game ini = ")
hero1_1 = Hero(hero1,100,50,40)
hero2_2 = Hero(hero2,100,68,44)

#looping 
while True :
    os.system("cls")
    user = str(input(f"kamu mau {hero1}/{hero2} menyerang siapa = "))
    if user == hero1 : 
        hero2_2.serang(hero1_1)
    elif user == hero2 : 
        hero1_1.serang(hero2_2)

    user2 = input("apakah mau melanjutkan permainan ini ? (y/n) = ")
    if user2 == "n" : 
        break
    

   




 

    