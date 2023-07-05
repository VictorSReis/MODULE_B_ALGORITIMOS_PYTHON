def VerificarOperadorBooleano(x, y):
    ResultadoRetorno = ""

    if(x == y):
        ResultadoRetorno = "VALOR IGUAL"
    elif (x > y):
        ResultadoRetorno = "X MAIOR"
    else:
        ResultadoRetorno = "Y É MAIOR"

    return ResultadoRetorno

