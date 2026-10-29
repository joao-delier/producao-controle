def calcular_peso(volume, isencao):
    peso = 0
    if(volume >= 4 and not isencao):
                peso = 2
                return peso
    else:
        peso = 1
        return peso

rodando = True
while rodando:
    volume_processo = 0
    while volume_processo <= 0:
            try:
                volume_processo = int(input("Digite o n de volumes do processo...\n"))
            except ValueError: 
                print("O numero de volumes tem que ser um numero inteiro entre 1 e 100...")
    
    processo_simples = True
    while processo_simples: 
        isento_ou_recolhido = input("Processo possui insencao da parte perdedora ou custas ja foram recolhidas? (y Y ||n N) ").lower()
        if isento_ou_recolhido == "y":
            processo_simples = False
            isento_ou_recolhido = True
        elif isento_ou_recolhido == "n":
            processo_simples = False
            isento_ou_recolhido = False
        else:
             processo_simples = True
    
        
    peso_processo = 0
    peso_processo = calcular_peso(volume_processo, isento_ou_recolhido)
    print(peso_processo)

    continuar = int(input("Pressione 1 para continuar ou 2 para sair..."))
    if continuar == 2:
        rodando = False


