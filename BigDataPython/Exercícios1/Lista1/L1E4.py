#Lista 1, exercício 4
i = int(input('Informe a Idade do nadador: '))
c = ''

if i < 5 or i > 99:
    c = 'Inválida.' 
elif i >= 5 and i < 8:
    c = 'Infantil A.'
elif i >= 8 and i < 11:
    c = 'Infantil B.'
elif i >= 11 and i < 14:
    c = 'Juvenil A.'
elif i >= 14 and i < 18:
    c = 'Juvenil B.'
else:
    c = 'Adulto.'
    
print(f'Idade na Categoria: {c}')