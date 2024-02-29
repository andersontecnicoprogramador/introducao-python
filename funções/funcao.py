# > FUNÇÕES

# 1. O que são funções e por que utilizá-las?

# Funções que já utilizamos anteriormente...
"""
print() # - Imprimi uma mensagem(int, float, str) no console (terminal, cmd)
input() # - Retorna um dado informado pelo usuario (entrada padrão) e pode receber uma string
len() # - Recebe uma lista e retorna o tamanho dessa lista
max() # - Retorna o maior valor de uma lista
"""
# 2. Criação de Funções

# Função inicial
"""
def saudacao():
    print('Seja bem-vindo(a)')
    print('Olá, é um prazer ter você fazendo parte desse curso!')

saudacao()
saudacao()
saudacao()
"""
# Função com parâmetros

def saudacao(nome,curso):
    print(f'Seja bem-vindo(a), {nome}')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Anderson','Python')


# Função com parâmetros defult

def saudacao(nome,curso='Python'):
    print(f'Seja bem-vindo(a), {nome}')
    print(f'Olá, é um prazer ter você fazendo parte do curso de {curso}!')

saudacao('Anderson', 'C++')

# Funções com retorno

def soma(num1,  num2):
    return num1 + num2

resultado = soma(5, 7)

print('O resultado da soma é', resultado)







def calculadora (num1, num2, operacao='+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '_':
        return num1 - num2
    
resultado = calculadora(10, 20,'_' )

print(resultado)
