# 11. Write a Python program to get the frequency of the elements in a list

# version 1

input_string = input("Enter Your String : ")
frequencies = {} 
  
for char in input_string: 
   if char in frequencies: 
      frequencies[char] += 1
   else: 
      frequencies[char] = 1
      
print ("Per char frequency in '{}' is :\n {}".format(input_string, str(frequencies)))
