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
print(" ")

#Op11
start = 25
end = 50
print(f"Prime numbers between {start} and {end} are the ff:")
for nums in range(start, end+1):
    if nums > 1:
        for itr in range(2, nums):
            if(nums % itr) == 0:
                break
        else: 
            print(nums, end=", ")
print("\n")

#Op12
fib1 = 0
fib2 = 1
for iter in range(10):
    print(fib1, end=", ")
    output = fib1 + fib2
    fib1 = fib2
    fib2 = output
print("\n")

#Op13
result = 1
for fact in (range(1,5+1)):
    result *= fact
print(result)
print(" ")

#Op14
num = 76542
reverse_number = 0
print("Given Number ", num)
while num > 0:
    reminder = num % 10
    reverse_number = (reverse_number * 10) + reminder
    num = num // 10
print(f"Reverse Number: {reverse_number}\n")

#Op15
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for ind in range(len(my_list)):
    if ind % 2 != 0: print(my_list[ind], end=", ")
print("\n")

#Op16
for integ in range(6):
    print(f"Current number is :{integ+1} and the cube is :{(integ+1)**3}")
print(" ")

#Op17
giv_num = num = 2
limit = 5
res = 0
for ind in range(limit):
    res += num
    num = (num * 10) + giv_num
print(f"{res}\n") 

#Op18
rows = 5
for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")
for i in range(rows, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print("\r")
    