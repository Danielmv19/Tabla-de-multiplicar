
def TablaMultiplicar(num):
    resultado = ()

    for i in range(1, 13):
        resultado = num * i
        print(" {} x {} = {} ".format(num, i, resultado))

TablaMultiplicar(4)