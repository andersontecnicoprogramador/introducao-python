# ESTRUTURAS CONDICIONAIS 

idade = 10

if idade >= 18:
    print('Você é maior de idade. ')
else:
    print('Você é menor de idade.')

"""
imagine que você querira imprimir "Aprovada(o)", ocaso o estudante tenha uma média
 superior ou igual a 7, e "Reprovado", caso a média seja inferior a 7.


media = float(input('Informe a média do estudante:  '))

if media >= 7:
    print('Você foi aprovada(o)!')
elif media >= 5:
    print('Recuperação')
else:
    print('Você foi reprovada(o).')
   
 """

media = 5
presenca = 50

if media >= 7 and presenca >= 70:
    print('Aprovado!')
else:
    print('Reprovado')