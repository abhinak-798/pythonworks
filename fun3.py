#1.Write a program to find the position of a character in a string
# a=input("enter a string:")
# ch=input("enter character:")
# print(a.index(ch))

# a=input("enter a string:")
# ch=input("enter character:")
# if ch in a:
#     print(a.find(ch))
# else:
#     print("character not present")

#2.write a program to find the count of character in  a string
# a=input("enter a string:")
# ch=input("enter character:")
# print(a.count(ch))

# s=input("enter a string:")
# ch=input("enter a character:")
# if ch in s:
#     print(s.count(ch))
# else:
#     print("character not present")

#3.create a random 5 digit otp number and print otp number
# import random
# print("OTP:",random.randint(10000,99999))

# import random
# otp=random.randint(10000,99999)
# print(otp)

#4.create a list of  5 random 3 digit numbers
# import random
# new=[]
# for i in range(5):
#     num=random.randint(100,999)
#     new.append(num)
# print(new)

# import random
# new=[]
# for i in range(1,6):
#     num=random.randint(100,999)
#     new.append(num)
# print(new)

#5.create a dictionary where keys are words and values are length of each word from the string
#new={'python':6,'coding':6,'is':2,'easy':4,'and':3,'fun':3}
#s="python coding is easy and fun"
# new={word:len(word) for word in s.split()}
# print(new)

# new={}
# for i in s.split():
#     new[i]=len(i)
# print(new)

#6.*create a dictionary where keys are each character and values are number of occurence of each character
#s="hello world"
#d={'h':1,'e':1,'l':3,'o':2,'':1,'w':1,'r':1,'d":1'}
# new={ch:s.count(ch) for ch in s}
# print(new)

# new={}
# for i in s:
#     if(i!=" "):
#         new[i]=s.count(i)
# print(new)

#7.write a program to find the number of digits,letters,and spaces in a string
#s="sdfghjk3456789  dffghjkl345678"
# digit=0
# letter=0
# space=0
# for i in s:
#     if(i.isdigit()):
#         digit=digit+1
#     elif(i.isalpha()):
#         letter=letter+1
#     elif(i.isspace()):
#         space=space+1
# print("digit:",digit)
# print("letter:",letter)
# print("space:",space)

#8.Given a list
#l=[['amal',23,30000],['arun',25,50000],['anu',24,40000]]
# create a list of salaries
# new=[i[2] for i in l]
# print(new)

# new=[]
# for i in l:
#     new.append(i[2])
# print(new)

# find the maximum salary
# new=[i[2] for i in l]
# print(max(new))

# new=[]
# for i in l:
#     new.append(i[2])
# print(max(new))

# find minimum salary
# new=[i[2] for i in l]
# print(min(new))

# new=[]
# for i in l:
#     new.append(i[2])
# print(min(new))

#Given a dictionary
#d={'arun':34,'amal':45,'anu':40,'kiran':25,'manu':30}
# create a new list of students whose mark>=40
# new=[]
# for i in d:
#     if(d[i]>=40):
#         new.append(i)
# print(new)

# Given two lists
# l1=[11,27,34,45,56]
# l2=[27,34,86,91]
# Find Common elements
# new=[]
# for i in l1:
#     if i in l2:
#         new.append(i)
# print(new)

# s1=set(l1)
# s2=set(l2)
# print(s1.intersection(s2))

#Given
#l=[23,45,67,12,90,56]
#find second largest number
# l.sort()
# print(l[-2])

#find second smallest number
# l.sort()
# print(l[1])

#combine two list without duplicates
# l1=[11,27,34,45,56]
# l2=[27,34,86,91]
#
# s1=set(l1)
# s2=set(l2)
# print(s1.union(s2))

# d={'a':10,'b':20}      #print a 10
# for i,j in d.items():        #b 20
#     print(i,j)


# num=7
# i=1
# while(i<=10):
#     print(num,'*',i,'=',num*i)
#     i=i+1


