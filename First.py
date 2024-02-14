'''r=5
v=(4/3)*3.142*(5**3)
print(v)

a=24.95*0.4
b = a*60
c=3+(59*0.75)
print(b+c)
'''
def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

print_n('shruthi',3)

