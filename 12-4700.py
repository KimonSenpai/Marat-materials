def isPrime(val):
  div = 2
  while div*div <= val:
    if val % div == 0:
      return False
    div += 1
  return True

# val = a*b
# val = sqrt(val)*sqrt(val)

for n in range(30):
  if isPrime(117 + 4*n):
    print(n)
    exit(0)