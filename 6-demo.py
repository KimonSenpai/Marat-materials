from math import pi, tan 

cnt = 0
for x in range(1, 10):
  for y in range(0, 11):
    if x*tan(pi/6) < y < -x*tan(pi/6) + 10:
      cnt += 1

print(cnt)
print(9*19 + 8*18 - 5*8)