f = open("27.txt")

N = f.readline()

kr1 = kr2 = kr13 = kr26 = 0
pair_count = 0
for line in f:
  val = int(line)
  if val % 26 == 0:
    pair_count += kr1 + kr2 + kr13 + kr26
    kr26 += 1
  elif val % 13 == 0:
    pair_count += kr2 + kr26
    kr13 += 1
  elif val % 2 == 0:
    pair_count += kr13 + kr26
    kr2 += 1
  else:
    pair_count += kr26
    kr1 += 1

#pair_count = kr2*kr13 + kr26*(kr1 + kr2 + kr13) + kr26*(kr26 - 1)//2

print(pair_count)

