from sys import exit
f = open("26_1868.txt")
n = int(f.readline())

booked = []

for line in f:
  row, place = map(int, line.split())

  booked.append((row, place))

booked.sort(reverse=True)

i = 0

while i < n:
  row = booked[i][0]
  mas = [booked[i][1]]
  i += 1
  while i < n and booked[i][0] == row:
    mas.append(booked[i][1])
    i += 1

  mas.reverse()

  for j in range(1, len(mas)):
    if mas[j] - mas[j - 1] == 3:
      print(row, mas[j-1] + 1)
      exit(0)
  

