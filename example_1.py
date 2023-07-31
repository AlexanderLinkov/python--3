s = list(input('Введите элементы списка через пробел: ').split())
r = []
for i in s:
    if s.count(i) > 1 and i not in r:
        r.append(i)
print(r)