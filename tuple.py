#OP1
tuple1 = (10, 20, 30, 40, 50)
print(tuple1[::-1])

#OP2
tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
print(tuple1[1][1])

#OP3
tuple1= (50, )
print(tuple1)

#OP4
tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
print(f'a: {a} b: {b} c: {c} d: {d}')

#OP5
tuple1 = (11, 22)
tuple2 = (99, 88)
tuple1, tuple2 = tuple2, tuple1
print(tuple1)
print(tuple2)

#OP6
tuple1 = (11, 22, 33, 44, 55, 66)
res = tuple((tuple1[3], tuple1[4])) #slow/old way
tuple2 = tuple1[3:-1] #slicing
print(res)
print(tuple2)

#OP7
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)

#OP8
tuple1 = (('a', 23), ('b', 37), ('c', 11), ('d', 29))
tuple1 = tuple(sorted(list(tuple1), key=lambda x: x[1]))
print(tuple1)

#OP9
tuple1 = (50, 10, 60, 70, 50)
print(tuple1.count(50))

#OP10
tuple1 = (45, 45, 45, 45)
print(True if tuple1.count(tuple1[0]) == len(tuple1) else False) # slow way
print(all(i == tuple1[0] for i in tuple1)) #For loop
