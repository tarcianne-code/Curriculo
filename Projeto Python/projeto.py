def amount_years(cap,rate,years):
     montante= cap* ( 1 + rate / 100  )**years 
     return montante 

def amount__months(cap,rate,months):
    Montante2 = cap*(1+(rate/100/12))**months
    return Montante2

choice =  input("Em quanto tempo -->")


if choice =="mês":
          cap = int(input('Insira o valor do capital --> '))
          rate = int(input('Informe a taxa de juros (em %) que você deseja --> '))
          months = int(input("Informe o tempo (em meses) --> "))
          Montante2 = amount__months(cap,rate,months)

          print(f'o montante após {months} foi de: {Montante2}')
          print('tabela de investimento em meses')
          print('-'*20)
          for v in range(1,months +  1 ):
                montante_mensal = amount__months(cap,rate,v)
                print(f'o invetimento no mês{v} foi:R${montante_mensal:.2f}') 


elif choice =="anos": 
          cap = float(input('Insira o valor do capital --> '))
          rate = float(input('Inoforme a taxa de juros (em %) que você deseja --> '))
          years = int(input("Informe o tempo (em anos) --> "))
          Montante = amount_years(cap,rate,years)

          print(f'o montante após {years} anos --> {Montante}') 
          print(f'O montante após {years} meses foi de: {amount_years}')
          print('Tabela de investimento por ano')
          print('-' * 20)
          for v in range(1, years  + 1):
             montante_anual = amount_years(cap, rate, (years - 1) * 12 + v)
             print(f'O investimento do ano {v} foi: R${montante_anual:.2f}')
          
else:
     print('opção invalida')

