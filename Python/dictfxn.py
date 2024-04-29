#OP1
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res = {i : j for i,j in zip(keys, values)}
print(res)

#OP2
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
res = {**dict1, **dict2}
print(res)

#OP3
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(sampleDict['class']['student']['marks']['history'])

#OP4
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
res = dict.fromkeys(employees, defaults)
print(res)

#OP5 and OP6
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
res = {k: sample_dict[k] for k in keys}
print(res)

krev = ["name", "salary"]
res = {k: sample_dict[k] for k in sample_dict.keys() - krev}
print(res)

#OP7
sample_dict = {'a': 100, 'b': 200, 'c': 300}
print('200 present in dict') if 200 in sample_dict.values() else print("Value not present in dict")

#OP8
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
sample_dict['location'] = sample_dict.pop('city')
print(sample_dict)

#OP9
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
print(min(sample_dict, key=sample_dict.get))

#OP10
sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
sample_dict['emp3']['salary']=8500
print(sample_dict)
