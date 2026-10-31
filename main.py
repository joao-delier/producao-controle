LIMITE_MINIMO_VOLUME = 1
LIMITE_MAXIMO_VOLUME = 100
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
    while volume_processo < LIMITE_MINIMO_VOLUME or volume_processo > LIMITE_MAXIMO_VOLUME:
        try:
            volume_processo = int(input("Digite o nº de volumes do processo...\n"))
        except ValueError: 
            print(f"O número de volumes tem que ser um número inteiro entre {LIMITE_MINIMO_VOLUME} e {LIMITE_MAXIMO_VOLUME}...")
        else:
            if volume_processo < LIMITE_MINIMO_VOLUME or volume_processo > LIMITE_MAXIMO_VOLUME:
                print(f"O número de volumes tem que ser um número inteiro entre {LIMITE_MINIMO_VOLUME} e {LIMITE_MAXIMO_VOLUME}...")
                
    
    resposta_valida_isencao = False
    
    while not resposta_valida_isencao: 
        isento_ou_recolhido = input("Processo possui isenção da parte perdedora ou custas já foram recolhidas? (s/n) ").lower()
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


