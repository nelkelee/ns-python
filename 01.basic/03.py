import time

a = range(1,10,2)
for i in a:
    print(a)

for i in range(0,10):
    for j in range(0,i):
        a = a + '*'
    print(a)
    a=''

number = 0
t = time.time() + 5
while time.time() < t:
    number += 1

print('{}'.format(number)) 
print(t)

