def factorial1(n):
    if(n==0):
        return 1
    else:
        fact1 = factorial1(n-1)
        fact = fact1*n
        return fact
    
print(factorial1(int(input())))