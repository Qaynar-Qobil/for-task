from os import system
system ("cls")

from colorama import Fore



try:
    son = int (input("son kiriting: "))
    if (son == 7):
        son = son / 0
        
except:
    print("Faqat son kiriting: ")

else:
    print("Hammasi ok.")