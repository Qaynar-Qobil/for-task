from os import system
system ("cls")

                                        #    SH A X M A D   #

# son = int(input("Qatorni kiriting: "))
# son2 = int(input("Ustunni kiriting: "))

# if (son + son2) % 2:
#     print("Qora")
# elif (son ):
#     print("Oq")

# ==================================================================================

                                    #    1 Misol
                                    #    2 Misol
                                    #    Ikkitasi birda.         

# son = int(input("Son kiriting: "))
# for i in range(0,son,2):
#     print(son - i)


# ==================================================================================

                                        #  4 Misol

# son = int(input("Tub tekshir: "))
# sum = 0
# for i in range(1,son + 1):
#     for j in range(1,i):
#         if i % j == 0:
#             print(i)
#             sum += 1
#         elif i % j == 1:
#             print(j)
            


# ==================================================================================

                                                #  5 Misol

# son = int(input("Son kirirting: "))                                                
# for i in range(son):
#     print(son - i)

# ==================================================================================

                                            #    6 Misol

son = int(input("SOn kiriting: "))
for i in range(1,son + 1):
    prob = " "*(son - i)
    start = "* " *i
    print(prob + start)

print()



# son = int(input("Son kiriting: "))
# for i in range(1,son + 1):
#     for j in range(1, i + 1):
#         if (i + j or j == i):
#             print('* ',end="")
#         else:
#             print(" ")

#     print()

            

    # pro = ''*(son - j)
    # start = "# " *j
    # print(pro + start)



# ==================================================================================

son = int(input('Son kirting: '))
while son > 0:
    if son == 0:
        print(son)
        son = son[:1:]
        son -= 1