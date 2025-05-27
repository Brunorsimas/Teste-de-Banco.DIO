# Teste-de-Banco.DIO
Identificador de Bandeira de Cartão de Crédito
Um programa Python simples que identifica a bandeira de um cartão de crédito (Visa, MasterCard, etc.) com base no número do cartão, incluindo validação pelo algoritmo de Luhn.

Funcionalidades
Valida o número do cartão usando o algoritmo de Luhn

Identifica a bandeira do cartão com base nos prefixos conhecidos

Suporta as principais bandeiras:

Visa

MasterCard

American Express

Discover

JCB

Diners Club

Elo

Hipercard

Maestro

Como usar
Clone o repositório ou copie o código identificador_bandeira.py

Execute o script Python:

bash
python identificador_bandeira.py
Digite o número do cartão quando solicitado

O programa exibirá a bandeira identificada ou mensagem de erro se o número for inválido

Requisitos
Python 3.x

Exemplo de uso
bash
Digite o número do cartão de crédito: 4111 1111 1111 1111
Bandeira identificada: Visa
Validações realizadas
Remove espaços e hífens do número do cartão

Verifica se contém apenas dígitos numéricos

Verifica se o tamanho está entre 13 e 19 dígitos

Aplica o algoritmo de Luhn para validação

Identifica a bandeira com base nos prefixos conhecidos
