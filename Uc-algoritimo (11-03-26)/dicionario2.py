contato = {
    "@camila": "Camila",
    "@paola": "paolla",
    "@sheron": "Sheron",
    "@bruna": "Bruna"
}


#Obter chave
print("Chaves: ")
for insta in contato.keys():
    print(insta)

#obter valores
print("\n Valores: ")
for nome in contato.values():
 print(nome)

    #obter pares
 print("\n Pares: ")
 for insta, nome in contato.items():
  print(f"{insta} --> {nome}")

  contato = {
    "@camila": 1.70,
    "@paola":1.80,
    "@sheron": 1.55,
    "@bruna": 1.60
}
  
  print("ordenada por chave:")
  for insta in sorted(contato.keys()):
    print(f"{insta} --> {contato[insta]:.2f}m")

    from operator import itemgetter
    print("\n ordenado por valor (altura):")
    for insta, estatura in sorted(contato.itens(), key = itemgetter(1)):
      print(f"{insta} --> {estatura: .2f}m")