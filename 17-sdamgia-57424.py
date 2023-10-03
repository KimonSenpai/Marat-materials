f = open("17_57424.txt")

mas = [int(line) for line in f]


max_bi = max(val for val in mas if 9 < val < 100)

cnt, max_sum = 0, 0

for i in range(1, len(mas)):
  if (9 < mas[i-1] < 100) + (9 < mas[i] < 100) == 1:
    if (mas[i-1] + mas[i])%max_bi == 0:
      cnt += 1
      max_sum = max(max_sum, mas[i - 1] + mas[i])

print(cnt, max_sum)

