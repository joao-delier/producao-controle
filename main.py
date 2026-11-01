from calcular_peso import calcular_peso, LIMITE_MINIMO_VOLUME, LIMITE_MAXIMO_VOLUME

import csv

with open('dados/dados.csv', mode='r') as file:
    file_csv = csv.reader(file, delimiter=',')
    for row in file_csv:
       print(row)


