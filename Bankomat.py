from os import system
system ("cls")

class Karta:
    def __init__(self,sery, password, balance):
        self.sery = sery
        self.__password = password
        self.__balance = balance

    def get_password(self):
        return self.__password

    def get_balanse(self):
        return self.__balance

    def set_balanse(self, money_amount):
        self.__balanse += money_amount

    def set_password(self, new_password):
        self.__password = new_password

class Odam:
    def __inti__(self, name, card):
        self.name = name
        self.__card = card

    def set_password(self, new_password):
        self.__card.set_password(new_password)

    def get_card(self):
        return self.__card

    def set_balanse(self, among_amount):
        self.__card.set_balanse(among_amount)

class Bankomat:
    def __init__(self, balance):
        self.__balance = balance

    def __check_password(self, card, password):
        if card.get_password() == password:
            return True
        return False

    def widthdraw_money(self, person, password, amount):
        card = person.get_card()

        if self.__check_password(card, password):
            if self.__balanse <= amount:
                return "Pulingiz Ko'pakanku"


        bank_taxi = amount * 3 // 100
        card = person.get_card()

        if card.get_balance() < bank_taxi:
            return print("Pulingiz yetarli emas. ")

        self.__balance += bank_taxi
        card.set_balance(-(amount + bank_taxi))

        print("Bank puli", self.__balance)

        return f"""sizming kartangizda {card.get_balance()} miqdorda pul qoldoi"""
    # else:
    #     return "Paswordingiz xato!!!"



card = Karta("1234 5678 9012 3214 412", 243, 100000)
person = Odam("John",card)

person.set_password(1243)

bank = Bankomat(1000000)

print(bank.widthdraw_money("Qaynar", 1243, 50000))
