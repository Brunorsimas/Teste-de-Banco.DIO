
# Identificador de Bandeira de Cartão de Crédito

Este projeto é uma aplicação simples desenvolvida em Python, capaz de identificar a bandeira com base no número do cartão. Além disso, valida se o número informado é um cartão válido através do Algoritmo de Luhn.

## 🚀 Funcionalidades

- ✅ Validação do número do cartão usando o **Algoritmo de Luhn**.
- ✅ Identificação da bandeira do cartão:
  - Visa
  - MasterCard
  - American Express
  - Discover
  - JCB
  - Diners Club
  - Elo
  - Hipercard
  - Maestro
  - Entre outros (ou retorna "Bandeira desconhecida").

## 🧠 Como funciona

O programa faz:

1. Limpeza do número (remove espaços e hífens).
2. Validação através do **Algoritmo de Luhn**, que detecta se o número do cartão é matematicamente válido.
3. Verificação dos padrões de prefixos dos cartões para determinar a bandeira correspondente.

## 🛠️ Tecnologias

- Linguagem: **Python 3**

## 💻 Como executar

1. Clone o repositório:

```bash
git clone [https://github.com/Brunorsimas/Teste-de-Banco.DIO.git]
```

2. Acesse o diretório do projeto:

```bash
cd seu-repositorio
```

3. Execute o script:

```bash
python teste_Banco.py
```

4. Insira o número do cartão (com ou sem espaços/hífens).  
O programa irá informar se o número é válido e a bandeira correspondente.

## 🔧 Exemplo de uso

```bash
Digite o número do cartão de crédito: 4111 1111 1111 1111
Bandeira identificada: Visa
```

```bash
Digite o número do cartão de crédito: 5105-1051-0510-5100
Bandeira identificada: MasterCard
```

## ⚠️ Observações importantes

- Este projeto é de caráter **educacional e experimental**.
- Não armazena, processa ou transmite dados reais de cartões.
- Não utilize números reais de cartões.

## 🤝 Contribuição

Contribuições são bem-vindas!  
Sinta-se livre para abrir issues, pull requests ou sugestões.
