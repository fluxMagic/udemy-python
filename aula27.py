"""
Fatiamento de strings
 012345678
 Olá mundo
 -987654321

 Fatiamento [i:f:p] [::]  # i= início  f= meio  p= intervalos
 Obs.: a função len retorna a qtd
 de caracteres da str
"""

variavel = 'Olá mundo'
print(variavel[0:9:2])

variavel = 'Olá mundo'
print(variavel[-1:-10:-1])