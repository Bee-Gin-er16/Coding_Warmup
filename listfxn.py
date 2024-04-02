#OP1
list1 = [100, 200, 300, 400, 500]
list1.reverse()
print(list1)

#OP2
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
res = [i + j for i,j in zip(list1, list2)]
print(res)

#OP3
numbers = [1, 2, 3, 4, 5, 6, 7]
res = [x * x for x in numbers]
print(res)

#OP4
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res = [i + j for i in list1 for j in list2]
print(res)

#OP5
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
res = [f"{x} {y}" for x,y in zip(list1, list2[::-1])]
print(res)

#OP6
#OP7
#OP8
#OP9
#OP10