#sem dicionario
matricula1 = 2026001
nome1 = "Ana Silva"
telefone1 = "9999-8888"

#com dicionario
aluno = {
    "matricula": 2026001,
    "nome": "Ana Silva",
    "telefone": "9999-8888"
}

print(aluno)

contato = {
    "@camilaqueiroz" = "Camila Queiroz",
    "@brunamarquezine": "Bruna M.",
    "@sheronmenezes": "Sheron M.",
    "@paolaoliveira": "Paola O."
}

print(contato)
print(type(contato))

# Acesso direto
print(contato["@camilaqueiroz"])

# Acesso seguro com get()
print(contato.get("@paolaoliveira"))
print(contato.get("@inexistente"))
print(contato.get("@inexistente", "Não encontrado"))


#add novo elemento
contato["@giovana"] = "Giovanna"
print("Após add: ", contato)

#atualiza elemento existente
contato["@paolaoliveira"] = "paolaoliveira"
print("Após add: ", conatato)

contato.update({
    "@brunamarquezine": "Bruna Marquezine",
    "@camilaqueiroz": "Camila Q."
})

print("Após atualização: ", contato)

#pop: remove e retorna
removido = contato.pop("@paolaoliveira")
print(f"Removido: {removido}")
print("Após o del: ", contato)

# del remove sem retorna
del contato["@camilaqueiroz"]
print("Após o del: ", contato)

#clear esvazia tudo
copia = dict(contato)
contato.clear()
print("Após clear: ", contato)
print("Cópia ", copia)

print("Número de contato: ", len(contato)) #tamanho dicio

#verificar existencia
if "@joão" in contato:
    print("Encontrado: {contato['@joão]}")

    if "inexistente" in contato:
        print("Existe")
    else:
        print("Não existe.")