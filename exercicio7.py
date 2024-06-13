# 7 - Peça a usuário para digitara porcentagem, e depois o número que ele
# deseja saber a porcentagem o programa deve calcular o percentual exemplo
# quanto é 25% de 80.

numero = float(input("Digite o numero: "))
porcentagem = float(input("Digite a porcentagem a ser calculada: "))

porcentagemNumero = (numero * porcentagem / 100)

print(f"{porcentagem}% de {numero} é igual a {porcentagemNumero}")