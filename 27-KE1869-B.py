f = open("27_B_1869.txt")

N = int(f.readline())

mas = [int(line.strip()) for line in f]

s = 0

min_pref = [-1]*89
min_pref[0] = 0
pref_len = [0]*89

max_sum = 0
min_len = 0

for i in range(N):
  s += mas[i]
  j = s%89
  if min_pref[j] == -1:
    min_pref[j] = s
    pref_len[j] = i + 1
  else:
    if s - min_pref[j] > max_sum:
      max_sum = s - min_pref[j]
      min_len = i+1 - pref_len[j]
    elif s - min_pref[j] == max_sum:
      min_len = min(min_len, i+1 - pref_len[j])

print(min_len)