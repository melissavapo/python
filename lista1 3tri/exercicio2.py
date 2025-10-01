def NumeroMaior(numero1, numero2, numero3):
    if (numero1 >= numero2 and numero1 >= numero3):
        print("o primeiro numero é maior que os outros numeros")
    if (numero2 >= numero1 and numero2 >= numero3):
        print("O segundo numero é maior que os outros numeros")
    if (numero3 >= numero1 and numero3 >= numero2):
       print("o terceiro numero é maior que os outros numeros")

numero1 = int(input("digite o primeiro numero inteiro"))
numero2 = int(input("digite o segundo numero inteiro"))
numero3 = int(input("digite o terceiro numero inteiro"))


NumeroMaior(numero1, numero2, numero3)

