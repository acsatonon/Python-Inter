from pessoa import calcular_idade
nome= input('Nome:')
ano_nascimento= int(input('Ano de Nascimento:'))
ano_hoje= int(input('Ano Atual:'))

print(f'{nome} : {calcular_idade(ano_nascimento, ano_hoje)}')
