from calcular_peso import calcular_peso, LIMITE_MINIMO_VOLUME, LIMITE_MAXIMO_VOLUME

import csv

with open('dados.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        numero_processo = row[0]
        volume_processo = int(row[1])
        isencao = row[2].lower()

print(f"Numero do processo: {numero_processo} - Volume: {volume_processo} - Isenção: {isencao}")