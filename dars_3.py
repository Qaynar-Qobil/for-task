# Listni elon qilish

# lst1 = []
# print(type(lst1))

# lst2 = list()
# print(type(lst2))
# "============================================================================================"

# lst = ["salom",4.5,9,True,[3,4]]
# for elem in lst:
#     print(f"{elem}- {type(elem)}")

# list elementlarini ekranga chiqarish
# "============================================================================================"
# lst = ["salom",4.5,9,True,[3,4]]
# for elem in range(0,len(lst)):
#     print(lst[elem])

# list elementlarini ekranga chiqarish
"============================================================================================"
# lst = [3,6,13,42,35,49,37,30]
# lst[8] = 17
# print(lst)

# list elementidan tashqaridagi elementni o'zgaritish mymin emas
"============================================================================================"
# lst = [3,7]

# lst.append(4)
# lst.append("salom")
# lst.append(True)
# lst.append(7.8)

# print(lst)

# listga elementni ohiridan qo'shish
"============================================================================================"

# lst = [[3,4],6,9,5.6,[4,5]]

# for v in lst:
#     if(type(v)==list):
#         print(v)

"============================================================================================"

# lst = list((4,6,3,7,67,4,9,67,4))
# print(lst)

"============================================================================================"

# lst = [2,3,5,2,4,3,4,5,5,5,3,5,3,4]
# print(lst[1::2])
# listdan elementlarni qirqib olish
"============================================================================================"
# lst = [2,3,5,2,4,3,4,5,5,5,3,5,3,4]
# print(lst[::-1])

# ohiridan boshiga teskari tartibda
"============================================================================================"

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[-4:-1])
# ['orange', 'kiwi', 'melon']
"============================================================================================"

# lst = ["salom","Aziz","Bobur","Salim"]

# if "Salim" in lst:
#     print("Salim listda bor")

# listda element borligini tekshirish
"============================================================================================"

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# print(thislist)
# thislist[1:4] = ["blackcurrant", "watermelon","Pinple"]
# print(thislist)

"============================================================================================"

# lst = ["Abror","Aziz","Sobir","Nozim"]
# lst.insert(2,"Qodir")
# print(lst)

# Listga index bo'yicha element kiritish
"============================================================================================"

# lst1 = [2,3,4,5,6,6]
# lst2 = ["as","df","as","df","as","df"]

# lst1.extend(lst2)
# print(lst2)
# List elementlarini birinchi listga qoshish
"============================================================================================"

# lst1 = [2,3,4,5,6,6]
# lst2 = ["as","df","as","df","as","df"]

# lst1 = lst1+lst2
# print(lst1)

# List elementlarini birinchi listga qoshish

"============================================================================================"

# lst = ["a","b","c"]
# print(lst*3)
# Listni songa ko'paytirish
"============================================================================================"
# import os

# lst = ["Cooper",
# "Emery",
# "Fleur",
# "Bryce",
# "Anabella",
# "Bevin",
# "Beverlie",
# "Doralia",
# "Ellissa",
# "Svend",
# "Wenona",
# "Freeman",
# "Sol",
# "Joan",
# "Gardener",
# "Willdon",
# "Johanna",
# "Tabor",
# "Cindie",
# "Zandra",
# "Eleonora",
# "Obed",
# "Brigit",
# "Jackelyn",
# "Chandal",
# "Josephine",
# "Rickie",
# "Simeon",
# "Tory",
# "Hanni",
# "Suzi",
# "Rozella",
# "Grete",
# "Junia",
# "Heall",
# "Esmaria",
# "Angelique",
# "Gonzales",
# "Hesther",
# "Avrom",
# "Ashby",
# "Terrye",
# "Caroline",
# "Tom"]

# while(1):
#     if input("Qidirasizmi: ") in ["Ha","ha","h","H"]:
#         os.system("cls")
#         word = input("Birikma kiriting: ")

#         for name in lst:
#             if word.lower() in name.lower():
#                 print(name)

#     else:
#         break

"============================================================================================"
# import random
# n = int(input("N: "))

# lst = []

# for v in range(n):
#     lst.append(random.randint(1,20))

# print(lst)

"============================================================================================"
# import random
# n = int(input("N: "))

# lst = [random.randint(1,20) for v in range(n)]
# print(lst)
# print(max(lst))
"============================================================================================"

# lst = ["salom","sa","salomlar"]
# print(min("salom","aka","salomlar"))

"============================================================================================"

# lst = [4,5,6,13]
# print(min(lst))
# print(min(2,4,5,6,5))

"============================================================================================"
# lst = [
#     "banan","olcha","nok","tarvuz",
#     "banan","Heall","Esmaria","Angelique","banan","Heall","Esmaria","Angelique"]
# # lst.remove("banan")
# # print(lst)
# word = input("Soz: ")

# for v in range(lst.count(word)):
#     lst.remove(word)

# print(lst)
"============================================================================================"
# lst = ["salom","sa","salomlar"]
# lst.pop(1)
# print(lst)
# Agar pop() ga index berilmasa ohirgisni ochiradi agar berilsa berilgan indexdagi
# elementni ochiradi.Agar listda yoq index berilsa error beriadi
"============================================================================================"

# num = 9
# lst = ["salom","sa","salomlar"]
# del num,lst # "berilgan o'zgaruvchini to'liq ochirib tashlaydi"
# print(lst)

"============================================================================================"

# lst = [4,3,3,6,4,5,6,7,7,7,8,8]
# print(lst)
# lst.clear() # Listni toliq tozalab beradi
# print(lst)

"============================================================================================"
# lst = [4,5,6,7,4,4,4,3,6]
# lst.sort(reverse=True)
# print(lst)

# lst = ["Anor","Olcha","Novvot","Qush","qush","Shakar"]
# lst.sort(key=str.lower)
# print(lst)
# Listni sortirovka qilish
"============================================================================================"
# lst = ["Olcha","Anor","Bodom"]
# lst.reverse()
# print(lst)
# Listni teskari tartibda chiqarish
"============================================================================================"

# lst = [3,4,5,6]
# lst1 = []

# lst1 = lst
# lst[0] = "A"
# print(lst1)
# print(lst)

# lst = [3,5,5,6,7,6]
# lst2 = []

# lst2 = lst.copy()
# lst[0] = "A"
# print(lst)
# print(lst2)

"============================================================================================"
# lst = ["salom","olcha","olma"]
# print(lst.index("olcha"))
# kiritilgan element indexini ko'rish
"============================================================================================"

# tupl = (3,4,6,5,6,3)
# print(tupl.index(3))
# # print(type(tupl))

# tupl = (3,4,6,5,6,3)
# print(tupl.count(3))
# print(type(tupl))

# tupl = (3,4,5,6,4,77,8,89,4)
# new_tuple = list(tupl)
# new_tuple[0] = "A"
# tupl = tuple(new_tuple)
# print(tupl)

"============================================================================================"
# lst = [3,4,5,6]
# lst = tuple(lst)
# print(lst)

"============================================================================================"
"============================================================================================"
