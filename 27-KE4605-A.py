f = open("27A_4605.txt")

N = int(f.readline())

mas = []
for line in f:
  pos, cnt = map(int, line.split())
  cnt = cnt // 36 + (cnt % 36 > 0)
  mas.append((pos, cnt))

min_cost = 10**18
for i in range(N):
  cost = 0
  for j in range(N):
    cost += mas[j][1]*abs(mas[j][0] - mas[i][0])
  min_cost = min(min_cost, cost)

print(min_cost)