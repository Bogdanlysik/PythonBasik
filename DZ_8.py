s = input('Введіть рядок:')
ch = input('введіть символ:')
b = list(s)

for a in range(len(b)):
    if b[a] == ch:
        print('індекс:', a)