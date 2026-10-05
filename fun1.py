#Addition of two number
#function definition
# def addition():
#     "Addition of two numbers"
#     num1 = int(input("enter a number:"))
#     num2 = int(input("enter second number:"))
#     sum = num1 + num2
#     print(sum)
#     return
#
# addition()      #function call

#define a function to display a message "Hello Your Name"
# def one():
#     "print hello your name"
#     name=input("enter your name:")
#     print("Hello"+" "+name)
      #return
# one()

#define a function to print the factorial of a number
# def factorial_num():
#     fact=1
#     n=int(input("enter a number:"))
#     for i in range(1,n+1):
#         fact=fact*i
#     print(fact)
#
# factorial_num()

# #define a function to find the number of occurence of a particular character in a string
# def count_ch():
#     s=input("enter a string:")
#     ch=input("enter character:")
#     count=0
#     for i in s:
#         if(i==ch):
#             count=count+1
#     print("count of characters =", count)
#
# count_ch()

# #define a function to print the sum of elements in a list l=[89,45,67,12]
# def sum_list(l):
#     sum=0
#     for i in l:
#         sum=sum+i
#     print(sum)
#
# l = [89, 45, 67, 12]
# sum_list(l)

#define a function to check whether a number is prime or not
# def check_prime():
#     num=int(input("enter a number:"))
#     for i in range(2,num):
#         if(num%i==0):
#             print("not prime")
#             break
#     else:
#         print("prime")
#
# check_prime()

#function arguments and parameters
# def check_prime(num):
#     for i in range(2,num):
#         if(num%i==0):
#             print("not prime")
#             break
#     else:
#         print("prime")
# n=int(input("enter a number:"))
# check_prime(n)

#define a function that takes 3 arguments(amount,rate,year) and find the simple interest value
# def simple_interest(p,n,r):
#     s=p*n*r/100
#     print(s)
#     return
# p=int(input("enter principle amount:"))
# n=int(input("enter year:"))
# r=int(input("enter rate:"))
# simple_interest(p,n,r)

#define a function that takes 3 numbers and returns the product of 3 numbers
# def add(a,b,c):
#     prod=a*b*c
#     return prod
#
# result=add(7,8,9)
# print(result)


#define a function that takes a string and a character and returns the number of occurence of character in a string
# def count_ch(s,c):
#     count=0
#     for i in s:
#         if(i==c):
#             count=count+1
#     return count
#
# result=count_ch("hello",'l')
# print(result)

#define a function that takes list as arguments and returns a new list containing unique elements from list  given list
#l=[12,34,78,12,67,34,90,23]
#new=[12,34,78,67,90,23]
# Function to return unique elements from a list
# l=[12,34,78,12,67,34,90,23]
# def unique_list(l):
#     new = []
#     for i in l:
#         if i not in new:
#             new.append(i)
#     return new
#
# result=unique_list(l)
# print(result)

#define a function that takes 2 list as arguments and print common elements
# l1=[12,34,56,78,90]
# l2=[90,34,11,57,45]
# def common(l1,l2):
#     for i in l1:
#         if i in l2:
#             print(i)
#     return
# common(l1,l2)


# def func(n,a):
#     print("name",n)
#     print("age",23)
# func(n="arun",a=23)
# func(a=23,n="arun")

# def fun(n,a=23):
#     print(n)
#     print(a)
# fun('arun',25)