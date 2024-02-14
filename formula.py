import math

def mysqrt(a):
    x = 1
    while True:
        print(x)
        y = (x+a/x)/2
        if y == x:
            break
        x = y

def test_square():
    print('a  mysqrt()    math.sqrt(a)    diff')
    
for i in range(1,10):
    a = float(input())

b = math.sqrt(float(a))
c = mysqrt(float(a)) - b
print(mysqrt(a), b, c)