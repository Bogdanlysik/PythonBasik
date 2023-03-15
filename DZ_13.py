d = {
  'apple': ['malum', 'pomum', 'popula'],
  'fruit': ['baca', 'bacca', 'popum'],
  'punishment': ['malum', 'multa']
}
new = {}
for key, wely in d.items():
  for i in wely:
    if i not in new:
      new [i] = [key]
    else:
      new[i].append(key)
print(new)
