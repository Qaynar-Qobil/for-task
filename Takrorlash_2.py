from csv import reader


all_words = []

with open("Forbidden_words.txt", "r") as fayl:
    readed = fayl.readlines()
    for vord in reader:
        if ("\n" in word):
            word = word.replase("\n", "")

        if (" " in word):
            
