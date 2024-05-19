import itertools as it

f = open("27-A_23.txt")

N = int(f.readline())

mas = [list(map(int, f.readline().split())) for _ in range(N)]
'''
max_sum = 0
for pr in it.product(*mas):
  s = sum(pr)
  if s % 3 != 0:
    max_sum = max(max_sum, s)

print(max_sum)
'''
max_sum = 0
for pr in it.product([0, 1], repeat=N):
  s = 0
  for i in range(N):
    s += mas[i][pr[i]]
  if s % 3 != 0:
    max_sum = max(max_sum, s)

print(max_sum)
#print(list(it.product([0, 1], repeat=3)))