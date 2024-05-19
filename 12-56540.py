
import itertools as it

def change(s: str):
  while "00" not in s:
    if "011" in s:
      s = s.replace("011", "101", 1)
    else:
      s = s.replace("01", "40", 1).replace("02", "20", 1).replace("0222", "1401", 1)
  return s



i = 13
min_cnt = 1000000
for inds in it.combinations(range(2*i), i):
  s = ["1"]*(2*i)
  for j in inds:
    s[j] = "2"
  s = '0' + ''.join(s) + '0'
  
  s = change(s)

  if s.count('1') == 8 and s.count('2') == 13:
    min_cnt = min(min_cnt, s.count('4'))

print(min_cnt)