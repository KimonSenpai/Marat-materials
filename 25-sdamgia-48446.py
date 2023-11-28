

for star_len in range(0, 4):
  for star in range(0, 10**star_len):
    for ques in range(0, 10):
      v = ""
      if star_len == 0:
        v = f"1{ques}49341"
      else:
        v = f"1{ques}493{star:0{star_len}}41"

      if int(v) % 2023 == 0:
        print(v)