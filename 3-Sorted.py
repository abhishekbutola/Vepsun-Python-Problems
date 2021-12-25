# i/p : red,yellow,red,green
# o/p : green,red,yellow

str1=input("Enter your String: ")
a=str1.split(",")
print("Your String: ",a)
b=set()
l= len(a)
for i in range(len(a)):
    b.add(a[i])
print ("Duplicate deletion :",b)
s=sorted(b)
print ("After sorting values :\t",s)

    

