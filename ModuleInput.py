def CalcularValor(x, y):
    return x * y


def GetInputInteger(pMensagem):
    return int(input(pMensagem))


def GetInputFloat(pMensagem):
    FloatValueInputReaded = 0
    try:
        FloatValueInputReaded = float(input(pMensagem))
    finally:
        FloatValueInputReaded = -1

    return FloatValueInputReaded