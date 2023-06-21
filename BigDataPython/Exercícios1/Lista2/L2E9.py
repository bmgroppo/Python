#Lista 2, Exercício 9
cont=0

while True:
    n=float(input('Digite um número: '))

    if (n%2==0):
        cont+=1

    if (n%11==0):
        break
    
print(f" Dos valores digitados {cont} são pares")