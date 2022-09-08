# def changeFirdtlatter(words, letter):
#     new_word = []
#     for i in range(len(words)):
#         new_word.append(letter[i]+words[i][1:])

#     return " ".join(new_word)


# def shiftsentense(sentense):
#     words = sentense.split(" ")
#     letter = [i[0] for i in words] 
#     letter.insert(0, letter[len(letter) - 1])
#     letter.pop(len(letter) - 1)
#     return changeFirdtlatter(words, letter)


# print(shiftsentense("create a functon"))


lst = ["cow", "cow", "pig", "cow"]
lst2 = []
lst2.append(lst)
for i in lst2:
    if lst not in lst2:
        print(lst2)


