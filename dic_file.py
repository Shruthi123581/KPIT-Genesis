fin = open('C:/Users/SHRUTHIB/Documents/Python/words.txt')
def dicti1(d,x):
    a = dict()
    for line in fin:
        count=0
        for letter in line.split():
            for val in d:
                keys = d[val]
            
                if(x==letter):
                    count=count+1
                    print(keys[letter],count)
    return x

x = ''
print(dicti1(fin,x))