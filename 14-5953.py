#10x0_17 = 1*17**3 + x*17
#abcde_q = e*q**0 + d*q**1 + c*q**2 + b*q**3 + a*q**4
def f(x):
  return 17**3 + x*17 + 15 + 15*17 + x*17**2 + 15*17**4

for x in range(0, 17):
  if f(x) % 13 == 0:
    print(f(x)//13)
    break