array1 = [1, 2, 3, 'kanon', 'keke', True]
print(array1)

array2 = [4, 5, 6, 'sumire', 'ren', 'chisato']
print(array2)

print(array1+array2)

for i in array1+array2:
    print(i)
    
array_number = [item for item in array1+array2 if type(item) is int]

for i in array_number:
    print("{} * 9 = {}".format(i, i*9))
    
a = [[1, 2, 3],[4, 5, 6]]
for x in a:
    print(x)
    for y in x:
        print(y)
        
b = {"name":"nijigasaki", "member":100}
print(b['member'])
print(b['name'])