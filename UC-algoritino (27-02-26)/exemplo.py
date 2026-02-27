altura = float(input("Digite a sua altura"))
altura = altura * 100

print(f"Sua altura é de {altura} cm")
print("Sua altura é de: ", altura, "cm")

nome = "Gaby"
idade = 23

texto = "Meu nome é {} e tenho {} anos".format(nome, idade)
texto = "Meu nome é {n} e tenho {i} anos".format(n=nome,i=idade)
texto = "Meu nome é %s e tenho %d anos" % (nome,idade)
print(texto)