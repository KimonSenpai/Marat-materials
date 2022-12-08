def change(n):
  if n%2 == 0:
    n = n*4
  else:
    n = n*4 + 3
  return n


for n in range(1, 115):
  if change(n) > 115:
    print(n)
    break