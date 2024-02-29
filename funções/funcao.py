# > FUNÇÕES

# 1. O que são funções e por que utilizá-las?

# Funções que ja utilizamos anteriomente...
"""
print() # - Imprimir uma mensagem(int, float, str) no console (terminal, cmd)
input() # - Retonar um dado informado pelo usuário (entrada padrão) e pode receber uma string
len() # - Recebe uma lista e retorna o tamanho o dessa lista
max() # - Retorna o maior valor de uma lista
"""
# 2. Criação de Funções 

# Função inicial

def saudacao():
    print('Seja bem-vinda(o)!')
    print('Ola, é um prazer ter você fazendo parte desse curso!')

saudacao()



# Função com parâmetros

def saudacao(nome, Curso='Python'):
    print(f'Seja bem-vinda(o),{nome}!')
    print(f'Ola, é um prazer ter você fazendo parte do curso de {Curso}!')

saudacao('Anderson')



def soma(num1, mum2):
    return num1 + mum2

resultado = soma(5, 7)


print('o Resultado da soma é', resultado)



def calculadora(num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '_':
        return num1 - num2
    
resultado = calculadora(10, 20)

print(resultado)