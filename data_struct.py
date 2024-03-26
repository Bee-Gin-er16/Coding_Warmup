#Op1
list1 = [3, 6, 9, 12, 15, 18, 21]
list2 = [4, 8, 12, 16, 20, 24, 28]

res = list()

odd_elements = list1[1::2]
even_elements = list2[0::2]

print("Printing Final list")
res.extend(odd_elements)
res.extend(even_elements)
print(res)

print("\n")
#Op2
sample_list = [34, 54, 67, 89, 11, 43, 94]

print("Original list ", sample_list)
element = sample_list.pop(4)
print("List After removing element at index 4 ", sample_list)
sample_list.insert(2, element)
print("List after Adding element at index 2 ", sample_list)
sample_list.append(element)
print("List after Adding element at last ", sample_list)

print("\n")
#Op3
sample_list = [11, 45, 8, 23, 14, 12, 78, 45, 89]
print("Original list ", sample_list)

length = len(sample_list)
chunk_size = int(length / 3)
start = 0
end = chunk_size

# run loop 3 times
for i in range(3):
    # get indexes
    indexes = slice(start, end)
    # get chunk
    list_chunk = sample_list[indexes]
    print("Chunk ", i, list_chunk)
    # reverse chunk
    print("After reversing it ", list(reversed(list_chunk)))

    start = end
    end += chunk_size

print("\n")
#Op4
sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]
print("Original list ", sample_list)

count_dict = dict()
for item in sample_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print("Printing count of each item  ", count_dict)

print("\n")
#Op5
first_list = [2, 3, 4, 5, 6, 7, 8]
print("First List ", first_list)

second_list = [4, 9, 16, 25, 36, 49, 64]
print("Second List ", second_list)

result = zip(first_list, second_list)
result_set = set(result)
print(result_set)
    