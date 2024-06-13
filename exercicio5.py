# 5 - Um show será realizado no tribos bar. O corpo de bombeiros avisou para
# o Junior que a lotação máxima para assistir o evento é de 4 pessoas por m2.
# A área do lugar se da seguinte forma:
# Em formato de trapézio o local possui 145 metros de altura,
# 120 metros de largura do lado oposto ao palco, 75 metros de largura onde
# fica o palco.
# O palco é um retângulo com dimensões de 15x8,5 metros.

# Quantos Ingressos para o público Junior poderá vender?
# Dicas: para calcular a área total de um trapézio se usa: Área = [(base maior
# + base menor) / 2] x altura.
# Para calcular a área total de um retângulo se usa: Área = largura x altura.

areaPalco = 15 * 8.5

baseMaior = 120
baseMenor = 75
altura = 145
areaTrapezio = (baseMaior + baseMenor) / 2 * 145

areaPermitida = areaTrapezio - areaPalco

limiteIngressos = areaPermitida * 4

print(f"a quantidade de ingressos que podem ser vendidas é {limiteIngressos}")