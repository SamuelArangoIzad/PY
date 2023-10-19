def años_bisiestos(inicio):
    bisiestos = [año for año in range(inicio +1, inicio+100)if(año%4==0 and año%100 != 0)or(año % 400==0)]
    for bisiestos in bisiestos[:30]:
        print(bisiestos)
año_usuario = int (input("Please , Write The Starting Year To Know The NExt Leap Years: "))
años_bisiestos(año_usuario)