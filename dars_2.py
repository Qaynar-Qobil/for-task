from os import system
system("cls")



# x = 4.5
# y = 4.5

# print(x is y)  # ikkita qiymat o'zaro tengligini tekshiradi
# "====================================================================="

# word = "bugun dars kech boshlandi"
# let = "a"

# print(let in word) # kiritilgan belgi yoki satrni ikkinchi satrda bor yoki yoqligini tekshiradi

# "======================================================================="

# word = "salom aka"
# let = "akam"
# print(let[0:3] in word)
# "======================================================================="

# print(4>2 and 5>1)
# print(4>2 and (5>1 or 6>9) and 9<0)

# print("b">"a")
# "======================================================================="

# print("salom" not in "s" and 4<7) 

# "======================================================================="


# IF ELSE

# son = int(input("Son kirit: "))

# if (son==0):
#     print("Nol")
# elif (son==1):
#     print("Bir")
# else:
#     print(f"Bu {son} soni")

# "======================================================================="

# son = int(input("Son1: "))
# son2 = int(input("Son2: "))

# if (son%2==0 and son2%2==0):
#     print("Ikkalasityam juft")
# elif(son%2!=0 and son2%2!=0):
#     print("Ikkalasiyam toq")
# elif(son%2==0):
#     print("Faqat birinchisi juft")
# elif(son2%2==0):
#     print("Faqat ikkichisi juft")
# elif(son%2!=0):
#     print("Faqat birinchisi toq")
# elif(son2%2!=0):
#     print("Faqat ikkichisi toq")
# # "======================================================================="


# if ("S".lower() == input("Ism kirit: ")[0].lower()):
#     print("Ism s harfidan boshlanadi")

# # "======================================================================="

# son = int(input("Son: "))

# if (len(str(son))==2):
#     if (son%2==0):
#         print("Son ikki honali va juft")
#     else:
#         print("Son ikki honali va Toq")
# # "======================================================================="

# son = int(input("Son: "))

# if(son%2==0):
#     print("Juft")
# if(len(str(son))==2):
#     print("Ikki honali")
# else:
#     print(f"Son {len(str(son))} xonali")

# # "======================================================================="
# import os
# import time

# son = int(input())

# while (son>0):
#     print(son)
#     son-=1
#     time.sleep(0.5)
#     os.system("cls")
# # "======================================================================="

# word = "schsb1chb"
# cnt = 0
# print(word.count("s"))
# new_word = ""

# while cnt<len(word):
#     if word[cnt] not in new_word:
#         new_word+=word[cnt]
#     cnt+=1

# print(new_word)

# # "======================================================================="

# word = "salomlarsa"
# cnt = 0

# new_word = ""

# while cnt<len(word):
#     if word.count(word[cnt])>1 and word[cnt] not in new_word:
#         print(word[cnt])
#         new_word+=word[cnt]
#     cnt+=1

# print(new_word)

# "======================================================================="

# word = "salomlarsa"
# cnt = 0

# new_word = ""

# while cnt<len(word):
#     if word[cnt] not in new_word:
#         print(word[cnt]+"-"+str(word.count(word[cnt])))
#         new_word+=word[cnt]
#     cnt+=1

# print(new_word)

# "======================================================================="


# for i in range(0,10,1):
#     if(i==3):
#         i+=4
#     print(i)
# "===================image.png===================================================="

# for x in "salom":
#     print(x)

# "===================image.png===================================================="
# x = range(0,6)
# print(x)

# for x in range(4,9,2):
#     print(x)

# "===================image.png===================================================="

# word = "salom aka bugun oqishga boraolmadim"

# for v in range(0,len(word)):
#     print(word[v])

# for v in word:
#     if(v=='b'):
#         continue
#     print(v)

# "===================image.png===================================================="

# word = "Salom aka Bugun OqishgA Boraolmadim Aka"
# word = word.strip()
# word = word+" "
# new_let = ""
# ctn = 0

# for indx in range(len(word)):
#     if (word[indx]==" "):
#         if (new_let[0].isupper()):
#             print(new_let)
#         new_let = ""
#     else:
#         new_let+=word[indx]


