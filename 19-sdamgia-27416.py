# +1, *2
#win: 77
#start: (7, S), 1<=S<=69
from functools import lru_cache
def go(x, y):
  return [f(x + 1, y), f(x, y + 1), f(x*2, y), f(x, y*2)]

@lru_cache(None)
def f(x, y):
  if x + y >= 77:
    return -0
  
  mas = go(x, y)

  if all(x > 0 for x in mas):
    return -max(mas) - 1
  else:
    return -max(x for x in mas if x <= 0) + 1
  
print("problem 19")
for s in range(1, 69 + 1):
  if +1 in go(7, s):
    print(s)
    break

print("problem 20")
for s in range(1, 69 + 1):
  if f(7, s) == +3:
    print(s)

print("problem 21")
for s in range(1, 69 + 1):
  if f(7, s) == -4:
    print(s)


