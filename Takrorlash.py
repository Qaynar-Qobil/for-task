
from os import system
system("cls")


# x = str("s1")
# r = str(3.8)
# d = str(2)

# print(x, r, d)

# ========================================================================= =============================================

# word = float(input("word: "))
# print(type(word))

# ========================================================================= =============================================
# yosh = 22

# print("Sizning yoshingiz", yosh, "da")
# print("sizning yoshhingiz %d da" % (yosh))
# print("sizning yishingiz {yoshh} da")
# print("sizning yoshingiz {1} da ismingiz: {0}".format ("Qaynar", (yosh)))

# ========================================================================= =============================================

# print(3*(3-7)+6*(2-3))
# ========================================================================= =============================================

# s =6     #  -5*-5*-5=25*-5=
# s//=3
# print(s)
# print()

# ========================================================================= =============================================

# str = "salom dunyo"
# print(str[len(str) // 2::] + " " + str[:len(str) // 2:])

# ========================================================================= =============================================

# name = 'Hafsa'
# age = 22
# print(name + ' ' + str(age)) 

# ========================================================================= =============================================

# a, b = input("ism: "), input("Familiya: ")
# print(f"Mening ismim {a} Familiyam {b}")

# ========================================================================= =============================================

# radius = int(input("radiusni aniqlang: "))
# s = radius ** 2 * 3.14
# p = 2 * 3.14 * radius

# print(f"Aylananing yuzi {s}")
# print(f"Aylananing radiusi  {p}")

# ========================================================================= =============================================

# stre = input("s: ")
# print(len(str(stre)))

# ========================================================================= =============================================

# str = input("so'z kiriting: ")
# son = int(input("s: "))
# # str = str[son:]
# print(str[son:])

# ========================================================================= =============================================

# word = input()
# n = int(input())
# print(word[::n])

# ========================================================================= =============================================

# son = input ("son: ")
# son = int(son[len(son) // 2:])
# son += 1
# print(son)

# ========================================================================= =============================================

# son = input("son: ")
# son = int(son[1::2]) / 10
# print(son)

# ========================================================================= =============================================

# word = "Salom haMmga qAlEsila"
# a = word.capitalize()
# print(a)

# ========================================================================= =============================================

# a = "Hello World H"
# a = a.replace("H", "S")
# print(a)

# ========================================================================= =============================================

# a = int(input())
# b = int(input())
# c = a + b
# print(a, '+', b ,'=', c)

# ========================================================================= =============================================

# word = "Salom \"Ozbekiston\""

# print(word)

# ========================================================================= =============================================


# a = int(input("v: "))
# b = int(input("b: "))
# if (a + b) % 2:
#     print("Qora")
# else:
#     print("Oq")

# ========================================================================= =============================================
 
# son = int(input("s: "))
# for i in range(0, son, 2):
#     print(son - i)

# ========================================================================= =============================================

# son = int(input("son: "))
# for i in range(son):
#     print(son - i)

# ========================================================================= =============================================
                                                        
# for i in range(100,1001):                          
#     i = str(i)
#     if i.count(i[0]) == 2 or i.count(i[1]) == 2:                  #   uch xonali sonlar orasidan 
#         print(i)                                                  # raqamlari takrorlanganlarini
                                                                  #    ekranga chiqarish


# def number(son):
#     son = str(son)
#     for i in son:
#         if son.count(i) == 2:
#             return 1

#         return 0

# for v in range(100, 1001):
#     if number(v):
#         print(v)

# ======================================================================================================================

# import random
# import os  
# import time
# import colorama


# for v in range(1, 100):
#     lst = [colorama.Fore.BLUE, colorama.Fore.GREEN, colorama.Fore.RED,
#     colorama.Fore.RESET, colorama.Fore.YELLOW, colorama.Fore.MAGENTA,
#     colorama.Fore.CYAN]
#     son = 20
#     for i in range(1, son + 1):
#         a = " " * (son - i)
#         b = "* " * i
#         print(random.choice(lst) + a + b)
#     time.sleep(0.05)
#     os.system("cls")

# ======================================================================================================================

# def alifbo(word):
#     word = word.upper()
#     Morsel = {
#         'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#     'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#     'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#     'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#     'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
#     '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#     '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#     '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
#     ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
#     '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
#     }

#     for i in word:
#         for j in Morsel:
#             if i == j:
#                 print(Morsel[j],end=" ")

# son = input("Input: ")
# alifbo(son)
# ======================================================================================================================

# lst = ["A","B","d","E","F","G","H","I","J","K","L","M","N","O","P","Q"]
# son = int(input())

# all_list = []
# mini_list = []

# for i in lst:
#     all_list.append(i)
#     if len(all_list) == son:
#         mini_list.append(all_list)
#         all_list = []

# if len(all_list):
#     mini_list.append(all_list)
#     print(mini_list)

# ======================================================================================================================

# myfamily = {
#   "child1" : {
#     "name" : "Emil",
#     "year" : 2004
#   },
#   "child2" : {
#     "name" : "Hemil",
#     "year" : 2007
#   },
#   "child3" : {
#     "name" : "Linus",
#     "year" : 2008
#   },
#   "child4" : {
#     "name" : "Torus",
#     "year" : 2001
#   }
# }

# for i in myfamily.keys():
#     if myfamily[i]["year"] >= 2001:
#         print(myfamily[i]["name"])

# ======================================================================================================================

# arr = [(1,2),(2,3),(3,4)]
# ans = []

# for i in arr:
#     a = list(i)
#     ans.append(a)

# print(ans)

# ======================================================================================================================

# dic = {1: 10, 2: 20, 3:30, 4: 15, 5: 25}
# for i, j in dic.items():
#     if min(dic.keys()) ==i:
#         print("min = ", i, j)

#     if max(dic.values()) == j:
#         print("max = ", i ,j)

# ======================================================================================================================

# arr = [(1,2),(2,3),(3,4)]
# ans = []
# for i in arr:
#     a = sum(list(i))
#     ans.append(a)

# print(ans)

# ======================================================================================================================

# def a():
#     return "salom"

# def b():
#     return a


# print(b()())


# ======================================================================================================================

# def katta(*arr):
#     return min(arr)

# print(katta(12,4,54,56,7,4,4,12))

# ======================================================================================================================

# import time
# import colorama
# import init


# son = int(input("Input: "))
# for i in range(1, son + 1):
#     if i == 22:
#         print((f"Mening yoshim {i} da"))
#         time.sleep(2)
#     else:
#         print(i)
#         time.sleep(0.05)
#         os.system("cls")

# ======================================================================================================================

# def printNumbers(num):
#    summa = 0
#    for i in range(1, num + 1):
#        summa = summa + pow(i,i)
#        print(f"{i} ^ {i}", end="")
#        if num == i:
#             print(end=" = ")
#        else:
#             print(end=" + ")

#    print(summa)
# son = int(input("Input: "))
# printNumbers(son)

# ======================================================================================================================

# def number(num):
#     num = str(num)
#     for i in num:
#         if i.count(i) == 2:
#             return 1

#         return 0

# for v in range(100,1001):
#     if number(v):
#         print(v)

# ======================================================================================================================

son = int(input("son: "))
for i in range(1,2*son):
    for j in range(1,2*son):
        if abs(son - i )+ 1 <= abs(son - j) + 1:    
            print(abs(son - j) + 1, end=" ")
        else:
            print(abs(son - i) + 1, end=" ")

    print()

# =======================================================================================================================

# import mysql.connector
# import os 

# os.system("cls")

# class Database:
#     def __init__(self, db_name):
#         self.connection = mysql.connector.connect(
#           host="localhost",
#           user="root",
#           password="salom777"
#         )
        
#         self.cursor = self.connection.cursor()
#         self.db_name = db_name

#         print("DATABASE INFO:")
#         self.__createDB()
#         self.__createTables()
#         print("---------------------------------------", '\n' * 2)
        
    
#     def __createDB(self):
#         self.cursor.execute(f"""
#             CREATE DATABASE IF NOT EXISTS {self.db_name};
#         """)
#         print(f"\"{self.db_name}\" database is created.")

#         self.cursor.execute(f"USE {self.db_name}")
#         print(f"connected from \"{self.db_name}\" database.")

#     def __createTables(self):
#         self.cursor.execute(f"""
#             CREATE TABLE IF NOT EXISTS users (
#               ID INT PRIMARY KEY AUTO_INCREMENT,
#               NAME VARCHAR(30) NOT NULL, 
#               USERNAME VARCHAR(30) UNIQUE
#             );
#         """)
#         print("users table created.")
    
#     def get_users(self, limit = -1):
#         self.cursor.execute(f"""
#             SELECT * FROM users;
#         """)

#         if limit < 0:
#             users = self.cursor.fetchall()
#         else:
#             users = self.cursor.fetchmany(limit)
    
#         self.connection.commit()
#         return users
        

#     def get_user(self, user_id = 1):
#         self.cursor.execute(f"""
#             SELECT * FROM users WHERE ID = {user_id};
#         """)

#         user = self.cursor.fetchone()
#         return user

# database = Database("foundation_60")
# users = database.get_users(10)
# user = database.get_user(4)

# print(user)

# ==============================================================================================================

# lst = [1, 2, [3, 5, [5, 6], [1, 6, [71, 1]], [95, 45, [53, [35]], 15], [1, 2, 3, [5, 6]]]]

# ans = str(lst).replace('[', '')
# ans = str(ans).replace(']', '')

# print(list(map(int, ans.split(','))))

# =============================================================================================================

# def Animals(animalName):
#     animals = ["dog", "cat", "bat", "cock", "cow", "pig",
#            "fox", "ant", "bird", "lion", "wolf", "deer", "bear",
#            "frog", "hen", "mole", "duck", "goat"]
    
#     checAnimals = []

#     for animal in animals:
#         count = 0
#         for hayvon in animal:
#             if hayvon in animalName:
#                 count += 1

#         if count == len(animal):
#             checAnimals.append(animal)

#     return " ".join(checAnimals)

# soz = input("So'z kiriting: ")
# print(Animals(soz))