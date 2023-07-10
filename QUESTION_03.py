# FUNÇÕES AUXILIARES

GLOBAL_MAXIMUM_PESO_CACHORRO = 49.99


def ObterEntradaConsoleComoNumero(pMensagemShowInConsole):
    # RETORNAR -1 SE O VALOR DIGITADO É INVALIDO / NÃO TEXTO
    # SATISFAZ A EXIGÊNCIA DE CÓDIGO = 5 DE 6
    InputConsoleNumero = 0

    # ABRE UM TRY PARA EVITAR EXCEÇÕES NO CÓDIGO CASO O USUÁRIO INFORME ALGO QUE NÃO
    # SEJA UM NÚMERO VÁLIDO
    try:
        InputConsoleNumero = int(input(pMensagemShowInConsole))
    except ValueError:
        # O VALOR DIGITADO NÃO É UM NÚMERO VÁLIDO
        InputConsoleNumero = -1
    return InputConsoleNumero


def ObterEntradaConsoleComoTextoLowerCase(pMensagemShowInConsole):
    return input(pMensagemShowInConsole).lower()


def ExibirMensagemInicial():
    print('Bem-vindo ao pet shop de Victor Santos Reis :)')


def ValidarPesoCachorro(pPesoInformado):
    global GLOBAL_MAXIMUM_PESO_CACHORRO
    return pPesoInformado <= GLOBAL_MAXIMUM_PESO_CACHORRO


def ValidarTamanhoPelo(pTamanhoPelo):
    if pTamanhoPelo == 'c':
        return True
    elif pTamanhoPelo == 'm':
        return True
    elif pTamanhoPelo == 'l':
        return True
    else:
        # O TAMANHO DO PELO INFORMADO NÃO É SUPORTADO
        return False


def ValidarServicoAdicional(pServicoID):
    if pServicoID >= 0 and pServicoID <= 3:
        return True
    else:
        return False


def ObterValorCobradoBaseBanho(pPesoInformado):
    ValorBase = 0
    if pPesoInformado < 3.00:
        ValorBase = 40.00
    elif pPesoInformado < 10.00:
        ValorBase = 50
    elif pPesoInformado < 30.00:
        ValorBase = 60
    else:
        # PRESSUPÕE-SE QUE O PARÂMETRO 'pPesoInformado' já foi validado e é menor que 50 kg
        # CASO CONTRARIO, ESSE ELSE CAUSARIA UM BUG DEVIDO AO PESO MÁXIMO SER MENOR QUE 50 kg
        # E ESSE ELSE RECEBER QUAL QUER VALOR QUE FOSSE MAIOR QUE 30
        ValorBase = 70
    return ValorBase


def ObterValorAdicional(pNumberAdicional):
    # ADICIONAL(CORTAR UNHAS (1)) - R$ 10,00
    # ADICIONAL(ESCOVAR DENTES (2)) - R$ 12,00
    # ADICIONAL(LIMPAR ORELHAS (3)) - R$ 15,00
    # ADICIONAL(NÃO ADICIONAR MAIS NADA (0)) - R$ 0,00

    ValorAdicionalInformado = 0
    if pNumberAdicional == 0:
        ValorAdicionalInformado = 0.00
    elif pNumberAdicional == 1:
        ValorAdicionalInformado = 10.00
    elif pNumberAdicional == 2:
        ValorAdicionalInformado = 12.00
    else:
        ValorAdicionalInformado = 15.00

    return ValorAdicionalInformado


def Cachorro_Peso():
    PesoCachorro = 0
    while True:
        # TENTA OBTER O PESO DO CACHORRO
        PesoCachorro = ObterEntradaConsoleComoNumero("Entre com o peso do cachorro: ")
        if PesoCachorro == -1:
            print('Favor informar um peso valido, apenas número é aceito!')
            continue

        # VALIDA O PESO DO CACHORRO== FALSE SE >= 50 kg
        # SE NÃO PASSAR NA VALIDAÇÃO, VOLTA PARA O INICIO.
        PesoValido = ValidarPesoCachorro(PesoCachorro)
        if not PesoValido:
            print('Desculpe, apenas cachorro com o peso inferior a 50 kg é aceito!')
            print('Informe um valor válido')
            continue

        # SE CHEGAR AQUI O PESO FOI OBTIDO E VALIDADO COM SUCESSO
        # QUEBRA O WHILE PARA RETORNAR O PESO
        break
    return PesoCachorro


def Cachorro_Pelo():

    # VARIÁVEL QUE VAI CONTER O VALOR DO MULTIPLICADOR
    Multiplicador = 0

    # ABRE O LAÇO PARA OBTER O MULTIPLICADOR E VALIDAR ANTES QUE POSSA RETORNAR.
    while True:
        print()
        print('Favor informar o tamanho do pelo do cachorro, conforme disponível abaixo')
        print('Pelo Curto : c')
        print('Pelo Médio : m')
        print('Pelo Longo : l')

        # OBTÉM O TAMANHO DO PELO PARA DEFINIR QUAL SERÁ O MULTIPLICADOR.
        TamanhoPelo = ObterEntradaConsoleComoTextoLowerCase('Tamanho: ')
        if not ValidarTamanhoPelo(TamanhoPelo):
            print('O tamanho do peso informado ({}) não é válido. Tente novamente.'.format(TamanhoPelo))
            continue

        # OBTÉM O MULTIPLICADOR PARA O TAMANHO DO PELO
        if TamanhoPelo == 'c':
            Multiplicador = 1.0
        elif TamanhoPelo == 'm':
            Multiplicador = 1.5
        else:
            # TAMANHO - L
            Multiplicador = 2.0

        # SE CHEGOU ATÉ AQUI O LAÇO PODE SER QUEBRADO E SAIR
        break
    return Multiplicador


def Cachorro_Extra():
    TotalAdicionais = 0.00
    while True:
        print()
        print('Especifique se deseja algum serviço adicional da lista abaixo.')
        print('1- CORTAR UNHAS - R$ 10,00')
        print('2- ESCOVAR DENTES - R$ 12,00')
        print('3- LIMPAR ORELHAS - R$ 15,00')
        print('0- NÃO ADICIONAR MAIS NADA')
        OpSelecionada = ObterEntradaConsoleComoNumero("Digite a opção: ")
        if not ValidarServicoAdicional(OpSelecionada):
            print('O serviço adicional inserido ({}) não é válido. Tente novamente.')
            continue

        # VERIFICA SE NÃO SOLICITOU PARA FINALIZAR
        if OpSelecionada == 0:
            break

        # CALCULA O VALOR DO SERVIÇO ADICIONAL ESPECIFICADO E SOMA AO TOTAL
        TotalAdicionais += ObterValorAdicional(OpSelecionada)
    return TotalAdicionais


# MAIN PROGRAM
ExibirMensagemInicial()

# OBTÉM AS INFORMAÇÕES NECESSÁRIAS PARA CALCULAR O VALOR FINAL
PesoAuAu = Cachorro_Peso()
Multiplicador = Cachorro_Pelo()
ValorAdicionais = Cachorro_Extra()
ValorBanho = ObterValorCobradoBaseBanho(PesoAuAu)

# FORMULA PARA CALCULO FINAL
# VALOR BASE * MULTIPLICADOR + ADICIONAL
ValorFinal = ValorBanho * Multiplicador + ValorAdicionais
TextoFinal = '| O valor total a ser pago é de: R$ {:.2f} |'.format(ValorFinal)
LenTexto = len(TextoFinal)

# APLICA UM ESPAÇO ANTES DE MOSTRAR O VALOR FINAL
print()

print('-'*LenTexto)
print(TextoFinal)
print('-'*LenTexto)
