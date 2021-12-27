# Program 10) Randomly pick a number from list
import random
print("This Program Randomly picks a number from the list \n")
list1=[]
n=int(input("enter the number of items : "))

print("\n Enter the values and press enter ")
for i in range(0,n):
    ele=int(input())
    list1.append(ele)
print("Your List : ",list1)

random_index = random.randint(0,len(list1)-1)

print("random number : ",list1[random_index])
