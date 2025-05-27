def limpar_numero(numero_cartao):
    """Remove espaços e hífens do número do cartão."""
    return str(numero_cartao).replace(" ", "").replace("-", "")


def validar_luhn(numero_cartao):
    """Valida o número do cartão usando o Algoritmo de Luhn."""
    numero = limpar_numero(numero_cartao)
    soma = 0
    alternar = False
    for digito in reversed(numero):
        d = int(digito)
        if alternar:
            d *= 2
            if d > 9:
                d -= 9
        soma += d
        alternar = not alternar
    return soma % 10 == 0


def identificar_bandeira(numero_cartao):
    """
    Identifica a bandeira do cartão de crédito a partir do número informado.
    Parâmetro:
        numero_cartao (str): Número do cartão de crédito.
    Retorna:
        str: Nome da bandeira ou mensagem de erro.
    """
    numero = limpar_numero(numero_cartao)
    if not numero.isdigit():
        return "Número inválido: contém caracteres não numéricos"
    if not (13 <= len(numero) <= 19):
        return "Número inválido: tamanho incorreto"
    if not validar_luhn(numero):
        return "Número inválido: falha na validação de Luhn"

    try:
        if numero.startswith("4"):
            return "Visa"
        elif numero[:2] in ["51", "52", "53", "54", "55"] or (
            len(numero) >= 4 and 2221 <= int(numero[:4]) <= 2720
        ):
            return "MasterCard"
        elif numero.startswith("34") or numero.startswith("37"):
            return "American Express"
        elif (
            numero.startswith("6011")
            or numero.startswith("65")
            or (len(numero) >= 3 and 644 <= int(numero[:3]) <= 649)
        ):
            return "Discover"
        elif numero.startswith("35"):
            return "JCB"
        elif numero.startswith(("36", "38", "39")):
            return "Diners Club"
        # Elo
        elif numero.startswith(
            (
                "4011",
                "4312",
                "4389",
                "4514",
                "4576",
                "5041",
                "5066",
                "5067",
                "509",
                "6277",
                "6362",
                "6363",
                "650",
                "6516",
                "6550",
            )
        ):
            return "Elo"
        # Hipercard
        elif numero.startswith("606282") or numero.startswith("3841"):
            return "Hipercard"
        # Maestro
        elif numero.startswith(
            (
                "5018",
                "5020",
                "5038",
                "5612",
                "5893",
                "6304",
                "6759",
                "6761",
                "6762",
                "6763",
            )
        ) or numero[:2] in ["50", "56", "57", "58", "63", "67"]:
            return "Maestro"
        else:
            return "Bandeira desconhecida"
    except ValueError:
        return "Número inválido"


if __name__ == "__main__":
    numero = input("Digite o número do cartão de crédito: ")
    bandeira = identificar_bandeira(numero)
    print(f"Bandeira identificada: {bandeira}")
