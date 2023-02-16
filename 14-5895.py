def f(x, y):
  return 12 + y*16 + x*16**2 + 5*16**3 + 7 + x*y + x*y**2 + 8*y**3


s = set()
for x in range(0, 16):
  for y in range(max(8 + 1, x + 1), 16):
    s.add(f(x, y))

print(len(s))