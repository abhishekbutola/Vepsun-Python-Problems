#Write a Python program to shuffle and print a specified list.

import random
a=[]
n=int(input("Enter number of items : "))
for i in range(n):
    k=input()
    a.append(k)

print ("Your List items : ",a)

random.shuffle(a)

print (" The shuffled list is : ",a)
