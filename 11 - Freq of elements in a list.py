#Write a Python Program to get the frequency of element in a list

a=[]
count =0;
n=int(input("insert number of items in a list : "))
for i in range(n):
    k= input("\nEnter your data : ")
    a.append(k)
print("\nYour List items : ",a)
for j in range(n):
    for k in range(n):
        if (a[j]==a[k]):
            count = count +1;
    print ("\nCount of %s is : %d"%(a[j],count))
    count =0;
