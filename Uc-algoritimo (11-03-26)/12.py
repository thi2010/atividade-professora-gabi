total = 0
qtd = 0

while True:
    valor = float(input("Depósito: "))

    if valor == 0:
        break

    total = total + valor
    qtd = qtd + 1

print("Total:", total)
print("Transações:", qtd)