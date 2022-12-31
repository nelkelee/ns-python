# range 보다 enumerate 를 사용해라
import itertools

f_list = ['A','B','C','D']
for f in range(len(f_list)):
    print(f_list[f])

for f,v in enumerate(f_list):
    print(f,v)

# 여러 이터레이터 루프에는 zip을 사용
a_list = ['A', 'B', 'C']
b_list = ['C', 'D', 'E', 'F']

for a,b in zip(a_list, b_list):
    print(a,b)
    
# 끝까지 출력시
for a,b in itertools.zip_longest(a_list, b_list):
    print(a,b)