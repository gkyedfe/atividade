# 6 - Willian gostaria de saber a altura de seus jogadores preferidos da NBA.
# Como a liga é americana, a altura dos jogadores é sempre anunciada em
# pés, e não metros.
# Desenvolva o algoritmo que transforme pés em metros.
# Deve-se multiplicar pés por 0.3048,2 para saber a altura em metros.

Pes = float(input("Digite a altura em pes dos jogador: "))

alturaMetros = Pes * 0.3048

print(f"A altura do jogador em metros é {alturaMetros} M")