# 8. Write a Python program to generate all permutations of a list in Python.

def factorial(num):
    if(num>0):
        num = num*factorial(num-1)
        return num
    else:
        return 1

n=int(input("Enter value of n : "))
r=int(input("Enter value of r : "))

x= factorial(n)
y= factorial(n-r)

Perm = int(x/y)

print("permutation : ",Perm)
