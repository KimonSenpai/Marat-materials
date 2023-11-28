val = 144

divs = []
div = 2

while div*div <= val:
  if val % div == 0:
    divs.append(div)
    if div*div != val:
      divs.append(val//div)
  
  div += 1

print(*divs)# divs = [2, 72, 3, ...]