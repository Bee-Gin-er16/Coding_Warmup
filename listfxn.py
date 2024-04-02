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
list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
res = list(filter(None, list1))
print(res)

#OP7
list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)

#OP8
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]
list1[2][1][2].extend(sub_list)
print(list1)

#OP9
list1 = [5, 10, 15, 20, 25, 50, 20]
list1[list1.index(20)]= 200
print(list1)

#OP10
list1 = [5, 20, 15, 20, 25, 50, 20]
def remove_value(sample_list, val):
    return [i for i in sample_list if i != val]

res = remove_value(list1, 20)
print(res)

