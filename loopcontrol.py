#BREAK
#s="hello"
# for i in s:
#     if(i=='l'):
#         break
#     print(i)

#CONTINUE
# for i in s:
#     if(i=='l'):
#         continue
#     print(i)

#GIVEN A LIST
#colours=['red','green','blue','yellow','black','orange']
#PRINT EACH COLOUR
# for i in colours:
#     print(i)

#PRINT THE FIRST COLOUR STARTING WITH 'b'
# for i in colours:
#     if(i[0]=='b'):
#         print(i)
#         break

#PRINT ALL COLOURS EXCEPT COLOUR STARTING WITH 'b'
# for i in colours:
#     if(i[0]=='b'):
#         continue
#     print(i)

#PRINT THE FIRST COLOUR CONTAINS LETTER 'n'
# for i in colours:
#     if('n' in i):
#         print(i)
#         break

#PRINT ALL COLOURS EXCEPT COLOUR CONTAINS LETTER 'n'
# for i in colours:
#     if('n' in i):
#         continue
#     print(i)

# 1.CHECK WHETHER A NUMBER IS AN ARMSTRONG NUMBER
# num=int(input("enter a number:"))
# s=str(num)
# l=len(s)
# sum=0
# for i in s:
#     sum=sum+int(i)**l
# if(sum==num):
#     print("armstrong number")
# else:
#     print("not armstrong")

# 2.GIVEN A LIST
#l=[1,2,3,4]
# CREATE A NEW LIST WITH SQUARES OF EACH ELEMENT
# new=[]
# for i in l:
#     new.append(i**2)
# print("new list:",new)

# 3.GIVEN A LIST
#l=[12,67,59,23]
# CREATE A NEW LIST WITH ELEMENTS WHOSE VALUE IS GREATER THAN 50
# new=[]
# for i in l:
#     if(i>50):
#         new.append(i)
# print("new list:",new)

# 4.CREATE A NEW SET WITH ELEMENTS WHOSE VALUE IS GREATER THAN 50
# new=set()
# for i in l:
#     if(i>50):
#         new.add(i)
# print("new set:",new)

# 5.GIVEN A LIST
#l=[1,2,3,4]
# CREATE A NEW DICTIONARY WHERE KEYS ARE NUMBERS AND VALUES ARE SQUARES OF EACH NUMBER
# new={}
# for i in l:
#     new[i]=i**2
# print(new)

# 6.CREATE A LIST WITH 5 RANDOM NUMBERS
# new=[]
# for i in range(5):
#     n=int(input("enter a number:"))
#     new.append(n)
#     #print(new)
# print(new)

# 7.FIND THE FACTORS OF A NUMBER
# n=int(input("Enter a number: "))
# print("Factors are:")
# for i in range(1,n+1):
#     if(n%i==0):
#         print(i)

# 8.FIND THE FIBONACCI SERIES
# a=0
# b=1
# for i in range(1,11):
#     print(a)
#     a,b=b,a+b


# for i in range(1,11):
#     print(i)
# else:     #will execute after normal execution exit
#     print("hello")


# i=1
# while(i<=5):
#     print(i)
#     i=i+1
# else:
#     print("hello")


# for i in range(1,11):
#     if(i==5):
#         break
#     print(i)
# else:     #will execute when loop completes its iterations
#     print("hello")



#PRIME OR NOT
# num=int(input("Enter a number:"))
# if(num>1):        #if num is greater than 1
#     for i in range(2,num):        #[2,.....num-1]
#         if(num%i==0):
#             print("not prime")
#             break
#     else:
#         print("prime")
# else:     #if num is either 0 or negative
#     print("number is neither prime nor composite")

#CHECK WHETHER A NUMBER IS PERFECT OR NOT
# num=int(input("enter a number:"))
# sum=0
# for i in range(1,num):
#     if(num%i==0):
#         sum=sum+i
# if(sum==num):
#     print("perfect number")
# else:
#     print("not perfect")

