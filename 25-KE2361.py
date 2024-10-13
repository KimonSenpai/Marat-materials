
cnt = 0
for val in range(550001, 10000000):
  if cnt == 5: break

  divs = []
  div = 2
  while div*div <= val:
    if val % div == 0:
      if div % 10 == 7:
        divs += [div]
      
      if div*div != val:
        d = val // div
        if d % 10 == 7:
          divs += [d]
    div += 1
  
  if len(divs) == 3:
    print(val, max(divs))
    cnt += 1