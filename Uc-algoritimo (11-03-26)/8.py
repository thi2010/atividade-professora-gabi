valor = float(input("Valor: "))

if valor < 100:
    desconto = 0
elif valor < 500:
    desconto = valor * 0.05
elif valor < 1000:
    desconto = valor * 0.10
else:
    desconto = valor * 0.15

print("Desconto:", desconto)
print("Final:", valor - desconto)