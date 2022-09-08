from os import system
from random import randrange
from secrets import randbelow
system ("cls")

                                    #   2 Misol

# son = []
# a = int(input())
# b = int(input())
# for i in range(a,b):
#     if i % 2 == 0:
#         son.append(i)

# print(son)
        
        
        
                                            #    3 Misol



# son = []
# a = int(input())
# b = int(input())
# for i in range(b,a,-1):
#     if i % 2 == 1:
#         son.append(i)

# print(son)
        
        

                                                #     4 Misol
                                                
list1 = ['salom', 123, True, 'Yoq', 'dunyo', 3.14, '7214']  
text = []
boshqa = []

for i in list1:
    if type(i) == str:
        text.append(i)
    else:
        boshqa.append(i)

text.sort()
boshqa.sort()
boshqa.reverse()
print(text)
print(boshqa)

                                                    #    8 Misol

# lst = "Salom bolalar. Anvarni qani?"
# lst = lst.split()

                                                    
                                                      
    
    
    


#                                     #  15 Misol
# a = [10,20,30,40]
# b = [100,200,300,400]
# b.reverse()
# for c in range(len(a)):
#     print(a[c], b[c])



                      #   6 Misol
# a="salom"; print(a[len(a)%2+1::]+a[:len(a)%2+1:])