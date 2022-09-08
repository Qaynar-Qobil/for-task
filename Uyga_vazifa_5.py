from os import system
system("cls")

                                                                #   1 Misol


# def printNumbers(num):
#     summa = 0
#     for i in range(1,num + 1):
#         summa = summa + pow(i,i)
#         print(f"{i}^{i}",end="")
#         if num == i:
#             print(end=" = ")
#         else:
#             print(end=" + ")

#     print(summa)

# son = int(input("son: "))
# printNumbers(son)






# =============================================================================================================

                                                                # 2 Misol

# son = int(input("son: "))
# for i in range(1,son + 1):
#     if i == 18:
#         print(f"Sizning yoshingiz {i} ga teng.")
#     else:
#         print(i)
        

# ===========================================================================================================

# def chekDivider(number1 = 32, number2 = 2):
#     while(1):
#         if(number1 == number2):
#             return 1

#         elif(number1 - number2 < number2):
#             return 0
    
#         number1 = number1 - number2


# def chekPrime(number):
#     counter = 0
#     for i in range(1,number):
#         if (chekDivider(number,i)):
#             counter += 1

#     if counter > 1:
#         return 0
#     else:
#         return 1

# son = int(input("son: "))
# for i in range(1,son + 1):
#     if (chekPrime(i)):
#         print(i)




            
    
# ===========================================================================================================

                                                #   4 Misol

# for i in range(100,1000):
#     i = str(i)
#     if i.count(i[0]) == 2 or i.count(i[1]) == 2:
#         print(i)


def numbers(number):
    number = str(number)
    for i in number:
        if (number.count(i) == 2):
            return 1

    return 0


for i in range(100,1000):
    if (numbers(i)):
        print(i)

   
    
        
    
            
          
         
        
        
        
        