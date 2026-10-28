
# pergunta o numero de volumes e converte str pra int
volume_processo = int(input("Digite o n de volumes do processo...\n"))

# pergunta sobre isencao ou se as custas ja foram recolhidas
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


