numeroI = int(input("Digite o valor inicial: "))
numeroF = int(input("Digite o valor final: "))

intervalo = numeroF - numeroI

if (intervalo < 100):
    for i in range(numeroI, numeroF+1):
        print(i)
else:
    print("intervalo invalido")