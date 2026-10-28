
rodando = True
while rodando:
    volume_processo = 0
    while volume_processo == 0:
            try:
                volume_processo = int(input("Digite o n de volumes do processo...\n"))
            except: 
                print("O numero de volumes tem que ser um numero inteiro entre 1 e 100...")
                
    isento_ou_recolhido = input("Processo possui insencao da parte perdedora ou custas ja foram recolhidas? (y || n) ")
    peso_processo = 0

    #funcao de calculo de peso
    def calcular_peso(volume, isencao):
            peso = 0
            if(volume >= 4 and isencao != "y"):
                peso = 2
                return peso
            else:
                peso = 1
                return peso
            
    peso_processo = calcular_peso(volume_processo, isento_ou_recolhido)
    print(peso_processo)
    continuar = int(input("Pressione 1 para continuar ou 2 para sair..."))
if continuar == 2:
    rodando = False


