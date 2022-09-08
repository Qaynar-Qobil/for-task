from os import system
system("cls")

# class User:
#     def __init__(self, fullname, age, username, passvord):
#         self.fullname = fullname
#         self.age = age
#         self.username = username
#         self.password = passvord

#     def user_info(self):
#         print(f"""
#         Username: {self.username}
#         Fulllname: {self.fullname}
#         Age: {self.age}
#         """)

# user1 = User("samad",34,"samad45","qwert45")
# user2 = User("ABdullo",12,"samad45","qwert45")
# user3 = User("Asadbek",18,"samad45","qwert45")
# user4 = User("Qodir",27,"samad45","qwert45")
# user5 = User("Bobur",11,"samad45","qwert45")
# user6 = User("Laziz",45,"samad45","qwert45")
# user7 = User("humoyun",35,"samad45","qwert45")

# users = [user1, user2, user3, user4, user5, user6, user7]

# for i in range(len(users)):
#     for j in range(len(users)):
#         users[i].age > users[j].age
#         # users[i].age,users[j].age = users[j].age, users[i].age
# for i in users:
#     i.user_info()

#     print("==================================================================")

# =========================================================================================================================================

# class First:

#     def madenewName(self, name):
#         return name.title()

# class Second(First):
#     def printName(self, name):
#         return self.madenewName(name)

# second1 = Second()
# print(second1.printName("Aziz"))

# =========================================================================================================================================


# class Person():

#     def __init__(self,name,surname,age):
#         self.name = name
#         self.surname = surname
#         self.age = age

#     def showInfo(self):
#         print(f"""         --
#         {self.name}
#         {self.surname}
#         {self.age}
#         --""")


# class Student(Person):
#     def __init__(self,name,surname,age,group):
#         self.group = group
#         Person.__init__(self,name,surname,age)

#     def showInfo(self):
#         Person.showInfo(self)
#         print(self.group)


# std1 = Person("Aziz","Raimov",45)
# std2 = Person("Abror", "Majidov", 23)

# all_std = [std1, std2]


# for i in all_std:
#     i.showInfo()
#     print("====================================================")

# =========================================================================================================================================

# from tabulate import tabulate

# class cars:
#     def __init__(self, model, color, prise, horsepower):
#         self.model = model
#         self.color = color
#         self.prise = prise
#         self.horsepower = horsepower

#     def returninfocar(self):
#         return {
#         "Modeli": self.model,
#         "Rangi": self.color,
#         "Narxi": self.prise,
#         "Horsepower": self.horsepower
#         }

# class Truck(cars):
#     def __init__(self,  model, color, prise, horsepower, capasity, weight):
#         super().__init__(model, color, prise, horsepower)
#         self.capasity = capasity
#         self.weight = weight

#     def returninfocar(self):
#        new_dct = super().returninfocar()
#        new_dct.update({"capasity":  self.capasity, "weight": self.weight})
#        return [new_dct]

#     def showTrukInfo(self):
#         print(tabulate(self.returninfocar(), headers= "keys"))

# class lightCar(cars):
#     def __init__(self, model, color, prise, horsepower, weight, max_score, typeCar):
#         self.weight = weight
#         self.max_score = max_score
#         self.typeCar = typeCar

#         super().__init__(model, color, prise, horsepower)

#     def returninfocar(self):
#         new_dct = super().returninfocar()
#         new_dct.update({"typeCar": self.typeCar, "weight": self.weight, "max_score": self.max_score})
#         return [new_dct]

# objTruck1 = Truck("Man", "White", "120.000$", 220, 4300, 9)
# objTruck2 = Truck("Mersedes", "Blue", "300.000$", 450, 5600, 10)

# all_cars = []

# for car in [objTruck1, objTruck2]:
#     all_cars.append(car.returninfocar()[0])

# objlightCar = lightCar("Tesla", "black", "70.000$", "180", "1", "200", "Electro car")
# print(tabulate(objlightCar.returninfocar(),headers="keys"))



# son = int(input("son: "))
# for i in range(1, 2*son):
#     for j in range(1, 2*son):
#         if abs(son - i) + 1 <= abs(son - j) + 1:
#             print(abs(son - j) + 1, end=" ")
#         else:
#             print(abs(son - i) + 1, end=' ')

#     print()