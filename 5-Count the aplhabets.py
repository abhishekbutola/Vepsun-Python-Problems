"""
Sample String : google.com'
Expected Result : {'o': 3, 'g': 2, '.': 1, 'e': 1, 'l': 1, 'm': 1, 'c': 1}
"""
k=[]
count = 0
str1=input("Sample String : ")
k=list(str1)

l=len(k)

for i in range(l):
    for j in range(l):
        if (k[i]==k[j]):
            count=count+1
    print (' %s : '%k[i],count,end="")
    print()
    count =0

