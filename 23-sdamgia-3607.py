

def f(fr, to): # кол-во способов получить fr->to
  if fr == to:
    return 1
  if fr > to:
    return 0
  
  res = f(fr, to - 2)
  
  if to % 5 == 0:
    res += f(fr, to // 5)
  
  return res

print(f(2, 50))