#código da tabuada das 4 operações com funções

def somar(numero):
    for i in range(1,11):
        print(f'{i}+{numero}={i+numero}')
        
def subtrair(numero):
    for i in range(1,11):
        print(f'{i}-{numero}={i-numero}')
        
def multiplicar(numero):
    for i in range(1,11):
        print(f'{i}*{numero}={i*numero}')
        
def dividir(numero):
    for i in range(1,11):
        print(f'{i}/{numero}={i/numero}')
        
operação = int(input('Digite a operação a ser realizada: \n 1-soma 2-subtração 3-multiplicação 4-ivisão 5-todas'))
numero = int(input('Digite um número a ser gerada a operação'))

if (operação == 1):
    print('soma:')
    somar(numero)
    
elif (operação == 2):
    print('subtrair:')
    subtrair(numero)
    
elif (operação == 3):
    print('multiplicar:')
    multiplicar(numero)
    
elif (operação == 4):
    print('dividir:')
    dividir(numero)
    
elif (operação == 5):
    print('soma:')
    somar(numero)
    print('subtrair:')
    subtrair(numero)
    print('multiplicar:')
    multiplicar(numero)
    print('dividir:')
    dividir(numero)
    
else:
    print('Erro!')
    
#THe end.