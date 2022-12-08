def change(n):
    b = ""
    while n > 0:
        b = str(n % 4) + b
        n = n // 4
    if n % 2 != 0:
        b = "2" + b + "11"
    else:
        b = "13" + b +"02"
    return int(b, 4)

mas = []

for n in range(1, 1000):
    x = change(n)
    if x > 1000:
        mas.append(x)

print(min(mas))