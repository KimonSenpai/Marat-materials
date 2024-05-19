f = open("27.txt")

N = f.readline()

kr1 = kr2 = kr13 = kr26 = 0
max_prod = 0
for line in f:
  val = int(line)
  if val % 26 == 0:
    max_prod = max(max_prod, val*kr1, val*kr2, val*kr13, val*kr26)
    kr26 = max(kr26, val)
  elif val % 13 == 0:
    max_prod = max(max_prod, val*kr2, val*kr26)
    kr13 = max(kr13, val)
  elif val % 2 == 0:
    max_prod = max(max_prod, val*kr13, val*kr26)
    kr2 = max(kr2, val)
  else:
    max_prod = max(max_prod, val*kr26)
    kr1 = max(kr1, val)

print(max_prod)

