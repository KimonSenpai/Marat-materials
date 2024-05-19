f = open("27-A_23.txt")

N = int(f.readline())

mas = [list(map(int, f.readline().split())) for _ in range(N)]

sums = [0]

for i in range(N):
  new = []
  for j in [0, 1]:
    for val in sums:
      new.append(val + mas[i][j])
  sums = new

max_sum = 0
for val in sums:
  if val % 3 != 0:
    max_sum = max(max_sum, val)

print(max_sum)