#Program 9) Write a Program to convert a list of characters into Strings

list1=[]
n=int(input("Enter the number of elements : "))
print ("insert your characters and press enter : ")
for i in range(0,n):
    ele=input()
    list1.append(ele)
    
#print("list is : ",list1)
mystring=''
for x in list1:
    mystring=mystring+''+x
    
print(mystring)
