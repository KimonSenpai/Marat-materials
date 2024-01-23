f = open("26_7602.txt")

k = int(f.readline())
n = int(f.readline())

pas = [-1]*n
box = [-1]*k
times = []

for line, i in zip(f, range(n)):
  tin, tout = map(int, line.split())
  times.append((tin, 0, i))
  times.append((tout, 1, i))

times.sort()
last_box = -1
cnt = 0
for t, state, i in times:
  if state == 0:
    f = False
    for j in range(k):
      if box[j] == -1:
        f = True
        break
    if not f: continue

    box[j] = i
    pas[i] = j
    last_box = j
    cnt += 1
    
  else:#state == 1
    if pas[i] == -1: continue

    box[pas[i]] = -1
    
print(cnt, last_box + 1)
