# soz = "salom aka nima muammo yaxshimisizlar"
# soz = soz.split(" ")

# for i in soz:
#     if len(i)%2 == 1:
#         i = i[::-1]
#         print(i, end=" ")
#     else:print(i, end=" ")
        


import math

# son  = int(input("son: "))
kordinatalar = [
    {
        "name" : "Abbos",
        "x" : 45,
        "y" : 56,
    },
    {
        "name" : "Aziz",
        "x" : 34,
        "y" : 12
    },
    {
        "name" : "Abror",
        "x" : 22,
        "y" : 15
    },
]



s = []

x = 13
y = 39

for i in kordinatalar:
    d = math.sqrt(math.pow( x - i['x'], 2) + math.pow(y + i['y'], 2))
    s.append(d)

print(kordinatalar[s.index(min(s))])

                                                        # 12     56



