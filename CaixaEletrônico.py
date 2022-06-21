#Funções
def remover_Cedulas(valor,cedula):
    valor -= cedula
    return valor

def imprimir_quant(quant,cedula):
    if quant == 0:
        return False #Retorna falso porque não entregou cédulas
    else:
        print("%d nota(s) de R$%d,00" % (quant,cedula))

#Programa principal
saque = int(input("Digite o valor que deseja sacar: "))
#Cédulas
c1 = 100
c2 = 50
c3 = 20
c4 = 10
cn = c1
cr = c2
#quantidade de notas
quantc1 = 0
quantc2 = 0
quantc3 = 0
quantc4 = 0
#Salvar valor de saque para não ser perdido
saq = saque
#Condição de saque
if saque%c4!=0 or saque==0:
    print("Não é possível retirar esse valor.")
else:
    while True:
        if saque < cn:
            while cn > saque:
                cn = cr
                cr = c3
                if cn == c3:
                    cr = c4
        #Remove cedulas do valor do saque para contagem
        saque = remover_Cedulas(saque,cn)
        #Contagem de notas
        if cn == 100:
            quantc1 +=1
        elif cn==50:
            quantc2 +=1
        elif cn==20:
            quantc3 +=1
        else:
            quantc4 +=1
        #Condição de saida do programa    
        if saque == 0: break
        
    #Exibir quantidade de cedulas retiradas
    print("Valor de Saque: R$%d,00" % saq)
    print("Entregar: ")
    imprimir_quant(quantc1,c1)
    imprimir_quant(quantc2,c2)
    imprimir_quant(quantc3,c3)
    imprimir_quant(quantc4,c4)

print("Fim do programa")
        
    
