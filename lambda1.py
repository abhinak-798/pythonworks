#square of a number
# sq=lambda x:x**2
# print(sq(4))

#cube of a number
# cube=lambda a:a**3
# print(cube(2))

#square root
# sr=lambda a:a**0.5
# print(sr(2))

#length of a string
# length=lambda x:len(x)
# print(length("hello"))

# name attribute of a dictionary
# d=lambda x:x['name']
# print(d({"name":"arun","age":23}))

# first character of a string
# first=lambda x:x[0]
# print(first("python"))

# last element of a list
# last=lambda x:x[-1]
# print(last([1,2,3,4]))

# sum of 2 numbers
# s=lambda x,y:x+y
# print(s(2,3))

# sum of 3 numbers
# sum=lambda a,b,c:a+b+c
# print(sum(1,2,3))


# product of 4 numbers
# p=lambda a,b,c,d:a*b*c*d
# print(p(1,2,3,4))

#MAP FUNCTION
#create a new list with squares of each element
# l=[1,2,3,4]
# print(list(map(lambda x:x**2,l)))
# print(set(map(lambda x:x**2,l)))
# print(tuple(map(lambda x:x**2,l)))

#create a new list with cubes
#l=[1,2,3,4]
# print(list(map(lambda x:x**3,l)))

#create a new list of square roots
# l=[25,36,81,100]
# print(list(map(lambda x:x**0.5,l)))

#create a new list of lengths
#colors=['red','green','blue','yellow','black']
# print(list(map(lambda x:len(x),colors)))

#create a new list of first characters
# print(list(map(lambda x:x[0],colors)))

#create a new list of last characters
# print(list(map(lambda x:x[-1],colors)))

#create a new list of reverse of each element
# print(list(map(lambda x:x[::-1],colors)))

#Given a list
#Add 10 to each element in the given sequence
#l=[23,78,12,56]
# print(list(map(lambda x:x+10,l)))

# given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]

# create a new list of emails
# print(list(map(lambda x:x['email'],l)))
# print(list(map(lambda x:x['name'],l)))
# print(list(map(lambda x:x['salary'],l)))


#FILTER FUNCTION
#print even numbers from list
#l=[1,2,3,4,5,6,7,8,9,10]
# print(list(filter(lambda x:x%2==0,l)))

#given a list
#numbers greater than 50
#l=[23,67,90,12,45,52]
# print(list(filter(lambda x:x>50,l)))

#given a list of fruits
#fruitname whose length is greater than 5
#f=['apple','orange','grapes','pineapple','grapes']
# print(list(filter(lambda x:len(x)>5,f)))

#given a list
#number divisible by 3 and 5
#l1=[34,78,96,23,12,15]
# print(list(filter(lambda x:x%3==0 and x%5==0,l1)))


#REDUCE FUNCTION
#sum of list
#l=[1,2,3,4]
# import functools
# print(functools.reduce(lambda a,b:a+b,l,0))

#product of list
# import functools
# print(functools.reduce(lambda a,b:a*b,l,1))