
def convert_morze(word):
    word = word.upper()
    char_to_dots = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
    ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
    '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }


    for i in word:
        for j in char_to_dots:
            if i == j:
                print(char_to_dots[j],end=" ")


soz = input("Soz kiriting: ")

convert_morze(soz)

"========================================================================================================="

# def shu(son):
#     if son>0:
#         for i in range(1,son+1):
#             print((son-i)*'_'+(i)*'#')
#     elif son<0:
#         son=-1*son
#         for i in range(son):
#             print((i)*'_'+(son-i)*'#')



# son = int(input("Son:"))

# shu(son)

"========================================================================================================="

# def input_kod():
#     kod = input("Kodni kiriting(16 atlik):")
#     lst = []
#     if len(kod)==16:
#         for i in kod:
#             lst.append(int(i))
#     else: input_kod()
#     return lst
    

# def check_valid(lst):
#     sum = 0
#     kum = 0
#     for i in range(16):
#         cum = 0
#         if i%2==1:
#             sum+=lst[i]
#         else:
#             a=lst[i]*2
#             a=str(a)
#             for j in range(len(a)):
#                 cum += int(a[j])
#             kum+=cum

#     if (sum+kum)%10==0:
#         return 'VALID'
#     else:return 'INVALID'
    

# print(check_valid(input_kod()))





"========================================================================================================="



"========================================================================================================="



"========================================================================================================="
