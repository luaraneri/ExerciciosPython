print("Digite n:")
n = (int)(input())

for i in range(n):
    i_fatorial = 1
    if i != 0:
        for m in range(1,i+1):
            i_fatorial *= m
    for j in range(i+1):
        j_fatorial = 1
        if j != 0:
            for m in range(1, j+1):
                j_fatorial *= m
        k = i - j
        k_fatorial = 1
        if k != 0:
            for m in range(1, k+1):
                k_fatorial *= m
        result = int((i_fatorial)/(j_fatorial*k_fatorial))
        print(f'{result}  ', end='')
    print('\n', end='')
