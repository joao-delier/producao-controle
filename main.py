def calcular_peso(volume, isencao):

    if(volume >= 4 and not isencao):
                peso = 2
                return peso
    else:
        peso = 1
        return peso

rodando = True
while rodando:
    volume_processo = 0
    while volume_processo <= 0 or volume_processo > 100:
        try:
            volume_processo = int(input("Digite o n de volumes do processo...\n"))
        except ValueError: 
            print("O numero de volumes tem que ser um numero inteiro entre 1 e 100...")
        else:
            if volume_processo <= 0 or volume_processo > 100:
                print("O numero de volumes tem que ser um numero inteiro entre 1 e 100...")
                
    
    resposta_valida_isencao = False
    
    while not resposta_valida_isencao: 
        isento_ou_recolhido = input("Processo possui insenção da parte perdedora ou custas ja foram recolhidas? (s/n) ").lower()
        if isento_ou_recolhido == "s":
            resposta_valida_isencao = True
            isento_ou_recolhido = True
        elif isento_ou_recolhido == "n":
            resposta_valida_isencao = True
            isento_ou_recolhido = False
        else:
             print("Entrada inválida. Por favor, digite 's' para sim ou 'n' para não.")
    
    peso_processo = calcular_peso(volume_processo, isento_ou_recolhido)
    
    print(f"O peso do processo: {peso_processo}")


    continuar = 0
    while continuar != 1 and continuar != 2:
        try:
            continuar = int(input("Pressione 1 para continuar ou 2 para sair..."))
        except ValueError:
            print("Entrada inválida. Por favor, digite 1 ou 2.")
    if continuar == 2:
        rodando = False


