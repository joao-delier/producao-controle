from calcular_peso import calcular_peso, LIMITE_MINIMO_VOLUME, LIMITE_MAXIMO_VOLUME

import csv
total_processos = 0
processo_atual = ['', '', '']
with open('dados/dados.csv', mode='r') as file:
    file_csv = csv.reader(file, delimiter=',')
    next(file_csv)  # pra pular o cabeçalho

    for row in file_csv:
       processo_atual[0] = row[0]
       processo_atual[1] = int(row[1])
       processo_atual[2] = row[2]
       peso = calcular_peso(processo_atual[1], processo_atual[2])

       print(f"nº do processo: {processo_atual[0]} | nº de volumes: {processo_atual[1]} | isenção: {processo_atual[2]} | peso: {peso}")
       total_processos += 1


#for i in processo_atual:
   # print(f"nº do processo: {i[0]} | nº de volumes: {i[1]} | isenção: {i[2]}")


