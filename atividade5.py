def calculadora():
    try:
        num1= float(input('Digite um número: '))
        num2= float(input('Digite outro número: '))
        operacao= input('tipo da operação(+,-,/,*): ')
   
        if operacao=='+':
                resultado= num1 + num2
        elif operacao=='-':
                resultado= num1 - num2
        elif operacao=='*':
                resultado= num1 * num2
        elif operacao=='/':
                resultado= num1 / num2
        else:
            return 'Operação inválida'
        
        return f'Resultado: {resultado}'

    except ValueError: 
        print('Por favor, insira números válidos')
        
    except ZeroDivisionError:
        print('Erro: Divisão por zero não é permitida!')
        
    finally:
        print('Tudo certo!')
        
calculadora()