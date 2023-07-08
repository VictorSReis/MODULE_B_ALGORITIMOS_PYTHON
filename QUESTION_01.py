# FUNCÕES AUXILIARES.

def ObterEntradaConsoleComoNumero(pMensagemShowInConsole):
    return int(input(pMensagemShowInConsole))


def ObterPercentualDescontoSobreQuantidadeProdutos(pQuantidadeProdutos):
    # DESCONTOS A SEREM VERIFICADOS:
    #  QUANTIDADE DE PRODUTO < 200 = 0%
    #  QUANTIDADE DE PRODUTO >= 200 & < 1000 = 5%
    #  QUANTIDADE DE PRODUTO >= 1000 & < 2000 = 10%
    #  QUANTIDADE DE PRODUTO >= 2000 = 15%

    # VARIÁVEL QUE CONTEM O PERCENTUAL DE DESCONTO PARA O PRODUTO
    ValorDesconto = 0

    if pQuantidadeProdutos < 200:
        ValorDesconto = 0

    elif pQuantidadeProdutos >= 200 and pQuantidadeProdutos < 1000:
        ValorDesconto = 5

    elif pQuantidadeProdutos >= 1000 and pQuantidadeProdutos < 2000:
        ValorDesconto = 10

    else:
        # COMO CHEGOU AQUI, O VALOR DA QUANTIDADE DE PRODUTOS SÓ PODE SER MAIOR OU IGUAL A 2000.
        ValorDesconto = 15

    # RETORNA O RESULTADO COM O PERCENTUAL QUE DEVE SER UTILIZADA PARA CALCULAR O DESCONTO FINAL.
    return ValorDesconto


def CalcularDescontoFinal(pQuantidadeProdutos, pValorUnitario, pPercentualDesconto=0):
    ValorProdutoSemDesconto = pQuantidadeProdutos * pValorUnitario
    if pPercentualDesconto == 0:
        return ValorProdutoSemDesconto
    else:

        return ValorProdutoSemDesconto - ((pQuantidadeProdutos * pValorUnitario) / 100) * pPercentualDesconto


# MAIN PROGRAM START

print('Bem vindo a Loja de Software de Victor Santos Reis :)')
ValorUnitario = ObterEntradaConsoleComoNumero('Entre com o valor unitário do produto: ')
QuantidadeProdutos = 0

# OBRIGADO O VALOR UNITÁRIO SER MAIOR QUE 200
# ABRE UM WHILE ATÉ CONSEGUIR UM VALOR VÁLIDO
while True:
    # OBTÉM A QUANTIDADE DE PRODUTOS
    QuantidadeProdutos = ObterEntradaConsoleComoNumero('Entre com a quantidade de produtos: ')

    # VERIFICA SE A QUANTIDADE NÃO É MENOR DO QUE O SOLICITADO PELA ATIVIDADE PRATICA.
    if QuantidadeProdutos <= 200:
        print('Favor informar uma quantidade que seja maior que 200!')
        continue
    else:
        break

PercentualDesconto = ObterPercentualDescontoSobreQuantidadeProdutos(QuantidadeProdutos)
ValorFinalComDesconto = CalcularDescontoFinal(QuantidadeProdutos, ValorUnitario, PercentualDesconto)

print('Valor SEM desconto: R$ {}'.format(CalcularDescontoFinal(QuantidadeProdutos, ValorUnitario)))
print('Valor COM desconto: R$ {}'.format(ValorFinalComDesconto))
print('    -> Desconto de: {}%'.format(PercentualDesconto))
