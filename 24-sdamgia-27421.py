f = open("24_demo_2021.txt")

s = f.readline().strip() + '$'

prev = s[0]
cnt, max_cnt = 1, 0

for c in s[1:]:
  if c != prev and c != '$':
    cnt += 1
  else:
    max_cnt = max(max_cnt, cnt)
    cnt = 1
  prev = c

print(max_cnt)