from os import system
system ("cls")

import calendar

txt = input().split()

[year, month] = [int(txt[0]), int(txt[1])]

cal = calendar.month(year, month)
cal = cal.split("\n")
cal = cal[1:]
cal[0] = "Du Se Ch Pa Ju Sh Ya"

for i in range(1, 4):
    string = ""
    for k in cal[i].split():
        if len(k) == 1:
            string += "0" + k + " "
        else:
            string += k + " "
    cal[i] = " " * (len(cal[i]) - len(string) + 1) + string

print("\n".join(cal))