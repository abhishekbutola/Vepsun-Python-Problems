# i/p : abc
#       xyz
#o/p  : xbc ayz

str1=input ("Enter your string \n")
str2=input ("Enter your string \n")
temp=str1[0]
str1=str1.replace(str1[0],str2[0])
str2=str2.replace(str2[0],temp)
print("String 1 = ",str1)
print ("String 2 = ",str2)
