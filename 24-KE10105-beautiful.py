f = open("24_10105.txt")

# T ... T

s = 'T' + f.readline() + 'T'

mas = [i for i in range(len(s)) if s[i] == 'T']

max_len = 0

for i in range(0, len(mas) - 101):
  max_len = max(max_len, mas[i + 101] - mas[i] - 1)

print(max_len)