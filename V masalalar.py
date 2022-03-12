# V6
"""
class Asl:
    def __init__(self, par1, par2, par3, par4, par5, par6, par7):
        pass
    def met1(self):
        pass
    def met2(self):
        pass
    def met3(self):
        pass
    def met4(self):
        pass
    def met5(self):
        pass
    def met6(self):
        pass
    def met7(self):
        pass
    """
 
 
 # V7
"""
class Car:
    def __init__(self, name, year, speed):
        self.name = name
        self.year = year
        self.speed = speed
        
    def start(self):
        pass
    def stop(self):
        pass
    def turn_right(self):
        pass
    def turn_back(self):
        pass
    
    def show(self):
        print(f"""
#        name:{self.name}
#       year:{self.year}
#        speed:{self.speed}
 #             """)
"""    
Malibu = Car("Malinu", "2002", "230")
Malibu.show()
"""

# V8
"""
class talaba:
    def __init__(self, ism, familiya, baxo):
        self.ism = ism
        self.familiya = familiya
        self.baxo = baxo
        
    def show(self):
        print(f"""
#        ism:{self.ism}
#        familiya:{self.familiya}
#        baxo:{self.baxo}
        
""")

box1 = talaba("Asliddin", "Abduraxmonov", 8)
box2 = talaba("Aizbek", "Qidirboyev", 10)
box3 = talaba("Asadbek", "Abdumavlonov", 9)

if box1.baxo > box2.baxo:
    box1.baxo = box2.baxo
    box1.ism = box2.ism
if box1.baxo > box3.baxo:
    box1.baxo = box3.baxo
    box1.ism = box3.ism 
box1.show()
"""     

# V9
"""
class Human:
    def __init__(self, name, age, profession, height, weight, single):
        pass
        
    def get_name(self):
         return self.name
     
    def get_age(self):
         return self.age
     
    def get_profession(self):
        return self.profession
     
    def get_height(self):
         return self.height
     
    def get_weight(self):
         return self.weight
     
    def get_single(self):
         return self.single 
"""


# V10
"""
class Bino:
    def __init__(self, balandligi, rangi):
        self.balandligi = balandligi
        self.rangi = rangi
        
    def show(self):
         print(f"""
#     balandligi:{self.balandligi}
#     rangi:{self.rangi}                         
""")

     
Hilton = Bino(100, "black")
Nest_one = Bino(80, "white")
Tower1 = Bino(40, "red")
Tower2 = Bino(30, "grey") 
Tower3 = Bino(80, "brown")


if Hilton.balandligi > 50:
    print(Hilton.rangi)
if Nest_one.balandligi > 50:
    print(Nest_one.rangi)
if Tower1.balandligi > 50:
    print(Tower1.rangi)     
if Tower2.balandligi > 50:
    print(Tower2.rangi)
if Tower3.balandligi > 50:
    print(Tower3.rangi)       
    
"""

# V11
"""
class Human:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        
    def full_name(self):
        return self.first_name + self.last_name
    
People = Human("Asliddin", "Abduraxmonov", 17)
print(People.full_name())
"""
    
# V12
"""
class Notebook:
    def __init__(self, firmasi, model, CPU, DDR, price):
        self.firmasi = firmasi
        self.model = model
        self.CPU = CPU
        self.DDR = DDR
        self.price = price
        
    def info_notebook(self):
        print(f"""
#        firmasi:{self.firmasi}
#        model:{self.model}
#        CPU:{self.CPU}
#        DDR:{self.DDR}
#        price;{self.price}
        
""")

kompyuter = Notebook("HP", " R8PSDF23", "Core I 5, Generation 11", "16 GB", "7000 $")
kompyuter.info_notebook()
"""
# V13
"""
class List:
    def __init__(self, my_list):
        self.my_list = my_list
        
    def delete_last_item(self):
        self.my_list.pop()
        
Nimadir = List([1, 2, 3, 4, 5, 6])
Nimadir.delete_last_item()
print(Nimadir.my_list)
"""


# V14
"""
class List:
    def __init__(self, numbers):
        self.numbers = numbers

    def delete_last_item(self):
        self.numbers.pop(0)
        
Nimadir = List([1, 2, 3, 4, 5, 6])
Nimadir.delete_last_item()
print(Nimadir.numbers)
"""

# V15
"""
class Car:
    def __init__(self, brands):
        self.brands = brands
        

    def brand_exist(self, objec):
        if objec in self.brands:
            return True 
        else: 
            return False

moshinalar = ["Mers", "Audi", "Nissan"]
ob = Car(moshinalar)
print(ob.brand_exist("Mer"))
"""
 
# V16
"""
class Clas:
    
    def get_string(self):
        self.soz = input("Biror so'z kiriting: ")
    
    def update_string(self):
        return self.soz[0].upper() + self.soz[1:-1] + self.soz[-1].upper()
    
Word = Clas()
Word.get_string()
print(Word.update_string())
"""


"""
# V17

class odam:
    def __init__(self, ism):
        self.ism = ism
    
    def salomlash(self):
        print(f"Salom {self.ism}")
        
human = odam(input())
human.salomlash()
"""

"""
# V18
class Rectangle:
    def __init__(self, eni, boyi):
        self.eni = eni
        self.boyi = boyi
    def get_parameter(self):
        print((self.eni + self.boyi) * 2)
    
    def get_area(self):
        print(self.eni * self.boyi)


tortburchak = Rectangle(4, 5)
tortburchak.get_parameter()
tortburchak.get_area()
"""


"""
# V19

class Aylana:
    def __init__(self, radius):
        self.radius = radius
        
    def aylana_uzunligi(self):
        return 2 * 3.14 * self.radius
    
    def aylana_yuzi(self):
        return 3.14 * pow(self.radius, 2)
    
    
shakl1 = Aylana(4)
print("Aylana uzunligi: ", shakl1.aylana_uzunligi())
print("Aylananing yuzi: ", shakl1.aylana_yuzi())
"""

"""
# V20

class odam:
    def __init__(self, ism):
        self.ism = ism
        
    def baqirish(self):
        print("Aaaayyyyyyy")

class kuchuk:
    def __init__(self, laqab):
        self.laqab = laqab
    def tishlash(self):
        human.baqirish()

human = odam("men")
dog = kuchuk("it")
dog.tishlash()
"""


"""
# V21
class Animal:
    def __init__(self):
        self.name = None
        self.age = None
        
    def eat(self):
        print("eat")

class Birds(Animal):
    def __init__(self):
        pass

owl = Birds()
owl.eat()
"""




"""
# V22
class Clas:
    def __init__(self, ism, familiya, yoshi, tugilgan_yili, ogirligi):
        pass
"""

"""
# V23
class Clas:
    def __init__(self):
        self.properti1 = None
        self.properti2 = None
        self.properti3 = None
"""
        


"""
# V24

class Clas:
    @staticmethod
    def show_salom():
        print("salom")



Clas.show_salom()
"""




"""
# V25
class Device:
    def __init__(self):
        self.properti1 = None
        self.properti2 = None
    
    def metod1(self):
        pass
    
    def metod2(self):
        pass
    
class Computer(Device):
    def __init__(self):       
        self.propert1 = None
        self.propert2 = None
        
    def metd1(self):
        pass
    
    def metd2(self):
        pass
    
class Phone(Device):
    def __init__(self):
        self.propert1 = None
        self.propert2 = None

    def met1(self):
        pass
    
    def met2(self):
        pass
    
class Desktop(Computer):
    def __init__(self):
        self.proper1 = None
        self.proper2 = None
    
    def me1(self):
        pass
    
    def me2(self):
        pass

class Laptop(Computer):
    def __init__(self):
        self.prope1 = None
        self.prope2 = None
        
    def m1(self):
        pass
    
    def m2(self):
        pass
    
class SmartPhone(Phone):
    def __init__(self):
        self.prop1 = None
        self.prop2 = None

    def method1(self):
        pass
    
    def method2(self):
        pass

class Tablet(SmartPhone):
    def __init__(self):
        self.pro1 = None
        self.pro2 = None
        
    def method3(self):
        pass

    def metdhod4(self):
        pass
"""


"""
# V26
class Human:
    def __init__(self, name, age, profession):
        self.adult_age = None
        self.age = age

    def is_adult(self):
        if self.age > 18:
            print("Voyaga yetgan")
        else:
            print("Voyaga yetmagan")


human1 = Human("Asliddin", 17, "programmer")
human1.is_adult()

human2 = Human("Mirjalol", 20, "programmer")
human2.is_adult()

human3 = Human("Anvarjon", 20, "programmer")
human3.is_adult()

human4 = Human("Shoxrux", 20, "programmer")
human4.is_adult()
"""



"""
# V27
class Odam:
    def __init__(self):
        self.raqam = None        
    def tepish(self):
        Koptok.uchish()


class Koptok:
    def uchish():
        print("Koptok uchyapti")

Zokir = Odam()
koptok = Koptok()
Zokir.tepish()
"""


"""
# V28
class Player:
    def __init__(self):
        self.jon = None
        self.qurol = None

    def otish(self):
        pass

    def reduce_life(self):
        pass
"""



"""
# V29
class Odam:
    def __init__(self):
        self.ism = None

    def Kuylash(self):
        print("Ish tayyor bo'ladi agar tayyor bo'sa soqqasi") 

    def Eshitish(self):
        self.Kuylash()

    def Gapirish(self):
        print("Yo'qol yalangoyoq")

Human1 = Odam()
Human2 = Odam() 

Human1.Kuylash()
Human2.Gapirish()
"""



























