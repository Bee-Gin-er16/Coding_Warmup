#OP1
for num in range(10):
    print(num+1, end=", ")
print("\n")

#Op2
for row in range(6):
    for col in range(row):
        print(col+1, end=" ")
    print("")
print("\n")

#Op3
# num = int(input("Enter a number:"))
for ctd in range(10):
    num += ctd
print(f"Sum is {num}")
print("\n")

#Op4
# mult = int(input("Enter a number for multiplication table:"))
for ctr in range(10):
    print((ctr+1)*(2), end=", ")
print("\n")

#Op5
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    elif num % 5 == 0 and num <= 150:
        print(num, end=", ")
print("\n")

#Op6
num = 75896
ctr = 0
while num != 0:
    num = num // 10
    ctr += 1
print(f"{ctr}\n")

#Op7
for row in reversed(range(5)):
    for col in reversed(range(row+1)):
        print(col+1, end=" ")
    print("")
print("")

#Op8
list1 = [10, 20, 30, 40, 50]
for items in reversed(list1):
    print(items, end=", ")
print("\n")

#Op9
neg_int = -10
while neg_int != 0:
    print(neg_int, end=", ")
    neg_int += 1
print("\n")

#Op10
for i in range(5):
    print(i, end=", ")
else:
    print(" Done!")

#Op11


#Op12


#Op13


#Op14


#Op15


#Op16

#Op17

#Op18

    