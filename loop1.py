#PRINT 1 TO 5
# i=1
# while(i<=5):#1<=5;2<=5;3<=5;4<=5;5<=5;6<=5(exits from the loop)
#     print(i)#1,2,3,4,5
#     i=i+1#2,3,4,5,6
#
# i=100
# while(i<=200)
#     print(i)
#     i=i+1


#1,2,3,.....100
# i=1
# while(i<=100):
#     print(i)
#     i=i+1


#1,3,5,7,9,11,13,15
# i=1
# while(i<=15):
#     print(i)
#     i=i+2


#2,4,6,8,10,12
# i=2
# while(i<=12):
#     print(i)
#     i=i+2


#1,4,7,10,13,16
# i=1
# while(i<=16):
#     print(i)
#     i=i+3


#10,20,30,40,50,60,70,80
# i=10
# while(i<=80):
#     print(i)
#     i=i+10


#3,6,9,12,15,18,21
# i=3
# while(i<=21):
#     print(i)
#     i=i+3


#5,4,3,2,1
# i=5
# while(i>=1):
#     print(i)
#     i=i-1


#8,6,4,2,0
# i=8
# while(i>=0):
#     print(i)
#     i=i-2


#100,101,102,...200
# i=100
# while(i<=200):
#     print(i)
#     i=i+1


#PRINT ALL 4 DIGIT NUMBERS(1000-9999)
# i=1000
# while(i<=9999):
#     print(i)
#     i=i+1

#PRINT THOSE 3 DIGIT NUMBERS THAT ARE DIVISIBLE BY 3
# i=100
# while(i<=999):
#     if(i%3==0):
#         print(i)
#     i=i+1

# PRINT THOSE 4 DIGIT NUMBERS THAT CONTAINS DIGIT '3'('in' OPERATOR SEQUENCE)
# i=1000
# while (i<=9999):
#     if('3' in str(i)):
#         print(i)
#     i=i+1

#PRINT THE NUMBERS THAT ARE DIVISIBLE BY 3 AND 5 IN THE RANGE (1,100)
# i=1
# while(i<=100):
#     if(i%3==0 and i%5==0):
#         print(i)
#     i=i+1

#1,4,9,16,25,36,49,64,81,100
# i=1
# while(i<=10):
#     print(i**2)
#     i=i+1

#PRINT THOSE 3 DIGIT NUMBERS  THAT CONTAINS 'DIGIT 3'
#COUNT OF THOSE 3 DIGIT NUMBERS THAT CONTAINS DIGIT '3'
# count=0
# i=100
# while(i<=999):
#     if('3' in str(i)):
#         print(i)
#         count=count+1
#     i=i+1
# print("count:",count)

#COUNT OF THOSE NUMBERS THAT ARE DIVISIBLE BY 7 AND 5 IN THE RANGE(200,300)
# count=0
# i=200
# while(i<=300):
#     if(i%7==0 and i%5==0):
#         print(i)
#         count=count+1
#     i=i+1
# print("count",count)

#COUNT OF ODD NUMBERS THAT ARE DIVISIBLE BY 5 IN THE RANGE(1,100)
# count=0
# i=1
# while(i<=100):
#     if(i%2!=0 and i%5==0):
#         print(i)
#         count=count+1
#     i=i+1
# print("count",count)

#COUNT OF ALL PALINDROME NUMBERS IN THE RANGE(1,1000)
# count=0
# i=1
# while(i<=1000):
#     s=str(i)
#     if(s==s[::-1]):
#         print(i)
#         count=count+1
#     i=i+1
# print("count",count)

#COUNT OF THOSE NUMBERS THAT ARE DIVISIBLE BY 3 IN RANGE(1,50)
# count=0
# i=1
# while(i<=50):
#     if(i%3==0):
#         print(i)
#         count=count+1
#     i=i+1
# print("count:",count)

#SUM OF SERIES 1,2,3,4,5
# sum=0
# i=1
# while(i<=5):      #1<=5;2<=5;3<=5;4<=5;5<=5;6<=5(loop exit)
#     sum=sum+i     #0+1+2+3+4+5
#     i=i+1         #2,3,4,5,6
# print("sum:",sum)

#SUM OF THOSE NUMBERS THAT ARE DIVISIBLE BY 3 IN THE RANGE(1,50)
# sum=0
# i=1
# while(i<=50):
#     if(i%3==0):
#         sum=sum+i
#     i=i+1
# print("Sum:", sum)

#SUM OF ALL 3 DIGIT NUMBERS
# sum=0
# i=100
# while(i<=999):
#     sum=sum+i
#     i=i+1
# print("Sum:", sum)

#SUM OF FIRST 10 EVEN NUMBERS
# sum=0
# i=2
# while(i<=20):
#     sum=sum+i
#     i=i+2
# print("Sum:", sum)

#PRODUCT 1,2,3,4,5
# product=1
# i=1
# while(i<=5):
#     product=product*i
#     i=i+1
# print("product:",product)

#PRODUCT OF FIRST 10 ODD NUMBERS
# product=1
# i=1
# while(i<=19):
#     product=product*i
#     i=i+2
# print("Product:", product)

#PRODUCT OF NUMBERS THAT CONTAINS DIGIT '3' IN THE RANGE(1,50)
# product=1
# i=1
# while(i<=50):
#     if '3' in str(i):
#         product=product*i
#     i=i+1
# print("Product:", product)

#FACTORIAL OF A NUMBER
# num=int(input("Enter a number:"))
# fact=1
# i=1
# while(i<=num):
#     fact=fact*i
#     i=i+1
# print("Factorial:",fact)

#MULTIPLICATION TABLE OF A NUMBER(UPTO 10)
# num=int(input("Enter a number:"))
# i=1
# while(i<=10):
#     print(num,'*',i,'=',num*i)
#     i=i+1
