# Controle de Produção

Sistema em Python que automatiza o controle mensal de processos trabalhados em um setor da área jurídica: calcula o peso de cada processo segundo regras internas, valida os dados e gera relatórios prontos.

> **EN:** A Python tool that automates monthly tracking of legal case processing work: it applies business rules, validates data and generates reports. Built as a learning-in-public project.

## O problema

Em muitos setores, a produção do mês ainda é controlada à mão, com planilhas e anotações. Cada processo trabalhado tem um **peso**, a unidade usada para medir produtividade (processos maiores contam mais), e esse cálculo é feito manualmente, o que gasta tempo e gera erros.

**Regras de peso:**

| Situação | Peso |
|---|---|
| Até 3 volumes | 1 |
| 4 volumes ou mais | 2 |
| Devedor isento ou custas já recolhidas | 1 (independente dos volumes) |

## O que o sistema faz

- recebe a lista de processos em formato csv;
- aplica as regras de peso automaticamente;
- valida os dados, como volume mínimo e máximo, status de isenção atual do processo;
- gera o relatório.

## Como rodar

**Pré-requisito:** Python 3 instalado.

```bash
git clone https://github.com/joao-delier/producao-controle.git
cd producao-controle
```

**Exemplo de uso:**

### MODO ARQUIVO CSV
Lê diretamente de um arquivo csv, e calcula o peso de cada processo.

```bash
python main.py
```

o csv deve ser 3 colunas no formato:
processo(text), volume(int), isenção(text)

exemplo:
```text
0000001-00.2026.8.00.0001,5,n
0000002-00.2026.8.00.0001,6,s
```
Saída:

```
nº do processo: 0000001-00.2026.8.00.0001 | nº de volumes: 5 | isenção: False | peso: 2
nº do processo: 0000002-00.2026.8.00.0001 | nº de volumes: 6 | isenção: True | peso: 1
```


### MODO INTERATIVO

Recebe volume e status de isenção de um processo e devolve o peso calculado.

exemplo:

```bash
python calcular_peso.py
```

```text
Digite o nº de volumes do processo...
5
Processo possui isenção da parte perdedora ou custas já foram recolhidas? (s/n) n
O peso do processo: 2
Pressione 1 para continuar ou 2 para sair...2
```
## Tecnologias

- Python
- Git

## Etapas

- [x] Ambiente e repositório
- [x] Calculadora de peso no terminal
- [x] Leitura de vários processos a partir de um arquivo CSV
- [ ] Validação de dados e testes automatizados
- [ ] Relatório mensal em Excel
- [ ] Banco de dados (SQLite)
- [ ] Interface web
- [ ] Publicação online

## Como este projeto foi feito

Este é um projeto de aprendizado em público, desenvolvido no formato de um emprego simulado: uma IA (Claude) faz o papel de tech lead, passa as tarefas com critérios de aceite e revisa o código depois de cada entrega.

**Todo o código é escrito por mim.** A IA não entrega soluções prontas: ela indica o que pesquisar, revisa o que eu fiz e tira dúvidas depois que eu já tentei resolver.

Todos os dados usados no repositório são fictícios.
