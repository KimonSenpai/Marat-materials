
def f(val):
  x = val
  s = 0
  while x > 0:
    s += x % 2
    x //= 2
  
  return val*2 + s%2


for val in range(1, 77):
  if f(f(val)) > 77:
    print(val)
    break