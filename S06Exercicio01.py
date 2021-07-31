num = 0

for n in range(1, 1000):
    if n%3==0:
        print(f'{n} ', end='')
        num += 1
        if num==5:
            break
