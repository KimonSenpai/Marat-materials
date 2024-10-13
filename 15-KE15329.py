def f(n, m):
    return int(n % m == 0)



def z(x, A):
    return (not f(x, A)) <= (f(x, 28) <= (not(f(x, 49))))

X = list(range(1, 1000))

print(not (True) <= True)

for A in range(1000, 1, -1):
    if all(z(x, A) for x in X):
        print(A)
        break