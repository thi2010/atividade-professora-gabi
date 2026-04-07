p = int(input())
d = int(input())
b = int(input())

pontos_p = p
pontos_d = d * 2
pontos_b = b * 3

total = pontos_p + pontos_d + pontos_b

if total >= 150:
    premio = "B"
else:
    premio = "N"
    if total >= 100:
        premio = "P"
    if total >= 120:
        premio = "D"

print(premio)