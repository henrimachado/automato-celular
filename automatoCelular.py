
def rule(Ger_At, Regra, Ger, Cel):
    Ger_Nov = [0]*(Cel)
    for i in range(Ger):
        for j in range(Cel):
            o = j-1
            g = j+1

            if g > (Cel-1):
                continue

            else:
                if Ger_At[o] == 0 and Ger_At[j] == 0 and Ger_At[g] == 0:
                    Ger_Nov[j] = Regra[7]

                elif Ger_At[o] == 0 and Ger_At[j] == 0 and Ger_At[g] == 1:
                    Ger_Nov[j] = Regra[6]

                elif Ger_At[o] == 0 and Ger_At[j] == 1 and Ger_At[g] == 0:
                    Ger_Nov[j] = Regra[5]

                elif Ger_At[o] == 0 and Ger_At[j] == 1 and Ger_At[g] == 1:
                    Ger_Nov[j] = Regra[4]

                elif Ger_At[o] == 1 and Ger_At[j] == 0 and Ger_At[g] == 0:
                    Ger_Nov[j] = Regra[3]

                elif Ger_At[o] == 1 and Ger_At[j] == 0 and Ger_At[g] == 1:
                    Ger_Nov[j] = Regra[2]

                elif Ger_At[o] == 1 and Ger_At[j] == 1 and Ger_At[g] == 0:
                    Ger_Nov[j] = Regra[1]

                elif Ger_At[o] == 1 and Ger_At[j] == 1 and Ger_At[g] == 1:
                    Ger_Nov[j] = Regra[0]

        for p in range(Cel):
            Ger_At[p] = Ger_Nov[p]

        for k in range(Cel):
            if Ger_At[k] == 0:
                print(" ", end='')
            else:
                print("0", end='')
        print("\n")


def Inicializar(Cel):
    Ger_At = [0]*Cel
    Ger_At[int(Cel/2)] = 1

    for n in range(Cel):
        if Ger_At[n] == 0:
            print(" ", end='')
        else:
            print("0", end='')
    print("\n")
    return Ger_At


def Bin_Conv(N_Regra):
    Num = N_Regra
    Binario = [""]*8
    for i in range(7, -1, -1):
        if Num % 2 == 0:
            Binario[i] = 0
            Num = int(Num/2)
        else:
            Binario[i] = 1
            Num = int(Num/2)
    return Binario


def Dados(Cel, Ger, N_Regra):
    print("O numero de celulas por geracao sera: {} \nO numero de geracoes sera: {} \nA regra a ser aplicada sera: {}".format(Cel, Ger, N_Regra))
    print("\nPara uma representacao mais fiel, caso o numero de celular inserido por par, sera adicionada uma unidade a mais.")
    print("--------------------------------------------------------------------\n\n")


def Entrada_Cel():
    valido = False

    while (valido == False):
        Cel = int(input("Quantidade de celulas por geracao (Entre 100 e 150): "))

        if Cel < 100 or Cel > 150:
            print("\nValor invalido. Insira novamente")
            valido = False
        else:
            valido = True

    if Cel % 2 == 0:
        Cel = Cel + 1
    return Cel


def Entrada_Ger():
    valido = False

    while (valido == False):
        Ger = int(input("Quantidade de geracoes (Entre 1 e 70): "))

        if Ger <= 0 or Ger > 70:
            print("\nValor invalido. Insira novamente")
            valido = False
        else:
            valido = True

    return Ger


def Entrada_Regra():
    valido = False

    while (valido == False):
        N_Regra = int(input("Regra a ser aplicada (Entre 0 e 255): "))

        if N_Regra < 0 or N_Regra > 255:
            print("\nValor invalido. Insira novamente")
            valido = False
        else:
            valido = True

    return N_Regra


# MAIN
print("Start")

Cel = Entrada_Cel()
Ger = Entrada_Ger()
N_Regra = Entrada_Regra()

Dados(Cel, Ger, N_Regra)
Binario = Bin_Conv(N_Regra)
Ger_At = Inicializar(Cel)
rule(Ger_At, Binario, Ger, Cel)
