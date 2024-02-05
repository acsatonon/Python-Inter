# a = 1
# print(a)

# def teste():
#     a = 2
#     print(a)

# teste()
# print(a)



# def converter_para_inteiro(numero):
#     return int(numero)

# num = input('num:')
# print(converter_para_inteiro(num))



# def soma(a,b,c,d):
#     return a+b+c+d

# e = int(input('num:'))
# f = int(input('num:'))
# g = int(input('num:'))
# h = int(input('num:'))
# print(soma(e,f,g,h))



# print('Olá Mundo')
# print('Olá', 'Mundo', end=' ', sep='...')
# print('Bom dia')

# def funcao(a,b=5):
#      return f'{a} {b}'
 
# print(funcao(9))



# def imprima(a):
#     return int(a)

# num= input('::')
# print(imprima(num))



# def impar_ou_par(num):
#     return num%2==0

# numero = int(input('num:'))
# print(impar_ou_par(numero))



# def maior_menor (a,b):
#     if a>b:
#         return 'A maior'
#     else:
#         return 'B maior'

# numero = float(input('num:'))
# numero2= float(input('num2:'))
# print(maior_menor(numero, numero2))



# def remove_vogal (frase):
#     sem_vogal = ''
#     vogais = 'aeiou'
#     for letra in frase:
#         if letra not in vogais:
#             sem_vogal += letra
#     return sem_vogal

# a= input('Digite:')
# print(remove_vogal(a))

# def remove_vogal (frase):
#     sem_vogal = ''
#     vogais = 'aeiou'
#     for letra in frase:
#         if letra in vogais:
#             sem_vogal += letra
#     return sem_vogal

# a= input('Digite:')
# print(remove_vogal(a))



def verifica_palindromo(frase):
    if frase== frase [::-1]:
        return 'é um palindromo'
    return 'não é um palindromo'