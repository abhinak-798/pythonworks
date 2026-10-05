#FOR LOOP
# s="hello"
# for i in s:
#     print(i)

#PRINT EACH COLOURS ,colours=['red','green','blue']      #list
# for i in colours:
#     print(i)

#PRINT EACH NUMBER,s={10,20,30}     #set
# for i in s:
#     print(i)

#PRINT EACH KEY,d={'a':10,'b':20,'c':30}        #dictionary
# for i in d:
#     print(i)

#PRINT EACH NUMBERS,d={'a':10,'b':20,'c':30}        #dictionary
#for i in d.values():
#     print(i)

#PRINT EACH NUMBER,t=(12,78,34,50)      #tuple
# for i in t:
#     print(i)

#PRINT EACH NUMBER,l=[56,89,34,10]      #list
# for i in l:
#     print(i)

#l=[12,34,56,45,89,16,69,33]
#PRINT EACH NUMBER IN A LIST
# for i in l:
#     print(i)

#PRINT EVEN VALUES
# for i in l:
#     if(i%2==0):
#         print(i)

#PRINT THOSE NUMBERS THAT ARE DIVISIBLE BY '5'
# for i in l:
#     if(i%5==0):
#         print(i)

#PRINT THOSE NUMBERS THAT CONTAINS '3'
# for i in l:
#     if('3' in str(i)):
#         print(i)

#SUM OF LIST
# sum=0
# for i in l:
#     sum=sum+i
# print("Sum =", sum)

#COUNT OF NUMBERS
# count = 0
# for i in l:
#     count=count+1
# print("Count =", count)

#COUNT OF EVEN NUMBERS IN A LIST
# count=0
# for i in l:
#     if i%2==0:
#         count=count + 1
# print("Count of even numbers =", count)

#PRODUCT OF LIST
# product = 1
# for i in l:
#     product=product*i
# print("Product =", product)

#PRINT SQUARES OF EACH NUMBER
# for i in l:
#     print(i**2)

#1.GIVEN A LIST
#l=[12,4.5,6.8,30,"arun","hello"]
#PRINT FLOATING POINT NUMBERS
# for i in l:
#     if(type(i)==float):
#         print(i)

#PRINT STRING VALUES
# for i in l:
#     if(type(i)==str):
#         print(i)

#PRINT NUMBERS
# for i in l:
#     if(type(i)==int or type(i)==float):
#         print(i)

#2.GIVEN A DICTIONARY
#d={'a':23,'b':25,'c':28,'d':30,'e':22}
#PRINT ONLY EVEN VALUES
# for i in d.values():
#     if(i%2==0):
#         print(i)

# 3.GIVEN A LIST
#colours=['red','green','blue','orange','black']
#PRINT STARTING LETTER OF EACH COLOUR
# for i in colours:
#     print(i[0])

#PRINT LAST LETTER OF EACH COLOUR
# for i in colours:
#     print(i[-1])

#PRINT REVERSE OF EACH COLOUR
# for i in colours:
#     print(i[::-1])

#PRINT ALL COLOURS CONTAINING LETTER 'b'
# for i in colours:
#     if('b' in i):
#         print(i)

#RANGE FUNCTION
# for i in range(1,6):
#     print(i)

#100-200
# for i in range(100,201):
#     print(i,end=" ")

#1,2,3,4,5
# for i in range(1,6):
#     print(i)

#1,3,5,7,9,11
# for i in range(1,12,2):
#     print(i)

#2,4,6,8,10
# for i in range(2,11,2):
#     print(i)

#100,200,300,400,500
# for i in range(100,501,100):
#     print(i)

#5,4,3,2,1
# for i in range(5,0,-1):
#     print(i)

# #3,6,9,12,15,18,21
# for i in range(3,22,3):
#     print(i)

#1,4,9,16,25,36
# for i in range(1,7):
#     print(i**2)

#print all 3 digit numbers(100-999)
# for i in range(100, 1000):
#     print(i)

#print all numbers divisible by 3 in the range 100-200
# for i in range(100,201):
#     if(i%3==0):
#         print(i)

#1,8,27,64,125
# for i in range(1,6):
#     print(i**3)

