n = int(input('число крім нуля:'))
counter = 0
suma = 0
sr = 0
chot = 0
ne_chot = 0
min_zna = max_zna = n
while True:
    n = int(input('число крім нуля:'))
    if n == 0:
        break
    counter += 1
    suma += n
    sr = suma / counter
    if n % 2 == 0:
        chot += 1
    if n % 2 != 0:
        ne_chot += 1
    if n < min_zna:
        min_zna = n
    if n > max_zna:
        max_zna = n
print('кількість чисел :',counter, 'сума:', suma,'парні:', chot, 'не парні:'
, ne_chot,'середня сума:', sr,'мінімальне значеня;', min_zna, 'максимальне значення:', max_zna)