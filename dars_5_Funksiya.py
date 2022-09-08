from os import system
system("cls")


dct = {
    23 : 12,
    34 : 67,
    45 : 60,
    90 : 11
}

# lst = list(dct.keys()) + list(dct.values())   #birinchi ususl
# print(max(lst))

son = 0

for i in dct:
    if son < i:
        son = i
        if son < dct[i]:                      #2 ususl
            son = dct[i]
print(son)




# data = [
#     {"V":"S001"},
# {"VI":"S002"},
# {"VII":"S009"},
# {"VII":"S008"},
# {"VI":"S005"},
# {"V":"S006"},
# {"VIII":"S007"},
# {"V":"S005"},
# {"VII":"S007"}
# ]

# lst = []
# for i in data:
#     [elem] = i.values()
#     lst.append(i)
    
# print(lst)

# for i in lst:
#     if lst.count(i) == 1:
#         print(i)
    
# ========================================================================================================================

# def funksiya_nomi(parametrlar):
#     pass

# def sumNumbers(a,b):
#     result = a+b
#     return result

# res = sumNumbers(4,5)






# from random import randint

# ret = randint(4,9)
# print(ret)

# ========================================================================================================================
 
# def sumAllNumbers(num,*items):
#     sumAll = 0
#     for v in items:
#         sumAll += v
#         return sumAll
    
    
# result = sumAllNumbers(1,2,3,4,5,6,7,8,9)
# ========================================================================================================================

# def printnums (num1, num2, *items):
#     print(num1)
#     print(num2)
#     print(items)
# printnums (1,2,3,4,5,6,7,8,9)

# ========================================================================================================================

# def max_Num (*num):
#     max_i = num[0]

#     for i in num:
#         if i > max_i:
#             max_i = i
#     return max_i

# print( max_Num(23,1,51,46,484,788,7,78))

# ========================================================================================================================

# def pagination(lst = [], size = 0):
#     all_list = []
#     mini_list = []
    
#     for v in lst:
#         mini_list.append(v)
#         if (len(mini_list) == size):
#             all_list.append(mini_list)
#             mini_list = []
#         if (len(mini_list) > 0):
#             all_list.append(mini_list)
#         return all_list
    
# lst = ("A","B","D","E","F","G","H","I","J","K","L")
# print(pagination)
            
        
            
    
    
    
    