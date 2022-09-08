from os import system
system("cls")


# class Student:
#     def __init__(self,name,age,clas):
#         self.ism = name
#         self.yosh = age
#         self.sinf = clas

#     def printinfoOFStudent(self):
#         print(f"""
#         name: {self.ism}
#         age: {self.yosh}
#         clas: {self.sinf}
#         """)

# Student1 = Student("Aziz",15,5)
# Student2 = Student("Qodir",45,5)

# Student1.printinfoOFStudent()
# Student2.printinfoOFStudent()

# ===============================================================================================

# import math

# class MyFunctions:
#     def __init__(self,number1,number2):
#         self.number1 = number1
#         self.number2 = number2
#         self.printSum()
#         self.printMinus()

#     def printSum(self):
#         print(self.number1 + self.number2)

#     def printMinus(self):
#         print(self.number1 - self.number2)

#     def printKvadrat(self):
#         print(math.pow(self.number1, self.number2))


# obj = MyFunctions(3,2)
# obj.printKvadrat()

# print(obj.printSum())
# print(dir(obj))

# ===============================================================================================

# class Kitob:
#     def __init__(self,nomi, narxi, muallifi, nashriyoti):
#         self.nomi = nomi
#         self.narxi = narxi
#         self.muallifi = muallifi
#         self.nashriyot = nashriyoti

#     def showInfo(self):
#         print(f"""
#         name: {self.nomi}
#         prise: {self.narxi}
#         tutor: {self.muallifi}
#         publish: {self.nashriyot}
#         """)

# Kitob1 = Kitob("O'tkan Kunlar", 98000, "Abdulla Qodiriy", "O'zbegim")
# Kitob2 = Kitob("Fizika", 27000, "Alisher Usmonov", "Aulin")
# Kitob3 = Kitob("Kecha va Kunduz", 100000, "Cho'lpon", "Burak")
# Kitob4 = Kitob("Oliver Twist", 95000, "Mark Twin", "Good")
# Kitob5 = Kitob("Ufq", 88000, "Said Ahmad", "Drink Print")

# all_books = [Kitob1, Kitob2, Kitob3, Kitob4, Kitob5]

# for book in all_books:
#     if (book.muallifi[0].lower() == "a"):
#         book.showInfo()

#         print("===================================================================================================")

# ======================================================================================================================================

class Kompyuter:
    def __init__(self,nomi, narxi, operativkasi, protsessori):
        self.nomi = nomi
        self.narxi = narxi
        self.operativkasi = operativkasi
        self.protsessori = protsessori

    def showInfo(self):
        print(f"""
        name: {self.nomi}
        narxi: {self.narxi}
        RAMi: {self.operativkasi}
        protsessori: {self.protsessori}
        """)

Kompyuter1 = Kompyuter("Asus", 3500000, 4, "Cori 3")
Kompyuter2 = Kompyuter("HP", 6000000, 6, "Cori 7")
Kompyuter3 = Kompyuter("MAC BUC", 10000000, 16, "Cori 9")
Kompyuter4 = Kompyuter("Del",11000000, 8, "Cori 5")
Kompyuter5 = Kompyuter("Acer", 9000000, 18, "Cori 6")

all_kompyuter = [Kompyuter1, Kompyuter2, Kompyuter3, Kompyuter4, Kompyuter5]

for i in range(len(all_kompyuter)):
    for j in range(len(all_kompyuter)):
        if (all_kompyuter[i].nomi[0]) < (all_kompyuter[j].nomi[0]):
            all_kompyuter[i], all_kompyuter[j] = all_kompyuter[j], all_kompyuter[i]
for i in all_kompyuter:
    i.showInfo()
    print("===============================================================")


 