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