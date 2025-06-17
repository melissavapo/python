def soma(numero1, numero2):
  return numero1 + numero2

def subtracao(numero, numero2):
    return numero1 - numero2

def multiplicacao(numero1, numero2):
    return numero1 * numero2

def divisao(numero1, numero2):
    return numero1 / numero2

numero1 = int(input("Digite um numero inteiro!"))
numero2 = int(input("Digite um numero inteiro!"))

resultadoSoma = soma(numero1, numero2)
resultadoSubtracao = subtracao(numero1, numero2) #As variaveis sao argumentos da chamada da funcao
resultadoMultiplicacao = multiplicacao(numero1, numero2)
resultadoDivisao = divisao(numero1, numero2)

print("O resultado da funcao soma", resultadoSoma)
print("o resultado da funcao subtracao", resultadoSubtracao)
print("o resultado da funcao multiplicacao", resultadoMultiplicacao)
print("o resultado da funcao divisao", resultadoDivisao)