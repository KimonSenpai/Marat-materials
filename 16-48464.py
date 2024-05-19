from functools import lru_cache

@lru_cache(None)
def F(n):
    if n == 0:
        return 0
    return (F(n-1) + n)

# f(n) = f(n - 1) + n = f(n - 2) + (n - 1) + n = 1 + 2 + ... + n
cnt = 0

# [765432012, 1542613236]
for i in range(765432010 + 2, 1542613235 + 2):
    if i % 3 == 0 :
        cnt += 1

print(cnt)