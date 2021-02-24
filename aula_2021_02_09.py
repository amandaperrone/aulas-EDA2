# estrutura de repetição if
valor1 = 3
valor2 = 5

if valor1 > valor2:
    print("Valor 1 é maior que valor 2")
elif valor1 == valor2:
    print("Valor 1 é igual valor 2")
else:
    print("valor 2 é maior que o valor 1")

print("-------------------\n")


# função
def soma(a, b):
    return a + b

print(soma(1, 2))

print("-------------------\n")

def soma(a, b):
    print(a + b)

print(soma(1, 2))

print("-------------------\n")

# atribuindo os retornos da função
def soma(c, d):
    return c + d, c, d

resultado, op1, op2 = soma(1, 2)

print("Resultado:", resultado, "Operador 1:", op1, "Operador 2:", op2)

print("Resultado %i operador1 %i e operador 2 %i" %(resultado, op1, op2))

print("-------------------\n")

#descartando valores
def soma(a, b, fator_correcao):
    return a+b+fator_correcao, a, b

resultado, _, _ = soma (1,2, fator_correcao=5) 
# pode-se passar as variáveis em outra ordem
# resultado, _, _ = soma (b=1, a=2, fator_correcao=5)

print("O resultado é", resultado)

# definindo valor padrão
def soma(a, b, fator_correcao=0): #nesse caso o fator_correcao é parâmetro opcional
  return a+b+fator_correcao, a, b

resultado, _, _ = soma (1,2) 

print("O resultado é", resultado)

print("-------------------\n")

print("EXERCICIO 1013 URI")
''' x = 7
y = 14
z = 106 '''
x = 217
y = 14
z = 6

if x > z:
  if x > y:
    print(x, "eh o maior")
  else:
    print(y, "eh o maior")
elif z > y:
  print(z, "eh o maior")
else:
  print(y, "eh o maior")

print("-------------------\n")

print("EXERCICIO 1044 URI")
a = 6
b = 25

if b % a == 0:
  print("Sao multiplos")
else:
  print("Nao sao multiplos")

print("-------------------\n")

print("EXERCICIO 3")
def maior (a, b, c):
  if a > b:
    if a > c:
      print(a, "eh o maior")
    else: 
      print(c, "eh o maior")
  elif b > c:
    print(b, "eh o maior")
  else:
    print(c, "eh o maior")

def multiplos (x, y):
  if x%y == 0:
    print("São múltiplos")
  else:
    print("Não são múltiplos")

maior (1250, 500, 100)
print("\n")
multiplos (10, 4)
