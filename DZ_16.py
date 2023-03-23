a = int(input('Введіть висоту фігури: '))
for i in range(a):
    for x in range(a * 2 - 1):
        if x == a - 1 - i or x == a - 1 + i or i == a - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

b = int(input('Введіть висоту фігури: '))

for i in range(b):
    for x in range(b * 2 - 1):
        if x >= b - 1 - i and x <= b - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

c = int(input('Введіть висоту фігури: '))

for i in range(c):
    for x in range(c * 2 - 1):
        if x >= c - 1 - i and x <= c - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

for i in range(c - 2, - 1, - 1):
    for x in range(c * 2 - 1):
        if x == c - 1 - i or x == c - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

d = int(input('Введіть висоту фігури: '))

for i in range(d):
    for x in range(d * 2 - 1):
        if x >= d - 1 - i and x <= d - 1 + i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()

for i in range(d - 2, - 1, - 1):
    for x in range(d * 2 - 1):
        if x == d - 1 - i or x == d - 1 + i or x == d - 1:
            print('* ', end='')
        else:
            print('  ', end='')
    print()
