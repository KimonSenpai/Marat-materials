



def change(n):

  for i in range(2):
    nn = n
    s_dig = 0
    while nn > 0:
      dig = nn % 2
      nn //= 2
      s_dig += dig

    n = 2*n + s_dig % 2

  return n

mas = []

for n in range(1, 93):
  res = change(n)
  if res > 93:
    mas.append(res)
  

print(min(mas))
