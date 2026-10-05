#LIST COMPREHENSION
#l=[1,2,3,4]
# new=[i**2 for i in l]
# print(new)

# new=[5 for i in l]
# print(new)

#given a list
#l=[12,45,34,67]
#create new list with even values
# new=[i for i in l if i%2==0 ]
# print(new)

#create a new list with values greater than 50
# new=[i for i in l if i>50]
# print(new)

#given a list
#colours=['red','green','blue','orange']
#create a new list with first letter of each colour
# new=[colour[0] for colour in colours]
# print(new)

#create a new list with length of each colour
# new=[len(colour) for colour in colours]
# print(new)

#create a new list with square root of each element
#l=[25,16,9,36]
# new=[i**0.5 for i in l]
# print(new)

#given a dictionary
#d={'arun':25,'amal':34,'akhil':26,'anu':21}
# #create a list of names
# new=[i for i in d]
# print(new)

# create a list of marks
# new=[i for i in d.values()]
# print(new)

#given a list
#l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']
#create a list of string values
# new=[i for i in l if type(i)==str]
# print(new)

# Create a list of float values
# new = [i for i in l if type(i)==float]
# print(new)

# #create a list of positive numbers
#l = [23, 56, 12, 89, -34, -23, -67, -43, 9.7, 4.5, 'hello', 'world']
# new= [i for i in l if type(i)!=str and i> 0]
# print(new)

# #given a list
#fruits = ['apple', 'orange', 'pineapple', 'avocado', 'grapes']
# # Create a new list with elements whose length is greater than 6
# new= [i for i in fruits if len(i)>6]
# print(new)

# #create a new list with elements whose value is divisible by 3 in range(1,101)
# new=[i for i in range(1, 101) if i%3==0]
# print(new)

#given
#s="python coding is easy and fun"
# Create a list with only vowels
# new=[i for i in s if i in "aeiouAEIOU"]
# print(new)


#SET COMPREHENSION
#s="python coding is easy and fun"
#create a new set with only letters
# new={i for i in s if i!=" "}
# print(new)

#create a new set with only vowels
# new={i for i in s if i in "aeiouAEIOU"}
# print(new)

#create a new list with length of each word
# new={len(i) for i in s.split()}
# print(new)



#DICTIONARY COMPREHENSION
#l=[1,2,3,4]
# new={i:i**2 for i in l}
# print(new)

#Given a list,
#l=[10,20,30,40]
#create a new dictionary where keys are index of each number and values are numbers from not list
# new= {i:l[i] for i in range(len(l))}
# print(new)

#Given a string,
#string="python coding is easy and fun"
#create a new dictionary where keys are words and values are length of each word
# new={i:len(i) for i in string.split()}
# print(new)