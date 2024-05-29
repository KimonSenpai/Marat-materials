from fnmatch import fnmatch


for v in range(3023, 10**10, 3023):
  if fnmatch(str(v), "1?954*21"):
    print(v)