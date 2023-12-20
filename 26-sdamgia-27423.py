f = open("26_demo.txt")

S, N = map(int, f.readline().split())

files = [int(line) for line in f]
files.sort()

cnt = 0
while S > 0:
  S -= files[cnt]
  cnt += 1

if S < 0:
  cnt -= 1
  S += files[cnt]

print(cnt)

S += files[cnt - 1]
for file in files[::-1]:
  if file <= S:
    print(file)
    break



