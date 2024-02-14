import math
def check_fermat(a, b, c, n):
    
    if(n>2) and math.pow(a,n)+math.pow(b,n) == math.pow(c,n):
        
        print("Holy smokes, Fermat was wrong!")

    else:
        
        print('No, that doesnt work')

def input_no():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    return check_fermat(a,b,c,d)

check_fermat(5,12,13,2)
input_no()