def star():
    for row in range(0,5):
        for col in range(0,5):
            print("*",end=" ")
        print()
star()
# Output
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * * 

def star1():
    for row in range(0,5):
        for col in range(0,row+1):
            print("*",end=" ")
        print()
star1()
# Output
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

def star2():
    for row in range(5,0,-1):
        for col in range(0,row):
            print("*",end=" ")
        print()
star2()
# Output
# * * * * *
# * * * *
# * * *
# * *
# * 


def numbers():
    for row in range(0,5):
        for col in range(0,row+1):
            print(col+1,end=" ")
        print()
numbers()
# Output
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5 

def numbers1():
    for row in range(0,5):
        for col in range(0,row+1):
            print(64+col+1,end=" ")
        print()
numbers1()
# Output
# 65
# 65 66
# 65 66 67
# 65 66 67 68
# 65 66 67 68 69 


def alphabet():
    for row in range(1,6):
        for col in range(1,row+1):
            print(chr(64+col),end=" ")
        print()
alphabet()
# Output
# A 
# A B 
# A B C 
# A B C D 
# A B C D E 


def alphabet1():
    for row in range(1,6):
        for col in range(1,row+1):
            print(chr(96+col),end=" ")
        print()
alphabet1()
# Output
# a 
# a b 
# a b c 
# a b c d 
# a b c d e 

def Pyramid():
    for row in range(1, 6):
        print(" " * (5-row), end="")
        print("* " * row)
Pyramid()
# Output
#     * 
#    * *
#   * * *
#  * * * *
# * * * * * 


def diamond():
    for row in range(1, 6):
        print(" " * (5-row), end="")
        print("* " * row)

    for row in range(4, 0, -1):
        print(" " * (5-row), end="")
        print("* " * row)
diamond()
# Output
#     *
#    * *
#   * * *
#  * * * *
# * * * * *
#  * * * *
#   * * *
#    * *
#     * 


def Hollow_square():
    for row in range(5):
        for col in range(5):
            if row == 0 or row == 4 or col == 0 or col == 4:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
Hollow_square()
# Output
# * * * * *
# *       *
# *       *
# *       *
# * * * * * 


# Tables
def tables():
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    for i in range(start, end + 1):
        print("Table Of", i)

        for j in range(1, 11):
            print(i, "*", j, "=", i * j)

        print()

tables()

# Output
# Enter the starting number: 2
# Enter the ending number: 5
# Table Of 2
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# 2 * 6 = 12
# 2 * 7 = 14
# 2 * 8 = 16
# 2 * 9 = 18
# 2 * 10 = 20

# Table Of 3
# 3 * 1 = 3
# 3 * 2 = 6
# 3 * 3 = 9
# 3 * 4 = 12
# 3 * 5 = 15
# 3 * 6 = 18
# 3 * 7 = 21
# 3 * 8 = 24
# 3 * 9 = 27
# 3 * 10 = 30

# Table Of 4
# 4 * 1 = 4
# 4 * 2 = 8
# 4 * 3 = 12
# 4 * 4 = 16
# 4 * 5 = 20
# 4 * 6 = 24
# 4 * 7 = 28
# 4 * 8 = 32
# 4 * 9 = 36
# 4 * 10 = 40

# Table Of 5
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50