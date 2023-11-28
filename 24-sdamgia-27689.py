f = open("24_demo.txt")

s = f.readline().strip()

cnt, max_cnt = 0, 0

for c in s:
  if c == 'T':
    cnt += 3
  else:
    cnt += int(c)
    max_cnt = max(max_cnt, cnt)
    cnt = 0

print(max_cnt)