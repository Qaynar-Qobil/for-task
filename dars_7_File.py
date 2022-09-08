from os import system
system("cls")

import os


# def countFile(pathFile, file_count, dir_count):
#     for item in os.listdir(pathFile):
#         if (os.path.isfile(os.path.join(pathFile,item))):
#             file_count += 1

#         else:
#             dir_count += 1
#             [new_file_count, new_dir_count] = countFile(os.path.join(pathFile, item),0,0)
#             file_count += new_file_count
#             dir_count += new_dir_count

#     return [file_count, dir_count]

# my_location = "C:/Users/User/Desktop/My file.py"

# print(countFile(my_location,0, 0))

# ===================================================================================================================

                                                #        FILE

# trnt("Bunday fayl mavjud emas. ")                                                y:
#     fayl = open("new_text_file.txt", "r")
#     reat = fayl.read()
#     print(reat)
# except:
#     pri

# ===================================================================================================================
# try:
#     fayl = open("new_text_file.txt","r")
#     try:
#         reat = fayl.read()
#         print(reat)
#     except:
#         print("Faylni o'qisda qandaydir hatolik bor. ")
# except:
#     print("bunday fayl mavjud emas.")

# ===================================================================================================================
# fayl = open("new_text_file.txt", "r")

# reat = fayl.readline(5)
# print(reat)

# ===================================================================================================================
# fayl = open("new_text_file.txt", "r")

# reat = fayl.readlines(22)
# print(reat)
# fayl.close()

# ===================================================================================================================

# i = 0
# while i < 101:
#     with open(f"virus_{i}.py","w") as f:
#         f.write("text")
#         f.close()
#         i += 1
