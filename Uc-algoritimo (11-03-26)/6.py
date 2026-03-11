idade = int(input("Idade: "))

if idade < 12:
    print("Infantil")
elif idade < 18:
    print("Juvenil")
elif idade < 60:
    print("Adulto")
else:
    print("Sênior")