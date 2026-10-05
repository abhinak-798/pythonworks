#NESTED LOOP
# for i in range(1,4):
#     for j in range(1,6):
#         print(i)

# for i in range(1,4):
#     for j in range(1,6):
#         print(j)
#
# for i in range(1,4):
#     for j in range(1,6):
#         print(i,j)

# l=['kelly','emy','alan']
# for i in l:
#     for j in range(1,4):
#         print(i)

# no=[1,2,3]
# qns=['what','when','why']
# for i in no:
#     print(i)
#     for j in qns:
#         print(j)

# l=[[1,2,3,4],[5,6,7,8]]
# for i in l:
#     print(i)
#     for j in i:
#         print(j)

# l=[{'id':101,'name':'arun','age':23},
#    {'id':102,'name':'amal','age':24},
#    {'id':103,'name':'anu','age':22}]
# for i in l:
#     print(i)
#     for j in i.values():
#         print(j)

#PATTERN PRINT
# for i in range(1,5):        #define number of rows
#     for j in range(1,5):       #define number of columns
#         print(i,end=" ")
#     print()

# for i in range(1,11):        #define number of rows
#     for j in range(1,11):       #define number of columns
#         print(j,end=" ")
#     print()

# for i in range(1,5):        #define number of rows
#     for j in range(1,5):       #define number of columns
#         print('*',end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()

# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

#1..
# 1 0 0 0
# 0 1 0 0
# 0 0 1 0
# 0 0 0 1
# for i in range(1,5):
#     for j in range(1,5):
#         if(i==j):
#             print(1, end=" ")
#         else:
#             print(0, end=" ")
#     print()

#2..
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# k=1
# for i in range(1, 5):
#     for j in range(1,i+1):
#         print(k, end=" ")
#         k=k+1
#     print()

#3..
# 2
# 4 6
# 8 10 12
# k=2
# for i in range(1, 4):
#     for j in range(1,i+1):
#         print(k, end=" ")
#         k=k+2
#     print()

#4..
# 1
# 3 5
# 7 9 11
# k=1
# for i in range(1, 4):
#     for j in range(1,i+1):
#         print(k, end=" ")
#         k=k+2
#     print()

#5..
# * * * *
# * * *
# * *
# *
# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print("*", end=" ")
#     print()

#6..
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1
# for i in range(5,0,-1):
#     for j in range(1,i+1):
#         print(i, end=" ")
#     print()

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# for i in range(1,5):
#     for j in range(i,0,-1):
#         print(j, end=" ")
#     print()

# 1
# 1 0
# 1 0 1
# 1 0 1 0
# k=4
# for i in range(1,k+1):
#     for j in range(i):
#         if j%2==0:
#             print(1, end=" ")
#         else:
#             print(0, end=" ")
#     print()

# A
# B B
# C C C
# D D D D
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k), end=" ")
#     k=k+1
#     print()

# A
# B C
# D E F
# G H I J
# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k), end=" ")
#         k=k+1
#     print()

# A
# A B
# A B C
# A B C D
# for i in range(1,5):
#     k=ord('A')
#     for j in range(1,i+1):
#         print(chr(k), end=" ")
#         k=k+1
#     print()

#l=[12,34,56,78,13,87,5]
#PRINT ALL PRIME NUMBERS IN THE GIVEN LIST
# for i in l:
#     for j in range(2,i):
#         if(i%j==0):
#             break
#     else:
#         print(i)

#PRINT ALL PRIME NUMBERS IN THE RANGE(1,100)
# for i in range(2,101):
#     for j in range(2,i):
#         if(i%j==0):
#             break
#     else:
#         print(i)
# *
# * *
# * * *
# * * * *
# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

# 1
# 4 9
# 16 25 36
# 49 64 81 100
# k=1
# for i in range(1, 5):
#     for j in range(1,i+1):
#         print(k**2, end=" ")
#         k=k+1
#     print()

# 1
# 3 3 3
# 5 5 5 5 5
# k=1
# for i in range(1,6,2):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     k=k+2
#     print()

# 1
# 1 A 1
# 1 A 1 A 1
# for i in range(1,6,2):
#     for j in range(1,i+1):#execute one time
#         if(j%2==0):
#             print('A',end=" ")
#         else:
#             print("1",end=" ")
#     print()

#       *
#     * *
#   * * *
# * * * *
# k=3*2     #initially sets the k as the double the space actually needed
# for i in range(1,5):
#     for p in range(1,k+1):    #loop for adding extra space in each line
#         print("",end=" ")
#     k=k-2
#     for j in range(1,i+1):
#         print('*',end=" ")       #loop for printing '*' in each line
#     print()

#      *
#     *  *
#   *  *  *
# *  *  *  *
# k=3*2     #initially sets the k as the double the space actually needed
# for i in range(1,5):
#     for p in range(1,k+1):    #loop for adding extra space in each line
#         print("",end=" ")
#     k=k-2
#     for j in range(1,i+1):
#         print('*',end="  ")       #loop for printing '*' in each line
#     print()

#       5
#     5  5
#   5  5  5
# 5  5  5  5
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print("",end=" ")
#     k=k-2
#     for j in range(1,i+1):
#         print('5',end="  ")
#     print()

# *  *  *  *
#   *  *  *
#     *  *
#       *
# k=0
# for i in range(4,0,-1):
#     for p in range(1,k+1):
#         print("",end=" ")
#     k=k+2
#     for j in range(1,i+1):
#         print('*',end="  ")
#     print()

# *
# * *
# * * *
# * * * *
# * * *
# * *
# *
# for i in range(1,5):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()
# for k in range(3,0,-1):
#     for j in range(1,k+1):
#         print('*',end=" ")
#     print()

 #    *
 #   * *
 #  * * *
 # * * * *
 #  * * *
 #   * *
 #    *
# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print("",end=" ")
#     k=k-2
#     for j in range(1,i+1):
#         print('*',end="  ")
#     print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print("",end=" ")
#     k=k+2
#     for j in range(1,i+1):
#         print('*',end="  ")
#     print()

  #       * *
  #       * *
  #     * * * *
  #     * * * *
  #   * * * * * *
  #   * * * * * *
  # * * * * * * * *
  # * * * * * * * *
# k=3*2
# for i in range(2,9,2):
#     for j in range(1,3):
#         for p in range(1,k+1):
#             print("",end=" ")
#         for q in range(1,i+1):
#             print('*',end=" ")
#         print()
#     k=k-2

# * *
# * * * *
# * * * * * *
# * * * * * * * *
# for i in range(2,9,2):
#     for j in range(1,i+1):
#         print('*',end=" ")
#     print()

# 5 4 3 2 1
# 5 4 3 2
# 5 4 3
# 5 4
# 5
k=5
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(k,end=" ")
        k=k-1
    k=5
    print()
