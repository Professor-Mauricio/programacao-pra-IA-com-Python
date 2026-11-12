while(True):
    a = int(input("Digite o primeiro valor A: "))
    b = int(input("Digite o segundo  valor B: "))
    c = int(input("Digite o terceiro valor C: "))


    #colocar em ordem crescente, do menor pro maior
    # Primeira solução: 6 comparações possíveis.

    if (a > b) and (b > c):
        print(c,b,a)
    if (a > c) and (c > b):
        print(b,c,a)
    if (b > a) and (a > c):
        print(c,a,b)
    if (b > c) and (c > a):
        print(a,c,b)
    if (c > a) and (a > b):
        print(b,a,c)
    if (c > b) and (b > a):
        print(a,b,c)              

        
    #colocar em ordem crescente, do menor pro maior
    # terceira solução

    if (a > b):
        if (b > c):
            print(c,b,a)
        else:
            if (a > c):
                print(b,c,a)
            else:
                print(b,a,c)
    elif (b > c):
        if (a > c):
            print(c,a,b)
        else:
            print(a,c,b)
    elif (c > b):
        if (c > a):
            print(a,b,c)
