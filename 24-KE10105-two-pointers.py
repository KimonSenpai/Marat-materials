f = open("24_10105.txt")

# [l; r)

s = f.readline() + '$'

max_len = 0
l = r = cnt = 0

while True:
  while s[r] != '$' and (cnt < 100 or s[r] != 'T'):
    if s[r] == 'T':
      cnt += 1
    r += 1
  
  if max_len < r - l:
    max_len = r - l
  
  if s[r] == '$': break

  while cnt == 100:
    if s[l] == 'T':
      cnt -= 1
    l += 1

print(max_len)