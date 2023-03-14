a = input('Введіть текст :')
b = a.split()
c = {}
for i in b:
    if i in c:
        c[i] += 1
    else:
        c[i] = 1
print('Скільки разів зустрівся текст :',c)
