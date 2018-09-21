def ehPrimo(n):
    for x in range(2, int(n / 2 + 1)):
        if not n % x:
            return False
    return True
cont = 0
i = 2
while cont < 10001:
    if ehPrimo(i):
        cont += 1
    if cont == 10001:
        print(i)
    i += 1
    