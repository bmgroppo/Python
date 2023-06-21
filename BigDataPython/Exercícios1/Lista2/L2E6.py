#Lista 2, Exercício 6
id=0
maior=0
cont=0

for cont in range (0,10):
    id=int(input(f"Digite a {cont+1}º de 10 idades: "))
    if (id>=18):
        maior=maior+1
print(f"De todas as idades, {maior} é(são) maior(es) de 18 anos.")