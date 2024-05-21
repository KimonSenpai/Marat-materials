f = open("27-B_3231.txt")

N = int(f.readline())

mas = [int(line) for line in f]

lsum = rsum = 0
s = 0

for i in range(1, N//2 + 1):
  rsum += mas[i]
  s += mas[i] * i

for i in range(0, N//2):
  lsum += mas[-i]
  s += mas[-i] * i

min_cost = s
min_num = 1

for i in range(1, N):
  s += lsum - rsum

  opos = (i + N//2)%N
  lsum +=  mas[i] - mas[opos]
  rsum += -mas[i] + mas[opos]

  if s < min_cost:
    min_cost = s
    min_num = i + 1

print(min_num)