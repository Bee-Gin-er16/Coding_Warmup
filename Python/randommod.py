import random, secrets, string, time

#OP1
print("Generating 3 random integer number between 100 and 999 divisible by 5")
int_list = []
for num in range(3):
    int_list.append(random.randrange(100, 999, 5))
print(int_list)

#OP2
lottery_tickets_list = []
print("creating lottery tickets")
for i in range(100):
    lottery_tickets_list.append(random.randrange(1000000000, 9999999999))
winners = random.sample(lottery_tickets_list, 2)
print(f"winners are: {winners}")

#OP3
secretsGenerator = secrets.SystemRandom()
print("Generating 6 digit random OTP")
otp = secretsGenerator.randrange(100000, 999999)
print("Secure random OTP is ", otp)

#OP4
str = 'HeloWurd'
print(f'Random word from {str}: {random.choice(str)}')

#OP5
def randomString(stringLength):
    """Generate a random string of 5 charcters"""
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

print ("Random String is ", randomString(5) )

#OP6
def randomPassword():
    randomSource = string.ascii_letters + string.digits + string.punctuation
    password = random.sample(randomSource, 6)
    password += random.sample(string.ascii_uppercase, 2)
    password += random.choice(string.digits)
    password += random.choice(string.punctuation)

    passwordList = list(password)
    random.SystemRandom().shuffle(passwordList)
    password = ''.join(passwordList)
    return password

print ("Password is ", randomPassword())

#OP7
num1 = random.random()
num2 = random.uniform(9.5, 99.5)
print(f'Res: {num1 * num2}')

#OP8
print("Random secure Hexadecimal token is ", secrets.token_hex(64))
print("Random secure URL is ", secrets.token_urlsafe(64))

#OP9
dice = [1, 2, 3, 4, 5, 6]
print("Randomly selecting same number of a dice")
for i in range(5):
    random.seed(25)
    print(random.choice(dice))
    
#OP10
def getRandomDate(startDate, endDate ):
    print("Printing random date between", startDate, " and ", endDate)
    randomGenerator = random.random()
    dateFormat = '%m/%d/%Y'

    startTime = time.mktime(time.strptime(startDate, dateFormat))
    endTime = time.mktime(time.strptime(endDate, dateFormat))

    randomTime = startTime + randomGenerator * (endTime - startTime)
    randomDate = time.strftime(dateFormat, time.localtime(randomTime))
    return randomDate

print ("Random Date = ", getRandomDate("1/1/2016", "12/12/2018"))