#OP1
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(sample_list)
print(sample_set)

#OP2
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
res = set.intersection(set1, set2)
print(res)

#OP3
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
res = set.union(set1,set2)
print(res)

#OP4
set1 = {10, 20, 30}
set2 = {20, 40, 50}
set1.difference_update(set2)
print(set1)

#OP5
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)

#OP6
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
res = set.symmetric_difference(set1,set2)
print(res)

#OP7
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
if set1.isdisjoint(set2):
  print("Two sets have no items in common")
else:
  print("Two sets have items in common")
  print(set1.intersection(set2))

#OP8
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.symmetric_difference_update(set2)
print(set1)

#OP9
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1.intersection_update(set2)
print(res)

