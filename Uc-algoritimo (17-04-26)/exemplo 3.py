total = 0

valor = float(input("Digite um valor (0 para parar): "))

while valor != 0:
    total = total + valor
    valor = float(input("Digite outro valor (0 para parar): "))

print("Total:", total)