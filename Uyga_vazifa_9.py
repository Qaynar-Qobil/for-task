# from os import system
# system("cls")


class Komanda:
    def __init__(self, nomi, ishtirokchilar_soni, trener, kapitan):
        self.nomi = nomi
        self.ishtirokchilar_soni = ishtirokchilar_soni
        self.trener = trener
        self.kapitan = kapitan

    def shovInfo(self) :
        print(f"""
        Nomi: {self.nomi}
        Ishtirokchilar_soni: {self.ishtirokchilar_soni}
        Trener: {self.trener}
        Kapitan: {self.kapitan}
        """)

    def get_name(self):
        return self.nomi

komanda1 = Komanda("Paxtakor", 15, "Shakar", "Abdulla")
komanda2 = Komanda("Bunyotkor", 12, "Bodom", "Botir")
komanda3 = Komanda("Archa", 30, "Bobur", "Qobil")
komanda4 = Komanda("Lakamativ", 11, "O'sha", "Burxon")
komanda5 = Komanda("Bog'bon", 8, "Olma", "Qodir")

all_komanda = [komanda1, komanda2, komanda3, komanda4, komanda5]

for i in range(len(all_komanda)):
    for j in range(len(all_komanda)):
        if ord(all_komanda[i].nomi[0]) < ord(all_komanda[j].nomi[0]):
            all_komanda[i], all_komanda[j] = all_komanda[j], all_komanda[i]

for i in all_komanda:
    i.shovInfo()
    print("===============================================")



            

# =================================================================================================================

# class Kitob:
#     def __init__(self,nomi, muallifi, narxi, nashriyoti):
#         self.nomi = nomi
#         self.muallifi = muallifi
#         self.narxi = narxi
#         self.nashriyoti = nashriyoti

#     def showInfo(self):
#         print(f"""
#         Name: {self.nomi}
#         Author: {self.muallifi}
#         Prise: {self.narxi}
#         Publisher: {self.nashriyoti}
#         """)

# kitob1 = Kitob("Tanlangan Asarlar", "Lev Tolstoy", 570000, "Andijon")
# kitob2 = Kitob("Ufq", "Said Ahmad", 100000, "Buxoro")
# kitob3 = Kitob("O'tkan Kunlar", "Abdulla Qodiriy", 150000, "Dushanbe")
# kitob4 = Kitob("Kecha va Kunduz", "Cho'lpon", 90000, "Farg'ona")
# kitob5 = Kitob("Oliver Tvist", "Mark Tvin", 60000, "fuliston")

# all_kitob = [kitob1, kitob2, kitob3, kitob4, kitob5]

# for kitob in all_kitob:
#     if (kitob.nashriyoti[0].lower() == "a" or kitob.nashriyoti[0].lower() == "f"):
#         kitob.showInfo()

#         print("======================================================")


# =================================================================================================================

# class Kompyuter:
#     def __init__(self, nomi, RAMi, narxi, protsessori):
#         self.nomi = nomi
#         self.RAMi = RAMi
#         self.narxi = narxi
#         self.protsessori = protsessori

#     def showInfo(self):
#         print(f"""
#         Name: {self.nomi}
#         RAM: {self.RAMi}
#         Cost: {self.narxi}
#         Prosessor: {self.protsessori}     
#         """)

# Kompyuter1 = Kompyuter("Asus", 4, 3500000, "Intel cleron")
# Kompyuter2 = Kompyuter("HP", 6, 8000000, "cori 3")
# Kompyuter3 = Kompyuter("Mac Buc", 16, 15000000, "cori 16")
# Kompyuter4 = Kompyuter("Acer", 8, 6000000, "cori 5")
# Kompyuter5 = Kompyuter("Del", 10, 12000000, "cori 7")

# all_kompyuter = [Kompyuter1, Kompyuter2, Kompyuter3, Kompyuter4, Kompyuter5]

# for komputer in all_kompyuter:
#     if (komputer.RAMi >= 4 and komputer.RAMi < 15):
#         komputer.showInfo()
#         print("=====================================================================")