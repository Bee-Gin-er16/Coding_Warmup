from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import time


#OP1
date_string = "Feb 25 2020  4:20PM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)

#OP2
date_string = "Feb 25 2020 4:20PM"
datetime_object = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
print(datetime_object)

#OP3
given_date = datetime(2020, 2, 25)
print("Given date")
print(given_date)
res_date = given_date - timedelta(days=7)
print("New Date")
print(res_date)

#OP4
given_date = datetime(2020, 2, 25)
print("Given date is")
print(given_date.strftime('%A %d %B %Y'))

#OP5
given_date = datetime(2020, 7, 26)
print(f"Given day of the week is : {given_date.strftime('%A')}") #My way

#OP6
given_date = datetime(2020, 3, 22, 10, 0, 0)
print("Given date")
print(given_date)
res_date = given_date + timedelta(days=7, hours=12)
print("New Date")
print(res_date)

#OP7
milliseconds = int(round(time.time() * 1000))
print('time in milliseconds')
print(milliseconds)

#OP8
given_date = datetime(2020, 2, 25)
given_date = datetime(2020, 2, 25)
string_date = given_date.strftime("%Y-%m-%d %H:%M:%S")
print(string_date)

#OP9
given_date = datetime(2020, 2, 25).date()
months_to_add = 4
new_date = given_date + relativedelta(months=+ months_to_add)
print(new_date)

#OP10
# 2020-02-25
date_1 = datetime(2020, 2, 25)
# 2020-09-17
date_2 = datetime(2020, 9, 17)
delta = None
if date_1 > date_2:
    print("date_1 is greater")
    delta = date_1 - date_2
else:
    print("date_2 is greater")
    delta = date_2 - date_1
print("Difference is", delta.days, "days")