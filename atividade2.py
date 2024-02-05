# linha= input()
# x=linha.split(" ")  # ['3', '2']

# A = int(x[0])
# B = int(x[1])

# if A%B==0:
#     print('Sao Multiplos')
# elif B%A==0:
#     print('Sao multiplos')
# else:
#     print('Nao sao Multiplos')
    
    
    
    
# def bhaskara(a,b,c):
#     a = float(a)
#     b = float(b)
#     c = float(c)
    
#     delta = (b**2) - (4*a*c)
    
#     if delta < 0 or a == 0:
#         return 'Impossivel calcular'
    
#     x1 = (((-1)*b) + (delta**0.5))/(2*a)
#     x2 = (((-1)*b) - (delta**0.5))/(2*a)
    
#     return [x1, x2]


# linha= input()
# a,b,c=linha.split(" ")
# x = bhaskara(a,b,c)

# if x != 'Impossivel calcular':
#     print(f'R1 = {x[0]}')
#     print(f'R2 = {x[1]}')
# else:
#     print('Impossivel calcular')




# N = int(input())
# contador= 1

# while contador < 10000:
#     if contador%N==2:
#         print(contador)

#     contador+= 1



# def convert(seconds): 
#     seconds = seconds % (24 * 3600) 
#     hour = seconds // 3600
#     seconds %= 3600
#     minutes = seconds // 60
#     seconds %= 60
      
#     return "%d:%02d:%02d" % (hour, minutes, seconds)
      
# N = int(input())
# print(convert(N)) 



# linha= input()
# x=linha.split(" ")  # ['3', '2']

# inicio = int(x[0])
# final = int(x[1])

# if inicio > final:
#     jogo = 24 - inicio + final
#     print(f'O JOGO DUROU {jogo} HORA(S)')

# elif inicio == final: 
#     print('O JOGO DUROU 24 HORA(S)')
    
# else:
#     jogo = final - inicio
#     print(f'O JOGO DUROU {jogo} HORA(S)')


MAIOR_VALOR = 0

FOR I IN RANGE(100):
    VALOR = INT(INPUT())
    
    if valor > MAIOR_VALOR:
        MAIOR_VALOR = valor
