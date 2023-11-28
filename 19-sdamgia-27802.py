from functools import lru_cache

def go(x):
  return [f(x + 1), f(x + 4), f(x*5)]

@lru_cache(None) # ускорение
def f(x):
  if x >= 68:
    return -0
  
  mas = go(x)

  if all(v > 0 for v in mas):
    return -max(mas) - 1
  else:
    return -max(v for v in mas if v <= 0) + 1
  

print("problem 19")
for s in range(1, 67 + 1):
  if +1 in go(s):
    print(s)
    break 

print("problem 20")
for s in range(1, 67 + 1):
  if f(s) == +3:
    print(s)

print("problem 21")
for s in range(1, 67 + 1):
  if f(s) == -4:
    print(s)
    break

