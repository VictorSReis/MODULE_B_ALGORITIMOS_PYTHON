# INFORMAÇÕES SOBRE SABORES E VALORES
# INDEX POSITION: 0-TR, 1-PR, 2-ES
SaboresSorvete_Tuple = ('TR', 'PR', 'ES')
QtdBolasSorvete_Disponiveis_Tuple = (1, 2, 3)
ValorBaseBolaSorvete = (6.00, 7.00, 8.00)


# SEGUNDO AS INFORMAÇÕES DO CADERNO DE QUESTÕES, OS VALORES REFERENTE
# AS BOLAS DE SORVETE QUANDO O USUÁRIO PEDIR 2 OU 3 É IGUAL A MULTIPLICAÇÃO
# DO VALOR DE UMA BOLA MENOS 1 REAL SE PEDIR 2 BOLAS E 3 REAIS SE PEDIR 3 BOLAS.
# UM TIPO DE DESCONTO PELO QUE VEMOS.


# FUNÇÕES AUXILIARES

def ApresentarCardapio():
    TextoColunas = '| N° BOLAS | Sabor Tradicional (tr) | Sabor Premium (pr) | Sabor Especial (es) |'
    TextoConteudo1 = '|    1     |         R$ 6,00        |       R$ 7,00      |       R$ 8,00       |'
    TextoConteudo2 = '|    2     |         R$ 11,00       |       R$ 13,00     |       R$ 15,00      |'
    TextoConteudo3 = '|    3     |         R$ 15,00       |       R$ 18,00     |       R$ 21,00      |'
    TextoHeader = '-' * 36 + 'Cardápio' + '-' * 36
    TextoFim = '-' * 80

    print(TextoHeader)
    print(TextoColunas)
    print(TextoConteudo1)
    print(TextoConteudo2)
    print(TextoConteudo3)
    print(TextoFim)


def ObterEntradaConsoleComoTexto(pMensagemShowInConsole):
    return input(pMensagemShowInConsole)


def ObterEntradaConsoleComoNumero(pMensagemShowInConsole):
    # VARIÁVEL A SER RETORNADA
    ValueInput = 0

    try:
        ValueInput = int(input(pMensagemShowInConsole))
    except ValueError:
        ValueInput = -1

    return ValueInput


def ValidarNomeSabor(pNomeSaborInput):
    Result = False

    # OBTÉM A VARIÁVEL GLOBAL QUE CONTEM OS SABORES.
    global SaboresSorvete_Tuple

    # CONVERTE A ENTRADA DO PARÂMETRO TODA PARA MAIÚSCULO.
    pNomeSaborInput = pNomeSaborInput.upper()

    # ABRE UM FOR PARA PROCURAR O SABOR NA TUPLE.
    # A VARIÁVEL 'Result' SÓ RECEBE O VALOR 'TRUE' SE O SABOR INFORMADO NO PARÂMETRO
    # FOR IGUAL A UM DOS 3 TIPOS
    for Sabor in SaboresSorvete_Tuple:
        if Sabor == pNomeSaborInput:
            # ENCONTROU . DEFINE 'TRUE' E QUEBRA O FOR
            Result = True
            break

    return Result


def ValidarQuantidadeBolas(pQtdInformada):
    Result = False

    # OBTÉM A VARIÁVEL GLOBAL QUE CONTEM AS QUANTIDADE DE BOLAS.
    global QtdBolasSorvete_Disponiveis_Tuple

    # ABRE UM FOR PARA PROCURAR A QUANTIDADE NA TUPLE.
    # A VARIÁVEL 'Result' SÓ RECEBE O VALOR 'TRUE' SE A QUANTIDADE INFORMADA NO PARÂMETRO
    # FOR IGUAL A UM DOS 3 TIPOS
    for QtdBolas in QtdBolasSorvete_Disponiveis_Tuple:
        if QtdBolas == pQtdInformada:
            # ENCONTROU . DEFINE 'TRUE' E QUEBRA O FOR
            Result = True
            break

    return Result


def CalcularValor(pTipoSorveteEscolhido, pQtdBolas):
    ValorEmReal = 0.00
    # COMO INFORMADO NA DOCUMENTAÇÃO DO PYTHON EM:
    # https://docs.python.org/pt-br/3/library/stdtypes.html?highlight=tuple#tuple TUPLAS IMPLEMENTAM FUNÇÕES COMUNS A
    # TIPOS SEQUENCIAS:
    # https://docs.python.org/pt-br/3/library/stdtypes.html?highlight=tuple#sequence-types-list-tuple-range
    # A OPERAÇÃO DE NOSSO INTERESSANTE É A: s.index(x[, i[, j]]) A OPERAÇÃO EM QUESTÃO NÓS RETORNA A
    # POSIÇÃO NA TUPLA DE UM DETERMINADO VALOR, COM ESSA POSIÇÃO PODEMOS OBTER OS VALORES NECESSÁRIOS PARA ESTÁ
    # FUNÇÃO DE FORMA RÁPIDA E PRÁTICA.

    # OBTÉM A VARIÁVEL GLOBAL QUE CONTEM OS TIPOS DE SORVETE
    # SERÁ UTILIZADA PARA DETERMINAR A POSIÇÃO DO VALOR A SER CALCULADO
    global SaboresSorvete_Tuple

    # OBTÉM A VARIÁVEL GLOBAL QUE CONTEM OS VALORES DE CADA BOLA
    global ValorBaseBolaSorvete

    IndexParaCalculo = SaboresSorvete_Tuple.index(pTipoSorveteEscolhido.upper())
    ValorBaseParaCalcularBola = ValorBaseBolaSorvete[IndexParaCalculo]

    # VERIFICA AGORA SE É APENAS UM BOLA.. SE FOR APENAS UMA O VALOR BASE ESTÁ CORRETO
    # E SÓ FALTAR MULTIPLICAR PELA QUANTIDADE DE BOLAS
    # CASO CONTRARIO, MULTIPLICAMOS E DEPOIS ABATEMOS UM TIPO DE DESCONTO.
    if pQtdBolas == 1:
        ValorEmReal = ValorBaseParaCalcularBola * pQtdBolas
    elif pQtdBolas == 2:
        ValorEmReal = (ValorBaseParaCalcularBola * pQtdBolas) - 1.00
    else:
        # 3 BOLAS
        ValorEmReal = (ValorBaseParaCalcularBola * pQtdBolas) - 3.00

    return ValorEmReal


def VerificarFinalizarPedido():
    FimPedido = False
    TextoFim = input('Deseja mais algum Sorvete? Digite s ou n: ').lower()
    if TextoFim == 's':
        FimPedido = False
    else:
        FimPedido = True
    return FimPedido


# MAIN PROGRAM
print('Bem-vindo a sorveteria de Victor Santos Reis :)')
ApresentarCardapio()

# VARIÁVEL QUE VAI CONTER O VALOR TOTAL DO PEDIDO
ValorTotal = 0.00

# ABRE UM WHILE PARA OBTER AS INFORMAÇÕES NECESSÁRIAS E FAZER O PEDIDO
while True:
    print()
    # OBTÉM O NOME DO SABOR DESEJADO
    NomeSaborSorvete = ObterEntradaConsoleComoTexto('Entre com o sabor do sorvete desejado(tr/pr/es): ')
    NomeValido = ValidarNomeSabor(NomeSaborSorvete)
    if not NomeValido:
        print('Sabor de Sorvete Inválido')
        continue

    # CHAMA O MÉTODO PARA OBTER A QUANTIDADE DE BOLAS DESEJADAS PELO CLIENTE
    # RETORNAR -1 SE O VALOR NÁO FOR NUMÉRICO
    QuantidadeBolas = ObterEntradaConsoleComoNumero("Entre com o número de bolas de sorvete desejado(1/2/3): ")
    QtdBolasValido = ValidarQuantidadeBolas(QuantidadeBolas)
    if not QtdBolasValido:
        print('Quantidade de Bolas de Sorvete Inválida')
        continue

    # CALCULA O VALOR DO PEDIDO E ADICIONA A VARIÁVEL 'ValorTotal' PARA SER EXIBIDA NO FINAL
    ValorTotal += CalcularValor(NomeSaborSorvete, QuantidadeBolas)

    # VERIFICA SE O CLIENTE QUER FINALIZAR O PEDIDO
    FinalizarPedido = VerificarFinalizarPedido()
    if FinalizarPedido:
        break
    else:
        # O CLIENTE AINDA NÃO FINALIZOU O PEDIDO
        continue

print()
print('Valor total do pedido: R$ {:.2f}'.format(ValorTotal))
