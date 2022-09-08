# from asyncore import write

from os import system
system("cls")


                                                    #   1 Misol

# f = open(input("Fayl nomini kiriting: "),"w")
# f2 = open("new1.txt","w")
# f3 = open("new2.txt", "w")

# a = list(f.name.split("."))
# b = list(a[0])
# c = []

# for i in b:
#     i = int(i)
#     c.append(i)
# c.sort()

# for i in c:
#     i = str(i)
#     f2.write(i )
# c.reverse()

# for i in c:
#     i = str(i)
#     f3.write(i )

# ==================================================================================================================

                                                            #   2  Misol

# f = open(input("Fayl nomini kiriting: "),"w")
# f2 = open("new1.txt","w")
# f3 = open("new2.txt", "w")

# a = f.name.split(".")
# b = list(a[0])
# b.sort()

# # c = ""

# for i in b[1:]:
#     f3.write(i)
# b.reverse()

# for i in b:
#     f2.write(i)
    
# ==================================================================================================================
                                                         
                                                            #   3  Misol

# with open("file.txt","r") as f:
#     fayl = f.read().split("N")
#     fayl2 = fayl[1].split()
#     fayl3 = fayl2[1].split(".")
#     fayl3.insert(0,fayl2[0])
#     # summa = 0
#     fayl4 = []

#     for i in fayl3:
#         i = int(i)
#         fayl4.append(i)

#     # print(fayl4)
#     print(f"{fayl3[0]} + {fayl3[1]} + {fayl3[2]} + {fayl3[3]} = {sum(fayl4)}")

# ==================================================================================================================
                                                    
                                                            #    4  Misol

with open("fayl_2.txt","r") as f:
    harf = f.read()
    # print(harf.count(harf))
    for i in harf:
        print(harf.count(i[0:]))
