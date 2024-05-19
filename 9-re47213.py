f = open("9 (11).csv")

mas = [list(map(int, line.split())) for line in f]

cnt = 0

for row in mas:
  d = {}

  for v in row:
    if v not in d:
      d[v] = 0
    d[v] += 1
  
  cnt_rep = 0
  l_sum, r_sum = 0, 0

  for v in d:
    if d[v] == 1:
      l_sum += v
    elif d[v] == 2:
      r_sum += 2*v
      cnt_rep += 1
    else:
      cnt_rep += 2

  if cnt_rep == 1 and l_sum / 4 <= r_sum: cnt += 1

print(cnt) 