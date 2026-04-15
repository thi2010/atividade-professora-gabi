def media():
    notas = []
    
    for i in range(3):
        try:
            notas.append(float(input("Digite a nota: ")))
        except:
            print("Erro: digite apenas números.")
            return
    
    print("Média:", round(sum(notas) / 3, 2))


def total_compra():
    try:
        p1 = float(input("Preço 1: "))
        p2 = float(input("Preço 2: "))
    except:
        print("Erro: digite apenas números.")
        return
    
    print("Total:", round(p1 + p2, 2))