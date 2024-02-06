from idade import idade
nome= input('Nome:')
dia_nascimento= int(input('Dia de Nascimento:'))
mes_nascimento= int(input('Mês de Nascimento:'))
ano_nascimento= int(input('Ano de Nascimento:'))

print(f'{nome} : {idade(dia_nascimento,mes_nascimento,ano_nascimento)}')
