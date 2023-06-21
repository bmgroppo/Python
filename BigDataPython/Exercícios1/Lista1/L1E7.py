#Lista 1, exercício 7

cod = int(input('Código do cargo: '))
s = float(input('Salário: R$'))
c = ''
aj = 0

if cod == 1:
    c = 'Escrituário'
    aj = 0.5
    
elif cod == 2:
    c = 'Secretário'
    aj = 0.35
      
elif cod == 3:
    c = 'Caixa'
    aj = 0.2
    
elif cod == 4:
    c = 'Gerente'
    aj = 0.1
    
elif cod == 5:
    c = 'Diretor'
    aj = 0
    
print(f'Cargo: {c}; Aumento: R${round(s*aj, 2)}; Novo salário: R${round(s+(s*aj), 2)}')