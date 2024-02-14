'''
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print(j+1, end=" ")
    print("\n")



rows = int(input("Enter number of rows: "))

ascii_value = 65

for i in range(rows):
    for j in range(i+1):
        alphabet = chr(ascii_value)
        print(alphabet, end=" ")
        print()
    
    ascii_value += 1
    print("\n")



rows = int(input("Enter number of rows: "))
for i in range(rows,0,-1):
    for j in range(i):
        print("*",end=" ")

    print("\n")



def triangle(n):
    k = n - 1
    for i in range(0, n):
        for j in range(0, k):
            print(end=" ")

        k = k - 1

        for j in range(0, i+1):
 
            print("* ", end="")
        print("\r")
 
# Driver Code
n = 5
triangle(n)
'''

def rev_triangle(n):
    k = n - 1
    for i in range(n,0,-1):
        for j in range(0, i+1):
            print("*",end="")

        for j in range(0,k+1):
            print(end = "")

        k = k-1

        print("\n")

n = int(input())
rev_triangle(n)

