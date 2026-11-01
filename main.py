import csv
from calcular_peso import calcular_peso, LIMITE_MINIMO_VOLUME, LIMITE_MAXIMO_VOLUME



total_processos = 0
soma_pesos = 0

processo_atual = ['', '', '']
with open('dados/dados.csv', mode='r', encoding='utf-8') as file:
    file_csv = csv.reader(file, delimiter=',')
    next(file_csv)  # pra pular o cabeçalho

    for numero_processo, volume, isencao in file_csv:
        processo_atual[0] = numero_processo
        try:
            processo_atual[1] = int(volume)
        except ValueError:
            print(f"Erro ao converter o valor '{volume}' para inteiro do processo {numero_processo}. Esse processo será ignorado.")
            continue
        
        processo_atual[2] = (isencao)
        resposta_isencao = isencao.lower().strip()
        if resposta_isencao == 's':
           processo_atual[2] = True
        elif resposta_isencao == 'n':
            processo_atual[2] = False
        else:
            print(f"Erro ao interpretar a isenção do processo {numero_processo}. Use ('s'/'n') esse processo sera ignorado.")
            processo_atual[2] = False  # 
            continue

        peso = calcular_peso(processo_atual[1], processo_atual[2])
        soma_pesos += peso

        print(f"nº do processo: {processo_atual[0]} | nº de volumes: {processo_atual[1]} | isenção: {processo_atual[2]} | peso: {peso}")
        total_processos += 1

print(f"Total de processos: {total_processos}")
print(f"Soma dos pesos: {soma_pesos}")



