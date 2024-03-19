#OP1
name = "James"
print(f"{name[0]}{name[int(len(name)/2)]}{name[-1]}")

#OP1.2
# str1 = "JhonDipPeta"
str1 = "JaSonAy"
midpoint = round(len(str1)/2)
print(f"{str1[midpoint-2]}{str1[midpoint-1]}{str1[midpoint]}")

#OP2
s1 = "Ault"
s2 = "Kelly"
mp = round(len(s1)/2)
x = s1[:mp]
# print(s1[:mp])
# print(s1[mp:])
x = x + s2
# print(x)
x = x + s1[mp:]
print(x)

#OP3
s1 = "America"
s2 = "Japan"
start = s1[0] + s2[0]
end = s1[-1] + s2[-1]
mid = s1[int(len(s1)/2)] + s2[int(len(s2)/2)]
fin = start + mid + end
print(fin)

#OP4
str1 = "PyNaTive"
print('Original String:', str1)
lower = []
upper = []
for char in str1:
    if char.islower():
        # add lowercase characters to lower list
        lower.append(char)
    else:
        # add uppercase characters to lower list
        upper.append(char)

# Join both list
sorted_str = ''.join(lower + upper)
print('Result:', sorted_str)

#OP5
Chars = 0
Digits = 0
Symbols = 0
str1 = "P@#yn26at^&i5ve"
for char in str1:
    if char.isalpha():
        Chars += 1
    elif char.isdigit():
        Digits += 1
    else:
        Symbols += 1
print("Chars =", Chars, "Digits =", Digits, "Symbol =", Symbols)

#OP6
s1 = "Abc"
s2 = "Xyz"
s1_length = len(s1)
s2_length = len(s2)
length = s1_length if s1_length > s2_length else s2_length
result = ""

# reverse s2
s2 = s2[::-1]
# iterate string 
# s1 ascending and s2 descending
for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)

#OP7
s1 = "Yn"
s2 = "PYnative"
print("Found") if s1 in s2 else print("Not Found")

#Op8
str1 = "Welcome to USA. usa awesome, isn't it?"
str1 = str1.lower()
res = str1.count("usa")
print(f"The USA count is: {res}")

#Op9
str1 = "PYnative29@#8496"
sum = 0
div = 0
for ind in str1:
    if ind.isdigit():
        sum += int(ind)
        div += 1
print(f"Sum: {sum} average: {sum/div}")

#Op10
str1 = "Apple"
char_dict = dict()
for char in str1:
    count = str1.count(char)
    char_dict[char] = count
print('Result:', char_dict)

#Op11
str1 = "PYnative"
print(str1[::-1])

#Op12
str1 = "Emma is a data scientist who knows Python. Emma works at google."
print(f"Last occurence of Emma at index {str1.rfind("Emma")}")

#Op13
str1 = "Emma-is-a-data-scientist"
res = ''.join(str1.split("-"))
print(res)

#Op14
str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
res_list = list(filter(None, str_list))
print(res_list)

#Op15
import re
str1 = "/*Jon is @developer & musician"
print("Original string is:", str1)

# replace special symbols with ''
res = re.sub(r'[^\w\s]', '', str1)
print("New string is:", res)

#OP16
str1 = 'I am 25 years and 10 months old'
int_list = []
for char in str1:
    if char.isdigit(): int_list.append(char)
print(f"integers in list: {''.join(int_list)}")

#Op17
str1 = "Emma25 is Data scientist50 and AI Expert"
res = []
temp = str1.split()
for item in temp:
    if any(char.isalpha() for char in item) and any(char.isdigit() for char in item):
        res.append(item)
print("Displaying words with alphabets and numbers")
for i in res:
    print(i)

#Op18
import string
str1 = '/*Jon is @developer & musician!!'
for char in string.punctuation:
    str1 = str1.replace(char, "#")
print("The strings after replacement : ", str1)