import json
space = " "
string = 'zakaria'
string2 = 'fatihi'
s3 = string + space + string2
numbers = '1234567890'
listt = ['zak', 'fa']
list2 = [1, '2', 'zak']
list3 = []

for x in list2:
    if isinstance(x, int):
        list3.append(int(x))
    elif isinstance(x, str):
        list3.append(x)
list4 = json.dumps(list3)
list4 = json.loads(list4)  # convert back to python obj
l5 = list(string2)
l5 = '--'.join(l5)
l5 = l5.split('----')

x = ['"abc*"', 'def:"', '"ghi"', 'nop']
y = []

for item in x:
    print(item.strip('":*'), end=' ')
    y += item.strip('":*')
print('')

y = ''.join(y)
print(y)

print(y.translate(str.maketrans('abc', '123')))

position = y.rfind('f')
y = y[:position] + y[position] + '123' + y[position + 1:]
print(y)


data = {
    "name": "John Smith",
    "age": 30,
    "city": "New York"
}
with open("data.json", "w") as outfile:
    json.dump(data, outfile)
with open("data.json", "r") as infile:
    data = json.load(infile)

list4 = json.load(open("data.json", "r"))

print(f'list={listt} \nlist2={list2} \nlist3={list3} \nlist4={list4}')
