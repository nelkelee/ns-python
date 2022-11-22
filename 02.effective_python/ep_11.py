list = [1,2,3,4,5,6,7,8,9,10]
print(list[2:4]) #[3,4]
print(list[:]) #[1,2,3,4,5,6,7,8,9,10]
print(list[-3:2]) #[]
print(list[-3:]) #[8, 9, 10]
print(list[-3:-5]) #[]
print(list[:-3]) #[1, 2, 3, 4, 5, 6, 7]

abc = list
print(abc) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list[:] = [11,12,13]
print(list) #[11, 12, 13]

