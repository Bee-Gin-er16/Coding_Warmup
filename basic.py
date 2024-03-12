#FUNCTION DEFINITION

#FP1
def multi_add(n1, n2):
    return n1*n2 if n1*n2 <= 1000 else n1+n2

#FP2
def sum_range(limit):
    current = 0
    previous = 0
    for number in range(limit):
        current = number
        total = str(current+previous)
        print("Current Number:"+str(current)+ " Previous Number:" +str(previous)+ "Sum: "+total)
        previous = current

#FP3
def even_chars(string):
    char_list = []
    count = 0
    while count < len(string):
        if count % 2 == 0:
            char_list.append(string[count])
        count+=1
    return char_list

#FP5
def samelast(list):
    return str(True if list[0] == list[-1] else False)

#FP6
def isdivby(list, divisor):
    print("Divisible by "+str(divisor))
    for num in list:
        if num % divisor == 0:
            print(str(num))
    print("")

#FP9 Palindrome for integers only
def checkpal(num):
    rev_num = []
    ctr = len(str(num))-1
    while ctr >= 0:
        rev_num.append(str(num)[ctr])
        ctr-=1
    rev_num = "".join(rev_num)
    if int(rev_num) == num:
        return True
    else:
        return False

#OP10 Assuming that the lists are the same length
def whole_list(l1, l2):
    new_list = []
    for num in l1:
        if num % 2 != 0: new_list.append(num)
    for num in l2:
        if num % 2 == 0: new_list.append(num)
    return new_list

#OP11
def rev_order(num):
    iter = len(num)-1
    rev_string = []
    while iter >= 0:
        rev_string.append(f"{num[iter]} ")
        iter-=1
    return "".join(rev_string)

#OP15
def sqrd(base, exp):
    result = base
    ctr = exp
    if(exp == 0):
        return 1
    elif(exp == 1):
        return base
    else:
        while ctr > 1:
            result *= base
            ctr-=1
    return result

# print("debug for console")

#OUTPUTS
#OP1
print("\nResult is: " +str(multi_add(20, 30))+ "\n")

#OP2
print("Printing current and previous number sum in a range("+str(10)+")")
sum_range(10)
    
#OP3
word = "pynative"
print(f"\n{even_chars(word)} \n")

#F4 OP4
x = len(word)
print(f"\n{word[2:x]} \n")

#OP5
num_list = [10, 20, 30, 40, 10]
print("Given list: "+str(num_list))
print("Result is: "+samelast(num_list))

#OP6
div_list = [10, 20, 33, 46, 55]
isdivby(div_list, 5)
            
#OP7
str_x = "Emma is good developer. Emma is a writer"
print(f"Emma appears in the string: {str_x.count("Emma")}")

#OP8 
for row in range(5):
    for col in range(row):
        print(row, end=" ")
    print("")
print("")

#OP9
pal_num = 121
print(f"Result is :{checkpal(pal_num)} \n")

#OP10
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print(whole_list(list1, list2))

#OP11
rev_int = 7536
print(f"\n{rev_order(str(rev_int))} \n")

#OP12
income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    x = income - 10000
    tax_payable = x * 10 / 100
else:
    tax_payable = 0
    tax_payable = 10000 * 10 / 100
    tax_payable += (income - 20000) * 20 / 100
print(f"Total tax to pay is {tax_payable} \n")

#OP13
for row in range(10):
    for col in range(10):
        print((row+1)*(col+1), end=" ")
    print(" ")
print("\n")

#OP14
tri_start = 5
while tri_start > 0:
    for row in range(tri_start):
        print("*", end="")
    print("")
    tri_start-=1

#OP15
base = 2
exponent = 5
print(f"\nResult of exponent {sqrd(base, exponent)}\n")