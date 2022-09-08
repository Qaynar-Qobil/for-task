
from os import system
system("cls")


# word = "olma"

# def printAllWords(word):
#     lst = []
#     for i in range(len(word)):
#         lst.append(word[i:]+word[:i])

#     return lst


# print(printAllWords(word))

# ============================================================================================================


# def shirflash(word):
#     for v in word:
#         # if(v.islover()):
#             print(chr(122 - (ord(v) - 97)),end="")

# shirflash('hello')

# ============================================================================================================

# def shirflash(word):
#     for v in word:
#         if v.islower():
#             print(chr(122 - (ord(v) - 97)),end="")
#         elif v.isupper():

#             print(chr(90 - (ord(v) - 65)),end="")


# soz = input("soz: ")
# shirflash(soz)

# ============================================================================================================

def findNearValue(lst, number):
    new_list = []
    min_value = abs(number - lst[0])

    for i in lst:
        if (abs(number - i) < min_value):
            min_value = abs(number - i)

    for j in lst:
        if (abs(number - j) == min_value):
            new_list.append(j)

    return new_list



lst = [23,55,2,4,65,24,67,8,5,2,54,34,21]
j = int(input("bos: "))
print(findNearValue(lst,j))

# ============================================================================================================

# def chekColum(lst):
#     for i in range()


# lst = [
#     [2,3,1,6,3,1,0]
#     [3,4,2,7,4,2,3]
#     [7,6,7,8,5,3,6]
#     [9,7,8,9,6,4,7]
# ]

# ============================================================================================================






