# ID GLOBAL PARA OS COLABORADORES
ID_GLOBAL = 0

# LISTA QUE VAI CONTER OS COLABORADORES
LISTA_COLABORADORES = []


# MÉTODOS AUXILIARES

def ObterEntradaConsoleComoTexto(pMensagemShowInConsole):
    return input(pMensagemShowInConsole)


def ObterEntradaConsoleComoNumero(pMensagemShowInConsole):
    return int(input(pMensagemShowInConsole))


def MontarDicionarioNovoColaborador(pIdColaborador, pNomeColaborador, pSetorColaborador, pSalarioColaborador):
    NOVO_COLABORADOR_DICI = {'id': pIdColaborador, 'nome': pNomeColaborador, 'setor': pSetorColaborador,
                             'salario': pSalarioColaborador}
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
    print('Salário: {}'.format(ColaboradorDict['salario']))


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
    print()
    TextoMenu = '-' * 30 + 'MENU PRINCIPAL' + '-' * 30
    print(TextoMenu)

    print('1 - Cadastrar Colaborador')
    print('2 - Consultar Colaborador')
    print('3 - Remover Colaborador')
    print('4 - SAIR')
    IdSolicitado = ObterEntradaConsoleComoNumero('')
    return IdSolicitado


# MÉTODOS SOLICITADOS


def CadastrarColaborador(pIdColaborador):
    # OBTÉM A LISTA DE COLABORADORES
    global LISTA_COLABORADORES

    # OBTÉM AS INFORMAÇÕES DO NOVO COLABORADOR
    nome = ObterEntradaConsoleComoTexto('Digite o nome do colaborador: ')
    setor = ObterEntradaConsoleComoTexto('Digite o setor do colaborador: ')
    salario = ObterEntradaConsoleComoTexto('Digite o salário do colaborador R$: ')

    # CRIA O DICIONARIO PARA O NOVO COLABORADOR
    DicNovoColaborador = MontarDicionarioNovoColaborador(pIdColaborador, nome, setor, salario)

    # ADICIONA NA LISTA O NOVO COLABORADOR
    LISTA_COLABORADORES.append(DicNovoColaborador.copy())

    print('Colaborador ({}) cadastrado com sucesso!'.format(nome))


def ConsultarColaborador():
    # 1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu

    print()
    TextoMenu = '-' * 30 + 'MENU DE CONSULTA' + '-' * 30
    print(TextoMenu)

    while True:
        print('Escolha a opção desejada:')
        print('1 - Consultar Todos')
        print('2 - Consultar por Id')
        print('3 - Consultar por Setor')
        print('4 - Retornar ao menu')
        OpSelecionada = ObterEntradaConsoleComoNumero('')

        # VERIFICA SE A OPÇÃO NÃO É INVALIDA
        if OpSelecionada <= 0 and OpSelecionada > 4:
            print('Opção Inválida')
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
    return 0


# MAIN PROGRAM
while True:

    # MOSTRA O MENU PRINCIPAL PARA O USUÁRIO
    idMenu = MostrarMenu()

    # CADASTRO
    if idMenu == 1:
        # INCREMENTA A VARIÁVEL GLOBAL
        ID_GLOBAL += 1

        # CHAMA O MÉTODO PARA CADASTRAR UM NOVO COLABORADOR
        CadastrarColaborador(ID_GLOBAL)

        # VOLTA PARA O INICIO DO MENU PRINCIPAL
        continue

    # CONSULTA
    elif idMenu == 2:
        # CHAMA O MÉTODO QUE ABRE O SUB MENU DE CONSULTA
        ConsultarColaborador()

        # VOLTA PARA O INICIO DO MENU PRINCIPAL
        continue

    # REMOVER
    elif idMenu == 3:
        break

    # SAIR
    else:
        # ENCERRA O PROGRAMA
        print('Encerando...')
        break
