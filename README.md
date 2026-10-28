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

- recebe a lista de processos trabalhados no mês;
- aplica as regras de peso automaticamente;
- valida os dados, como o formato do número do processo;
- gera o relatório mensal.

## Como rodar

Em construção. As instruções entram aqui com a primeira versão funcional.

## Tecnologias

- Python
- Git

## Etapas

- [ ] Ambiente e repositório
- [ ] Calculadora de peso no terminal
- [ ] Leitura de vários processos a partir de um arquivo CSV
- [ ] Validação de dados e testes automatizados
- [ ] Relatório mensal em Excel
- [ ] Banco de dados (SQLite)
- [ ] Interface web
- [ ] Publicação online

## Como este projeto foi feito

Este é um projeto de aprendizado em público, desenvolvido no formato de um emprego simulado: uma IA (Claude) faz o papel de tech lead, passa as tarefas com critérios de aceite e revisa o código depois de cada entrega.

**Todo o código é escrito por mim.** A IA não entrega soluções prontas: ela indica o que pesquisar, revisa o que eu fiz e tira dúvidas depois que eu já tentei resolver.

Todos os dados usados no repositório são fictícios.
