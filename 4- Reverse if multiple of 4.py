#i/p  Juli    o/p iluJ


str1=input("Enter String \n")
l=len(str1)
if (l%4==0):
    for i in range(len(str1)) :
        print (str1[l-1],end="")
        l=l-1     
else :
    print (" String length %d is not a mutiple of 4"%l)
