# 3 - A idade da minha mãe multiplicada pela minha idade é igual a 525. Se
# quando eu nasci minha mãe tinha 20 anos, quantos anos eu tenho?
# Solução MATEMÁTICA
# Considerando a minha idade igual a x, podemos então considerar que a
# idade da minha mãe é igual a x + 20. Como sabemos o valor do produto das
# nossas idades,
# então:
# x . (x + 20) = 525
# Aplicando a propriedades distributiva da multiplicação:
# x2 + 20 x - 525 = 0
# Chegamos então em uma equação do 2o grau completa,
# com a = 1, b = 20 e c = - 525.
# USE
# import math e a função math.sqrt(delta) para pegar a raiza do delta

import math


idadeNasceu = 20

delta = idadeNasceu**2 - 4 * 1 * -525
idadeFilha = (-20 + math.sqrt(delta)) / 2 * 1

idadeMae = idadeNasceu + idadeFilha

print(f"Idade Filha {idadeFilha}")
print(f"Idade Mãe {idadeMae}")