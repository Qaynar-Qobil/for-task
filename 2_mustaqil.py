from os import system
system ("cls")


# x = int(input("x: "))
# y = int(input("y: "))

# if((x+y)%2==0):
#     print("Oq")
# else:
#     print("Qora")

# x = int(input("x: "))

# for x in range(10,100):
#     count = 0
#     for v in range(1,x):
#         if(x%v==0):
#             count+=1

#     if(count==1):
#         print(x)

# for son in range(100,1000):
#     son = str(son)
#     if son.count(son[0])==2 or son.count(son[1])==2:
#         print(son)


# ====================================================================================================================


import random
import os
import time
import colorama

for b in range(1,100):
    lst = [colorama.Fore.RED,colorama.Fore.BLUE,colorama.Fore.YELLOW,colorama.Fore.GREEN,colorama.Fore.CYAN]
    # x = random.randint(1,10)
    x = 10
    for v in range(1,x+1):
        prob = " "*(x-v)
        star = "* "*v
        print(random.choice(lst) + prob+star)
    time.sleep(1)
    os.system("cls")
    

    

# ---*
# --* *
# -* * *


# ====================================================================================================================

# a = 5
# b = 9

# a,b = b,a

# print(a)

# ====================================================================================================================


# [a,b] = input("2ta son kirit: ").split(" ")

# a,b = int(a),int(b)
# counter = 0

# while(b>a):
#     if (b%2==0) and counter!=3:
#         print(b)
#         counter+=1
#     b-=1


# ===========================================================================

# lst = [True, "Salom", 5, 5.6]
# lst2 = []


# for i in range(len(lst)):
#     print(type(lst[i]))

# ====================================================================================================================


# import random
# # import os
# # import time
# # import colorama


# son = int(input("s: "))
# lst = [random.randint(1,20) for i in range(son)]
# # for i in range(son):
#     # lst.append(random.randint(1,20))
# print(lst)

# print(min(lst))

# ====================================================================================================================

# lst = [5,6,8,7,2]
# lst2 = []
# lst2 = lst.copy()
# lst[0] = "A"
# print(lst2)
# print(lst)

# ====================================================================================================================


# lst = [3,5,6,7,4,2]

# print(lst.index(2))

# ====================================================================================================================


# tupl = (2,3,4,5,6,6)
# tpl = list(tupl)
# tpl[5] = "salom"
# tupl = tuple(tpl)
# print(tupl)