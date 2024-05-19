f = open("27-B_23.txt")

N = int(f.readline())

s = 0
min_dif = 10**18

for i in range(N):
  a, b = map(int, f.readline().split())
  s += max(a, b)
  dif = abs(a - b)
  if dif % 3 != 0:
    min_dif = min(min_dif, dif)

if s % 3 == 0:
  s -= min_dif

print(s)


