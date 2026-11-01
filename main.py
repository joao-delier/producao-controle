import csv
from calcular_peso import calcular_peso, LIMITE_MINIMO_VOLUME, LIMITE_MAXIMO_VOLUME


total_processos = 0
soma_pesos = 0

processo_atual = ['', '', '']
with open('dados/dados.csv', mode='r') as file:
    file_csv = csv.reader(file, delimiter=',')
    next(file_csv)  # pra pular o cabeçalho

    for row in file_csv:
        processo_atual[0] = row[0]
        try:
            processo_atual[1] = int(row[1])
        except ValueError:
            print(f"Erro ao converter o valor '{row[1]}' para inteiro do processo {row[0]}. O valor será definido como 0.")
            processo_atual[1] = 0  # 
            continue
        processo_atual[2] = (row[2])
        if row[2].lower().strip() == 's':
           processo_atual[2] = True
        elif row[2].lower().strip() == 'n':
            processo_atual[2] = False

        peso = calcular_peso(processo_atual[1], processo_atual[2])
        soma_pesos += peso

        print(f"nº do processo: {processo_atual[0]} | nº de volumes: {processo_atual[1]} | isenção: {processo_atual[2]} | peso: {peso}")
        total_processos += 1

print(f"Total de processos: {total_processos}")
print(f"Soma dos pesos: {soma_pesos}")

#for i in processo_atual:
   # print(f"nº do processo: {i[0]} | nº de volumes: {i[1]} | isenção: {i[2]}")


