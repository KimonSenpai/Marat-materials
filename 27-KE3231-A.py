f = open("27-A_3231.txt")

N = int(f.readline())

mas = [int(line) for line in f]
min_cost = 10**20
min_num = 0
for i in range(N):
  cost = 0
  for j in range(N):
    if j == i: continue

    cost += mas[j]*min((i - j)%N, (j - i)%N)

  if cost < min_cost:
    min_cost = cost
    min_num = i + 1

print(min_num)