from sys import exit
f = open("26_1868.txt")
n = int(f.readline())

booked = {}

for line in f:
  row, place = map(int, line.split())
  if row not in booked:
    booked[row] = []
  booked[row].append(place)

r, p = 100000000, 100000000000
for row in booked:
  mas = booked[row]
  mas.sort()
  for j in range(1, len(mas)):
    if mas[j] - mas[j-1] == 3:
      r = row
      p = mas[j-1] + 1
      break
print(r, p)