f = open("27_A_1869.txt")

N = int(f.readline())

mas = [int(line.strip()) for line in f]
max_sum = 0
min_len = 0


for lhs in range(0, N):
  for rhs in range(lhs + 1, N + 1):
    s = sum(mas[lhs:rhs])
    if s % 89 != 0: continue
    if s > max_sum:
      max_sum = s
      min_len = rhs - lhs
    elif s == max_sum:
      min_len = min(min_len, rhs - lhs)

print(min_len)