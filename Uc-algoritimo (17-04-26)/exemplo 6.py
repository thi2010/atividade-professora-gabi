frase = input("digita: ")

vogais = 0

for letra in frase:
    if letra in "aeiou":
        vogais += 1

print(vogais)