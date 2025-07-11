mark = {
    'bangla': 80,
    'english': 'A',
    'maths': '70',
}
print('Dictinary Key')
for key in mark:
    print(key)

print('Dictinary Values')
for value in mark.values():
    print(value)

print('Dictinary Key&value')
for k, v in mark.items():
    print(k, ':', v)


print('*************Range in for loop************')

for i in range(5):
    print(i+1)

for num in range(1, 11):
    print(num)

print('Range Step')
for num in range(20, 31, 2):
    print(num)

print("*****************Break Statement********************")
languages = ['HTML','CSS','C++','Python']

for lang in languages:
    if lang == 'C++':
        break
    print(lang)

print("*****************Continue Statement********************")

for lang in languages:
    if lang == 'CSS':
        continue
    print(lang)


print('*****************Nested For Loop********************')
names = ["Alice", "Bob", "Charlie", "Diana"]
for name in names:
    print('Name is: ', name)
    for nam in name:
        if nam=='Charlie':
            continue
        print(nam)

        
