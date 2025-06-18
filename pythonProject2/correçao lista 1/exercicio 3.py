def calculaDiametro(raio):
    return 2 * raio
def calculaCircunferencia(pi, raio):
    return pi * raio * 2
# Main
def calculaAreaCircunferencia(pi, raio):
    return (pi * raio ** 2)


raio =float(input("digite o raio do criculo"))
pi = 3.14159

diametro = calculaDiametro(raio)
circunferencia = calculaCircunferencia(pi, raio)
area = calculaAreaCircunferencia (pi, raio)

print(" o diametro é de: ", diametro)
print("a circunferencia é de: ", circunferencia)
print("a area é de:", area)
