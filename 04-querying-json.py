import requests, json 

response = requests.get("https://mul14.github.io/data/employees.json")
data = response.json()

def salary(data):
    if (data['salary'] > 15000000): 
        return {
            "first_name":data['first_name'],
            "last_name":data['first_name']
            }
    else: 
        return

def location(data):
    city = data['addresses'][0]['city']
    if 'DKI Jakarta' in city: 
        return data['first_name']
    else: 
        return
def birthDay(data):
    month = int(data['birthday'].split('-')[1]) == 4
    if month :
        return {
            "Name":data['first_name']
            }
def department(data):
    if data['department']['name'] == 'Research and development':
        return data['first_name']
def absent(data):

    def countAbsent(var): return int(var.split('-')[1]) == 10 and int(var.split('-')[0]) == 2019

    month = filter(countAbsent,data['presence_list'])
    return {"name":data['first_name'],"absent":len(list(month))}



Salary = list(filter(None,map(salary,data)))
Location = list(filter(None,map(location,data)))
BirthDay = list(filter(None,map(birthDay,data)))
Department = list(filter(None,map(department,data)))
Absent = list(filter(None,map(absent,data)))

print(Salary)
print(Location)
print(BirthDay)
print(Department)
print(Absent)