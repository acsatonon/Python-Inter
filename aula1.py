linha= input()
x=linha.split(" ")  # ['3', '2']

opcao = int(x[0])
quantidade = int(x[1])

if opcao == 1:
    lanche= 4.0 * quantidade
elif opcao == 2:
    lanche= 4,