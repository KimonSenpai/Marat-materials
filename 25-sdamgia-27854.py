for i in range(110203, 110245+1):
    divs = []
    div = 1

    while div*div <= i:
        if i % div == 0:
            if div % 2 == 0:
                divs.append(div)
            if div*div != i and (i // div) % 2 == 0:
                divs.append(i//div)

        div += 1
    if len(divs) == 4:
        print(*sorted(divs))