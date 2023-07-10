# ID GLOBAL PARA OS COLABORADORES
ID_GLOBAL = 0

# LISTA QUE VAI CONTER OS COLABORADORES
LISTA_COLABORADORES = []


# MÉTODOS AUXILIARES

def ObterEntradaConsoleComoTexto(pMensagemShowInConsole):
    return input(pMensagemShowInConsole)


def ObterEntradaConsoleComoNumero(pMensagemShowInConsole):
    return int(input(pMensagemShowInConsole))


def MontarDicionarioNovoColaborador(pIdColaborador, pNomeColaborador, pSetorColaborador, pPagamentoColaborador):
    NOVO_COLABORADOR_DICI = {'id': pIdColaborador, 'nome': pNomeColaborador, 'setor': pSetorColaborador,
                             'pagamento': pPagamentoColaborador}
    return NOVO_COLABORADOR_DICI


def ObterDictColaboradorId(pIdColaborador):
    DicionarioColaborador = dict()

    # OBTÉM A VARIÁVEL COM OS COLABORADORES
    global LISTA_COLABORADORES

    # RETORNA A QUANTIDADE DE ITENS DENTRO DA LISTA
    QuantidadeColaboradores = len(LISTA_COLABORADORES)

    # FAZ UM FOR PARA VERIFICAR SE EXISTE
    for i in range(0, QuantidadeColaboradores, 1):
        ColaboradorDic = dict(LISTA_COLABORADORES[i])
        if ColaboradorDic['id'] == pIdColaborador:
            DicionarioColaborador = ColaboradorDic.copy()
            break

    return DicionarioColaborador


def MostrarInfoColaborador(pIdColaboradorInLista):
    # OBTÉM O DICIONÁRIO COM AS INFORMAÇÕES DO COLABORADOR COM BASE NO ID INFORMADO NO PARÂMETRO
    ColaboradorDict = ObterDictColaboradorId(pIdColaboradorInLista)

    # MOSTRA AS INFORMAÇÕES DO COLABORADOR
    print('ID: {}'.format(ColaboradorDict['id']))
    print('Nome: {}'.format(ColaboradorDict['nome']))
    print('Setor: {}'.format(ColaboradorDict['setor']))
    print('Pagamento: {}'.format(ColaboradorDict['pagamento']))


def VerificarIDColaboradorExiste(pIdVerificar):
    ResultadoIDExiste = False

    # OBTÉM A VARIÁVEL COM OS COLABORADORES
    global LISTA_COLABORADORES

    # RETORNA A QUANTIDADE DE ITENS DENTRO DA LISTA
    QuantidadeColaboradores = len(LISTA_COLABORADORES)

    # FAZ UM FOR PARA VERIFICAR SE EXISTE
    for i in range(0, QuantidadeColaboradores, 1):
        ColaboradorDic = dict(LISTA_COLABORADORES[i])
        if ColaboradorDic['id'] == pIdVerificar:
            ResultadoIDExiste = True
            break

    return ResultadoIDExiste


def Consultar_ConsultarTodos():
    # OBTÉM A VARIÁVEL COM OS COLABORADORES
    global LISTA_COLABORADORES

    # VERIFICA SE EXISTE ALGUM COLABORADOR
    # RETORNA A QUANTIDADE DE ITENS DENTRO DA LISTA
    QuantidadeColaboradores = len(LISTA_COLABORADORES)
    if QuantidadeColaboradores == 0:
        print('Nenhum colaborador foi cadastrado até o momento!')
        return

    # LISTA TODOS OS COLABORADORES E MOSTRA AS INFORMAÇÕES DE CADA UM
    print()
    TextoLista = 'LISTA DOS COLABORADORES REGISTRADOS:'
    print(TextoLista)
    print('-'*len(TextoLista))
    for i in range(1, QuantidadeColaboradores+1, 1):
        # CHAMA O MÉTODO RESPONSÁVEL POR MOSTRAR AS INFORMÇÕES DO COLABORADOR
        MostrarInfoColaborador(i)
        print()

    print('FINAL LISTA' + '-'*25)
    print()


def Consultar_ConsultarPorId():

    print('-' * 30)
    while True:
        # SOLICITA O ID
        IdParaConsultar = ObterEntradaConsoleComoNumero('Informe o id do colaborador: ')

        # VERIFICA SE O ID EXISTE
        IdColaboradorExiste = VerificarIDColaboradorExiste(IdParaConsultar)
        if not IdColaboradorExiste:
            print('O ID-{} informado não existe na lista de colaboradores. Informe um Id válido'.format(IdParaConsultar))
            continue

        # SE CHEGOU ATÉ AQUI O ID É VÁLIDO E O LAÇO PODE SER QUEBRADO
        break

    # MOSTRA AS INFORMAÇÕES DO COLABORADOR
    MostrarInfoColaborador(IdParaConsultar)


def Consultar_ConsultarPorSetor():
    # OBTÉM A VARIÁVEL COM OS COLABORADORES
    global LISTA_COLABORADORES

    # OBTÉM A QUANTIDADE DE COLABORADORES
    QuantidadeColaboradores = len(LISTA_COLABORADORES)

    # OBTÉM O SETOR A SER CONSULTADO
    SetorColaborador = ObterEntradaConsoleComoTexto('Informe o setor a ser consultado os colaboradores: ').lower()

    print('-' * 30)

    # FAZ UM FOR PARA LISTAR TODOS OS COLABORADORES POR SETOR INDICADO
    for idColab in range(0, QuantidadeColaboradores, 1):
        # OBTÉM O SETOR DO COLABORADOR
        setor = LISTA_COLABORADORES[idColab]['setor'].lower()

        # VERIFICA SE É O SETOR A SER CONSULTADO
        if setor == SetorColaborador:
            # OBTÉM O ID DO COLABORADOR E MOSTRA SUAS INFORMAÇÕES
            MostrarInfoColaborador(LISTA_COLABORADORES[idColab]['id'])
            print()


def MostrarMenu():
    TextoMenu = '-' * 30 + 'MENU PRINCIPAL' + '-' * 30
    print('*'*len(TextoMenu))
    print(TextoMenu)

    print('1 - Cadastrar Colaborador')
    print('2 - Consultar Colaborador')
    print('3 - Remover Colaborador')
    print('4 - SAIR')
    IdSolicitado = ObterEntradaConsoleComoNumero('')
    return IdSolicitado


# MÉTODOS SOLICITADOS


def CadastrarColaborador(pIdColaborador):

    # SHOW MENU CADASTRO
    TextoMenu = '-' * 30 + 'MENU DE CADASTRO' + '-' * 30
    print('*'*len(TextoMenu))
    print(TextoMenu)

    # OBTÉM A LISTA DE COLABORADORES
    global LISTA_COLABORADORES

    # OBTÉM O ID ATUAL
    global ID_GLOBAL

    print('Colaborador ID: {}'.format(ID_GLOBAL))

    # OBTÉM AS INFORMAÇÕES DO NOVO COLABORADOR
    nome = ObterEntradaConsoleComoTexto('Digite o nome do colaborador: ')
    setor = ObterEntradaConsoleComoTexto('Digite o setor do colaborador: ')
    pagamento = ObterEntradaConsoleComoTexto('Digite o pagamento do colaborador R$: ')

    # CRIA O DICIONARIO PARA O NOVO COLABORADOR
    DicNovoColaborador = MontarDicionarioNovoColaborador(pIdColaborador, nome, setor, pagamento)

    # ADICIONA NA LISTA O NOVO COLABORADOR
    LISTA_COLABORADORES.append(DicNovoColaborador.copy())

    # MOSTRA O NOME DO COLABORADOR CADASTRADO
    TextoColaboradorCadastrado = '| Colaborador ({}) cadastrado com sucesso! |'.format(nome)
    print('-'*len(TextoColaboradorCadastrado))
    print(TextoColaboradorCadastrado)
    print('-'*len(TextoColaboradorCadastrado))


def ConsultarColaborador():
    # 1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu

    TextoMenu = '-' * 30 + 'MENU DE CONSULTA' + '-' * 30
    print('*'*len(TextoMenu))
    print(TextoMenu)

    while True:
        print('Escolha a opção desejada:')
        print('1 - Consultar Todos')
        print('2 - Consultar por Id')
        print('3 - Consultar por Setor')
        print('4 - Retornar ao menu')
        OpSelecionada = ObterEntradaConsoleComoNumero('')

        # VERIFICA SE A OPÇÃO NÃO É INVALIDA
        if OpSelecionada <= 0 or OpSelecionada > 4:
            print('Opção Inválida')
            print()
            continue

        # VERIFICA E FAZ A CONSULTA DO COLABORADOR COM BASE NO ID INFORMADO
        if OpSelecionada == 1:
            Consultar_ConsultarTodos()
        elif OpSelecionada == 2:
            Consultar_ConsultarPorId()
        elif OpSelecionada == 3:
            Consultar_ConsultarPorSetor()
        else:
            # EXIT MENU -> CONSULTAR COLABORADOR
            break


def RemoverColaborador():

    TextoMenu = '-' * 25 + 'MENU REMOVER COLABORADOR' + '-' * 25
    print('*'*len(TextoMenu))
    print(TextoMenu)

    # VARIÁVEL QUE VAI RECEBER O ID QUE SERÁ REMOVIDO
    IdParaRemover = -1

    # ABRE UM LAÇO PARA OBTER O ID E TENTAR VALIDAR PARA SABER SE EXISTE MESMO
    while True:
        # SOLICITA O ID
        IdParaRemover = ObterEntradaConsoleComoNumero('Informe o id do colaborador a ser removido: ')

        # VERIFICA SE O ID EXISTE
        IdColaboradorExiste = VerificarIDColaboradorExiste(IdParaRemover)
        if not IdColaboradorExiste:
            print(
                'O ID-{} informado não existe na lista de colaboradores. Informe um Id válido'.format(IdParaRemover))

            # SAI DO MENU CASO O USUÁRIO NÃO LEMBRE O ID OU NÃO TENHA CADASTRADO
            # CASO NÃO TIVESSE NADA CADASTRADO, O USUÁRIO FICARIA PRESO NESSE MENU SE NÃO HOUVER
            # ESSA SESSÃO DE CÓDIGO
            SairMenu = ObterEntradaConsoleComoTexto('Deseja sair do menu (s/n)?: ').lower()
            if SairMenu == 's':
                IdParaRemover = -1
                break

            continue

        # SE CHEGOU ATÉ AQUI O ID É VÁLIDO E O LAÇO PODE SER QUEBRADO
        break

    # VERIFICA SE O USUÁRIO NÃO OPTOU POR SAIR
    # SE SIM, A VARIÁVEL 'IdParaRemover' TEM SEU VALOR IGUAL A -1
    if IdParaRemover == -1:
        return

    # OBTÉM A VARIÁVEL COM OS COLABORADORES
    global LISTA_COLABORADORES

    # OBTÉM A QUANTIDADE DE COLABORADORES
    QuantidadeColaboradores = len(LISTA_COLABORADORES)

    # ARMAZENA O DICT DO COLABORADOR A SER REMOVIDO
    DictColaboradorRemover = dict()

    # ABRE UM FOR PARA PROCURAR O INDEX DA LISTA A QUAL ESTÁ O COLABORADOR DO ID INFORMADO
    for i in range(0, QuantidadeColaboradores, 1):
        if LISTA_COLABORADORES[i]['id'] == IdParaRemover:
            DictColaboradorRemover = LISTA_COLABORADORES[i]
            break

    # REMOVE O COLABORADOR
    LISTA_COLABORADORES.remove(DictColaboradorRemover)


# MAIN PROGRAM
print('Bem-Vindo ao Departamento de Controle de Colaboradores de Victor Santos Reis :)')
while True:

    # MOSTRA O MENU PRINCIPAL PARA O USUÁRIO E OBTÉM O ID DA FUNÇÃO DESEJADA
    idMenu = MostrarMenu()

    # VALIDA O ID INFORMADO
    if idMenu <= 0 or idMenu >= 5:
        print('Opção inválida')
        continue

    # CADASTRAR COLABORADOR
    if idMenu == 1:
        # INCREMENTA A VARIÁVEL GLOBAL
        ID_GLOBAL += 1

        # CHAMA O MÉTODO PARA CADASTRAR UM NOVO COLABORADOR
        CadastrarColaborador(ID_GLOBAL)

        # VOLTA PARA O INICIO DO MENU PRINCIPAL
        continue

    # CONSULTAR COLABORADOR
    elif idMenu == 2:
        # CHAMA O MÉTODO QUE ABRE O SUB MENU DE CONSULTA
        ConsultarColaborador()

        # VOLTA PARA O INICIO DO MENU PRINCIPAL
        continue

    # REMOVER COLABORADOR
    elif idMenu == 3:
        # CHAMA O MÉTODO PARA REMOVER O COLABORADOR
        RemoverColaborador()

        # VOLTA PARA O INICIO DO MENU PRINCIPAL
        continue

    # SAIR - ID 4
    else:
        # ENCERRA O PROGRAMA
        print('Encerando...')
        break
