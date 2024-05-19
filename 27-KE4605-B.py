f = open("27B_4605.txt")

N = int(f.readline())

mas = []
for line in f:
  pos, cnt = map(int, line.split())
  cnt = cnt // 36 + (cnt % 36 > 0)
  mas.append((pos, cnt))

s = 0
lsum = mas[0][1]
rsum = 0

for i in range(1, len(mas)):
  rsum += mas[i][1]
  s += mas[i][1]*(mas[i][0] - mas[0][0])

min_sum = s

for i in range(1, len(mas)):
  s += (mas[i][0] - mas[i-1][0])*(lsum - rsum)
  rsum -= mas[i][1]
  lsum += mas[i][1]

  min_sum = min(min_sum, s)

print(min_sum)