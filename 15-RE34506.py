def f(x, A):
  return (x & 25 != 0) <= ((x & 17 == 0) <= (x & A != 0))



X = [v for v in range(0, 100)]


for A in range(1, 1000):
  if all(f(x, A) for x in X):
    print(A)
    break