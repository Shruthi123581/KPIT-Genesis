# list methods

list1 = [3,4,'str',4]
list1.append(6)
list2 = list1.copy()
list2.clear()

print(list1.count(3))
print(list1)
print(list2)
list2.append([2,3])
list1.extend(list2)
print(list1)
print(list2)

print(list1.index(3))
list1.insert(1,'shruthi')
print(list1)

list1.pop(6)
print(list1)

list1.reverse()
print(list1)

# list1.sort()

list1.pop(2)
list1.pop(3)
print(list1)
list1.sort()
print(list1)

# Tuple methods
tuple1 = (1,'str')
print(tuple1)
# tuple1.count(1)
print(tuple1.count(1))
print(tuple1.index('str'))

# Dict methods
dict1 = {'shruthi':1, 'abc': 3,'def':2}
print(dict1)
# print(dict1.clear())
dict2 = dict1.copy()
print(dict2)

print(dict1.fromkeys(dict1))
print(dict1.get('abc'))
print(dict1.items())
print(dict1.keys())
dict1.pop('def')
dict1.popitem()
print(dict1)
dict1.setdefault('xyz',3)
print(dict1)
dict1.update({'xyz':5})
print(dict1)
print(dict1.values())