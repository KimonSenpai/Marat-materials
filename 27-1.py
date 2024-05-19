# В последовательности натуральных чисел найти 
# максимальную сумму пары, кратную 150. 
# 0 - признак конца последовательности.

mas = [0]*150
max_sum = 0
while True:
  val = int(input())
  if val == 0: break

  max_sum = max(max_sum, val + mas[-val%150])
  mas[val%150] = max(mas[val%150], val)


print(max_sum)