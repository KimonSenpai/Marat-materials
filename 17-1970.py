
f = open("17_1970.txt")

mas = []

for line in f:
    mas.append(int(line))
cnt, max_sum = 0, -20000
for i in range(1, len(mas)):
    if mas[i] % 3 == 0 or mas[i-1] % 3 == 0:
        cnt += 1
        max_sum = max(max_sum, mas[i] + mas[i - 1])

print(cnt, max_sum)

