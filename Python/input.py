#OP1
# num1 = int(input("Enter the first number:"))
# num2 = int(input("Enter the second number:"))
# print(f"Product of {num1} and {num2} is: {num1+num2}")

#OP2
print('Name','Is','James', sep="**")

#OP3
print("%o" % 8)

#OP4
print("%.2f" % 458.541315)

#OP5
# numbers = []
# for num in range(5):
#     num = float(input(f"Enter the {num}st/th number:"))
#     numbers.append(num)
# print(numbers)

print("\n")

#OP6
# with open("text.txt", "r") as fp:
#     lines = fp.readlines()
# with open("new_file.txt", "w") as fp:
#     count = 0
#     for line in lines:
#         if count == 4:
#             count += 1
#             continue
#         else:
#             fp.write(line)
#         count += 1

#OP7
# str1, str2, str3 = input("Enter three strings:").split()
# print(f"Str1: {str1} Str2: {str2} Str43 {str3}")
        
#OP8
totalMoney = 1000
quantity = 3
price = 450
print(f"I have {totalMoney} dollars so I can buy {quantity} football for {price:.2f} dollars. \n")

#OP9
import os
size = os.stat("text.txt").st_size
print('\nfile is empty\n') if size == 0 else print('file is not empty\n')

#OP10
with open('text.txt', "r") as fp:
    lines = fp.readlines()
    print(lines[2])
    fp.close()