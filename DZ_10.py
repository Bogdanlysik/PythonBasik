nam = [12, 13, 34, 21, 53, 66, 53, 12]
counter = 0
for i in range(1, len(nam)-1):
    if nam[i] > nam[i+1] and nam[i] > nam[i-1]:
        counter += 1
print(counter)
