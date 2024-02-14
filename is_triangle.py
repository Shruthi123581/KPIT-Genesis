def is_triangle(a,b,c):
    if c>(a+b):
        print("No")
    elif((a+b)==c):
        print("Yes")

def input1():
    a = int(input())
    b = int(input())
    c = int(input())
    return is_triangle(a,b,c)

is_triangle(1,1,3)
input1()
