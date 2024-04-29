#FN1
def greet(name, age):
    print(f"Hello, my name is {name} and i am {age} year's old")

#FN2
def func1(*args):
    for i in args:
        print(i)

#FN3
def calc(num1, num2):
    results = []
    results.append(num1+num2)
    results.append(num1-num2)
    return results

#FN4
def showEmployee(name, salary = 9000):
    print(f"Name: {name} salary: {salary}")

#FN5
def outer_fun(a, b):
    square = a ** 2

    # inner function
    def addition(a, b):
        return a + b

    # call inner function from outer function
    add = addition(a, b)
    return add + 5

#FN6
def sum_rec(ctr, res = 0):
    return res if ctr == 0 else sum_rec(ctr-1, res + ctr)

#FN7
def display_student(name, age):
    print(name, age)

#FN8

#Calls
    
#C1
greet("Jan", 18)

#C2
func1(20, 40, 60)
func1(80, 100)

#C3
print(calc(40, 10))

#C4
showEmployee("Ben", 12000)
showEmployee("Jessa")

#C5
print(f"Outer fun result : {outer_fun(5,10)} \n")

#C6
print(f"Recursion result : {sum_rec(10)} \n")

#C7
display_student("Emma", 26)
# assign new name
showStudent = display_student
# call using new name
showStudent("Emma", 26)

#C8
print(f"Even list from 4 to 30: {list(range(4, 30, 2))} \n")

#C9
x = [4, 6, 8, 24, 12, 2]
print(max(x))