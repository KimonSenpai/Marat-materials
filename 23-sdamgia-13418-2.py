# 1 -> 27, не проходя 26 и проходя 4



def f(fr, to):
  if fr == to:
    return 1
  if fr > to:
    return 0
  
  res = f(fr, to - 1)
  if to % 2 == 1:
    res += f(fr, to // 2)
  return res

print(f(1, 4)*f(4, 27) - f(1, 4)*f(4, 26)*f(26, 27))