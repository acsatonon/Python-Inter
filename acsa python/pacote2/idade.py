from datetime import datetime
ano = datetime.today().year
mes = datetime.today().month
dia = datetime.today().day

def idade(dia_nascimento,mes_nascimento,ano_nascimento):
    
    if mes == mes_nascimento:
        return ano - ano_nascimento 
    elif mes < mes_nascimento:
        if dia <= dia_nascimento:
            return ano - ano_nascimento - 1
    else:
     return ano - ano_nascimento
    