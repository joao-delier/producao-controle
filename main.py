import csv
from calcular_peso import calcular_peso, LIMITE_MINIMO_VOLUME, LIMITE_MAXIMO_VOLUME



total_processos = 0
soma_pesos = 0
erros_processo = 0


with open('dados/dados.csv', mode='r', encoding='utf-8') as file:
    file_csv = csv.reader(file, delimiter=',')
    next(file_csv)  # pra pular o cabeçalho

    for numero_linha, linha in enumerate(file_csv, start=2):  # start=2 para começar a contagem a partir da segunda linha
        if len(linha) == 0 :
            continue
        if len(linha) != 3:
            print(f"Erro no formato da linha: {linha}. Esperado 3 colunas, mas encontrou {len(linha)}. Essa linha será ignorado.")
            continue

        numero_processo, volume, isencao = linha
        isencao_processo = isencao.strip().lower()
        
        try:
            volume_processo = int(volume)
            if volume_processo > LIMITE_MAXIMO_VOLUME or volume_processo < LIMITE_MINIMO_VOLUME:
                print(f"Volume do processo {numero_processo} fora do limite permitido. Esse processo será ignorado.")
                erros_processo += 1
                continue
        except ValueError:
            print(f"Erro ao converter o valor '{volume}' para inteiro do processo {numero_processo}. Esse processo será ignorado.")
            erros_processo += 1
            continue

        if isencao_processo == 's':
            isencao_processo = True
        elif isencao_processo == 'n':
            isencao_processo = False
        else:
            print(f"Erro ao interpretar a isenção do processo {numero_processo}. Use ('s'/'n') esse processo será ignorado.")
            erros_processo += 1
            continue

        peso = calcular_peso(volume_processo, isencao_processo)
        soma_pesos += peso

        print(f"nº do processo: {numero_processo} | nº de volumes: {volume_processo} | isenção: {isencao_processo} | peso: {peso}")
        total_processos += 1

print(f"Total de processos: {total_processos}")
print(f"Soma dos pesos: {soma_pesos}")
print(f"Total de processos com erro: {erros_processo}")


