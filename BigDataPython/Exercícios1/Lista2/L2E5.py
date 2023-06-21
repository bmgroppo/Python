#Lista 2, Exercício 5

num=0
imp=0
cont=0

for cont in range (0,5):
    num=int(input(f"Digite o {cont+1}º de 5 valores: "))
    if (num%2!=0):
        imp=imp+1
print(f"A quantidade de números impares é {imp}")