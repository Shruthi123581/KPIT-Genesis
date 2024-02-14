def invert_dic(d):
    inverse = dict()
    for key in d:
        val = d[key]
        
        inverse.setdefault(val,key)
    return inverse

d = {'a':1,'b':2,'c':3,'d':4}
#d.setdefault('a',1)
print(invert_dic(d))