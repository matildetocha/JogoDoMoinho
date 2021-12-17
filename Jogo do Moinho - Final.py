"""
Projeto 2 - Jogo do Moinho

Matilde Tocha 99108
"""

# TAD posicao: Representa uma posicao do tabuleiro de jogo. Cada posicao e caracterizada
#             pela coluna e linha que ocupa no tabuleiro.
# Representacao[posicao] = (c, l)


def cria_posicao(c, l):
    """
    Construtor posicao.

    Recebe duas cadeias de carateres correspondentes a coluna c e ha linha l de uma
    posicao e devolve a posicao correspondente. Caso algum dos seus argumentos nao seja
    valido, a funcao gera um erro com a mensagem 'cria_posicao: argumentos invalidos'.

    :param c: string, coluna da posicao.
    :param l: string, linha da posicao.
    :return: tuple, posicao do tabuleiro de jogo.

    """
    if not isinstance(c, str) or (c != 'a' and c != 'b' and c != 'c'):
        raise ValueError('cria_posicao: argumentos invalidos')
    if not isinstance(l, str) or (l != '1' and l != '2' and l != '3'):
        raise ValueError('cria_posicao: argumentos invalidos')
    return c, l


def cria_copia_posicao(p):
    """
    Construtor copia posicao.

    Recebe uma posicao e devolve a copia nova da posicao.

    :param p: tuple, posicao do tabuleiro de jogo.
    :return: tuple, posicao do tabuleiro de jogo (copia).
    """
    return cria_posicao(obter_pos_c(p), obter_pos_l(p))


def obter_pos_c(p):
    """
    Seletor coluna.

    Devolve a componente coluna c da posicao p.

    :param p: tuple, posicao do tabuleiro de jogo.
    :return: string, coluna da posicao.
    """
    return p[0]


def obter_pos_l(p):
    """
    Seletor linha.

    Devolve a componente linha l da posicao p.

    :param p: tuple, posicao do tabuleiro de jogo.
    :return: string, linha da posicao.
    """
    return p[1]


def eh_posicao(arg):
    """
    Reconhecedor posicao.

    Recebe um argumento de qualquer tipo e devolve True se o seu argumento
    corresponde a um TAD posicao e False caso contrario.

    :param arg: universal, argumento.
    :return: bool, veracidade do argumento.
    """
    return isinstance(arg, tuple) and len(arg) == 2 and isinstance(obter_pos_c(arg), str) \
        and obter_pos_c(arg) in ('a', 'b', 'c') and isinstance(obter_pos_l(arg), str) and \
        obter_pos_l(arg) in ('1', '2', '3')


def posicoes_iguais(p1, p2):
    """
    Teste posicoes iguais.

    Recebe duas posicoes e devolve True se correspondem a uma posicao e
    sao iguais e False caso contrario.

    :param p1: tuple, posicao do tabuleiro de jogo 1.
    :param p2: tuple, posicao do tabuleiro de jogo 2.
    :return: bool, veracidade dos argumentos (True se forem posicoes e iguais).
    """
    return eh_posicao(p1) and eh_posicao(p2) and obter_pos_c(p1) == obter_pos_c(p2) \
        and obter_pos_l(p1) == obter_pos_l(p2)


def str_para_posicao(p):
    """
    Tranformador posicao.

    Recebe uma cadeia de caracteres que a representa uma posicao e devolve a posicao.

    :param p: string, representacao externa da posicao.
    :return: tuple, posicao do tabuleiro de jogo.
    """
    return p[0], p[1]


def posicao_para_str(p):
    """
    Tranformador posicao.

    Recebe uma posicao e devolve a cadeia de caracteres 'cl' que a representa, sendo os
    valores c e l as componentes coluna e linha de p.

    :param p: tuple, posicao do tabuleiro de jogo.
    :return: string, representacao externa da posicao.
    """
    return '{}{}'.format(obter_pos_c(p), obter_pos_l(p))


def coluna_para_inteiro(c):
    """
    Devolve um inteiro correspondente a coluna da posicao inserida.

    :param c: string, coluna da posicao.
    :return: int, valor correspondente da coluna.
    """
    c_int = {'a': 0, 'b': 1, 'c': 2}
    return c_int[c]


def linha_para_inteiro(l):
    """
    Devolve um inteiro correspondente a linha da posicao inserida.

    :param l: string, linha da posicao.
    :return: int, valor correspondente da linha.
    """
    l_int = {'1': 0, '2': 1, '3': 2}
    return l_int[l]


def obter_posicoes_adjacentes(p):
    """
    Funcao de alto nivel.

    Recebe uma posicao e devolve um tuplo com as posicoes adjacentes a posicao
    inserida de acordo com a ordem de leitura do tabuleiro.

    :param p: tuple, posicao do tabuleiro de jogo.
    :return: tuple, posicoes adjacentes.
    """
    l = obter_pos_l(p)
    c = obter_pos_c(p)
    if l == '1':
        if c == 'a':
            return cria_posicao('b', '1'), cria_posicao('a', '2'), cria_posicao('b', '2')
        elif c == 'c':
            return cria_posicao('b', '1'), cria_posicao('b', '2'), cria_posicao('c', '2')
        return cria_posicao('a', '1'), cria_posicao('c', '1'), cria_posicao('b', '2')
    elif l == '3':
        if c == 'a':
            return cria_posicao('a', '2'), cria_posicao('b', '2'), cria_posicao('b', '3')
        elif c == 'c':
            return cria_posicao('b', '2'), cria_posicao('c', '2'), cria_posicao('b', '3')
        return cria_posicao('b', '2'), cria_posicao('a', '3'), cria_posicao('c', '3')
    elif l == '2':
        if c == 'a' or c == 'c':
            return cria_posicao(c, '1'), cria_posicao('b', l), cria_posicao(c, '3')
        return cria_posicao('a', '1'), cria_posicao('b', '1'), cria_posicao('c', '1'), cria_posicao('a', '2'), \
            cria_posicao('c', '2'), cria_posicao('a', '3'), cria_posicao('b', '3'), cria_posicao('c', '3')


# TAD peca: Representa as pecas do jogo. Cada peca e caracterizada pelo jogador a quem
#           pertencem, podendo ser pecas do jogador 'X' ou do jogador 'O' e, ainda, peca livre ''.
# Representacao[peca] = [j]


def cria_peca(s):
    """
    Construtor peca.

    Recebe uma cadeia de caracteres correspondente ao identificador de um dos dois jogadores
    ('X' ou 'O') ou uma peca livre (' ') e devolve a peca correspondente. Caso algum dos seus
    argumentos nao seja valido, a funcao gera um erro com a mensagem 'cria_peca: argumento invalido'.

    :param s: string, identificador de um dos jogadores ou da peca livre.
    :return: list, peca.
    """
    if not isinstance(s, str) or (s != 'X' and s != 'O' and s != ' '):
        raise ValueError('cria_peca: argumento invalido')
    return [s]


def cria_copia_peca(j):
    """
    Construtor copia peca.

    Recebe uma peca e devolve a copia da nova peca.

    :param j: list, peca.
    :return: list, peca.
    """
    return cria_peca(j[0])


def obter_jogador_peca(j):
    """
    Seletor jogador.

    :param j: list, peca.
    :return: str, jogador.
    """
    return j[0]


def eh_peca(arg):
    """
    Reconhecedor peca.

    Recebe um argumento de qualquer tipo e devolve True se o seu argumento
    corresponde a um TAD peca e False caso contrario.

    :param arg: universal, argumento.
    :return: bool, veracidade do argumento.
    """
    return isinstance(arg, list) and len(arg) == 1 and isinstance(arg[0], str) \
        and (arg[0] == 'X' or arg[0] == 'O' or arg[0] == ' ')


def pecas_iguais(j1, j2):
    """
    Teste pecas iguais.

    Recebe duas pecas e devolve True se correspondem a uma peca e sao
    iguais e False caso contrario.

    :param j1: list, peca 1.
    :param j2: list, peca 2.
    :return: bool, veracidade dos argumentos
    """
    return eh_peca(j1) and eh_peca(j2) and j1[0] == j2[0]


def peca_para_str(j):
    """
    Transformador peca.

    Recebe uma peca e devolve a cadeia de caracteres que a representa.

    :param j: list, peca.
    :return: string, representacao externa da peca.
    """
    return '[{}]'.format(j[0])


def peca_para_inteiro(j):
    """
    Funcao de alto nivel.

    Recebe uma peca e devolve um inteiro com o valor de 1, -1 ou 0, dependendo se a peca e do jogador
    'X', 'O', ou ' ' (livre), respetivamente.

    :param j: list, peca.
    :return: int, valor correspondente a peca do jogador ou livre.
    """
    peca_int = {'X': 1, 'O': -1, ' ': 0}
    return peca_int[obter_jogador_peca(j)]


def inteiro_para_peca(n):
    """
    Funcao de alto nivel.

    Recebe um inteiro e devolve um jogador 'X', 'O', ou ' ' (livre), dependendo se o inteiro e
    1, -1 ou 0 (livre), respetivamente.
    :param n:
    :return:
    """
    int_peca = {1: 'X', -1: 'O', 0: ' '}
    return int_peca[n]


# TAD tabuleiro: Representa um tabuleiro do jogo do moinho de 3x3 posicoes
#                e as pecas dos jogadores que nele sao colocadas.
# Representacao[tabuleiro] = [[j, j, j], [j, j, j], [j, j, j]]


def cria_tabuleiro():
    """
    Construtor tabuleiro.

    Devolve um tabuleiro de jogo do moinho de 3x3 sem posicoes ocupadas por pecas de jogador.

    :return: list, tabuleiro livre.
    """
    return [[cria_peca(' ') for pecas in range(3)] for linhas in range(3)]


def cria_copia_tabuleiro(t):
    """
    Construtor copia tabuleiro.

    Recebe um tabuleiro e devolve uma copia nova do tabuleiro.

    :param t: list, tabuleiro.
    :return: list, tabuleiro.
    """
    return [[cria_copia_peca(j) for j in linhas] for linhas in t]


def obter_peca(t, p):
    """
    Seletor peca.

    Recebe um tabuleiro e uma posicao e devolve a peca na posicao inserida do tabuleiro.
    Se a posicao nao estiver ocupada, devolve uma peca livre.

    :param t: list, tabuleiro.
    :param p: tuple, posicao do tabuleiro.
    :return: list, peca.
    """
    return t[linha_para_inteiro(obter_pos_l(p))][coluna_para_inteiro(obter_pos_c(p))]


def obter_vetor(t, s):
    """
    Seletor vetor.

    Recebe um tabuleiro e uma linha ou coluna e devolve todas as pecas da linha ou coluna
    especificada pelo seu argumento.

    :param t: list, tabuleiro.
    :param s: string, linha ou coluna.
    :return: tuplo, pecas da linha ou coluna.
    """
    return tuple(t[i][coluna_para_inteiro(s)] for i in range(3)) if s in ('a', 'b', 'c') \
        else tuple(t[linha_para_inteiro(s)][i] for i in range(3))


def coloca_peca(t, j, p):
    """
    Modificador tabuleiro.

    Recebe um tabuleiro, uma peca e uma posicao e modifica destrutivamente o tabuleiro t
    colocando a peca j na posicao p, e devolve o proprio tabuleiro.

    :param t: list, tabuleiro.
    :param j: list, peca.
    :param p: tuple, posicao do tabuleiro.
    :return: list, tabuleiro modificado.
    """
    t[linha_para_inteiro(obter_pos_l(p))][coluna_para_inteiro(obter_pos_c(p))] = j
    return t


def remove_peca(t, p):
    """
    Modificador tabuleiro.

    Recebe um tabuleiro e uma posicao e modifica destrutivamente o tabuleiro t removendo a
    peca da posicao p, e devolve o proprio tabuleiro.

    :param t: list, tabuleiro.
    :param p: list, peca.
    :return: list, tabuleiro modificado.
    """
    t[linha_para_inteiro(obter_pos_l(p))][coluna_para_inteiro(obter_pos_c(p))] = cria_peca(' ')
    return t


def move_peca(t, p1, p2):
    """
    Modificador tabuleiro.

    Recebe um tabuleiro, uma posicao 1 e uma posicao 2 e modifica destrutivamente o tabuleiro
    t movendo a peca que se encontra na posicao p1 para a posicao o2, e devolve o proprio
    tabuleiro.

    :param t: list, tabuleiro.
    :param p1: tuple, posicao do tabuleiro 1.
    :param p2: tuple, posicao do tabuleiro 2.
    :return: list, tabuleiro modificado
    """
    coloca_peca(t, obter_peca(t, p1), p2) and remove_peca(t, p1)
    return t


def ha_ganhador(t):
    """
    Recebe um tabuleiro e verifica se ha 1 ou mais jogadores com 3 pecas em linha na vertical
    ou horizontal. Se nao houver ganhador devolve 2, se dois jogadores tiverem um 3 em linha
    devolve -2 e se apenas houver um ganhador devolve o inteiro da peca desse mesmo jogador.

    :param t: list, tabuleiro.
    :return: int, valor do ganhador.
    """
    ganhador = 2
    for s in ('a', 'b', 'c', '1', '2', '3'):
        if obter_vetor(t, s)[0] == obter_vetor(t, s)[1] == obter_vetor(t, s)[2] == cria_peca('X'):
            ganhador -= 1
        elif obter_vetor(t, s)[0] == obter_vetor(t, s)[1] == obter_vetor(t, s)[2] == cria_peca('O'):
            ganhador -= 3
    return ganhador


def eh_tabuleiro(arg):
    """
    Reconhecedor tabuleiro.

    Recebe um argumento de qualquer tipo e devolve True se o seu argumento
    corresponde a um TAD tabuleiro e False caso contrario. Um tabuleiro valido
    pode ter um maximo de 3 pecas de cada jogador, nao pode conter a diferenca
    de 2 peca entre cada jogador e apenas pode haver um ganhador em simultaneo.

    :param arg: universal.
    :return: bool, veracidade do argumento.
    """
    if not isinstance(arg, list) or len(arg) != 3:
        return False
    pecas = []
    for i in arg:
        if not isinstance(i, list) or len(i) != 3:
            return False
        for e in i:
            pecas += [e]
            if not eh_peca(e):
                return False
    pecas_iguais_x = []
    pecas_iguais_o = []
    for p in pecas:
        if pecas_iguais(p, cria_peca('X')):
            pecas_iguais_x += [p]
        elif pecas_iguais(p, cria_peca('O')):
            pecas_iguais_o += [p]
    if len(pecas_iguais_x) > 3 or len(pecas_iguais_o) > 3:
        return False
    if len(pecas_iguais_x) == len(pecas_iguais_o) - 2 or len(pecas_iguais_o) == len(pecas_iguais_x) - 2:
        return False
    if ha_ganhador(arg) == -2:
        return False
    return True


def eh_posicao_livre(t, p):
    """
    Reconhecedor peca livre.

    Recebe um tabuleiro e uma posicao e devolve True se a posicao
    p do tabuleiro corresponder a uma posicao livre e False caso contrario.

    :param t: list, tabuleiro.
    :param p: tuple, posicao do tabuleiro.
    :return: bool, veracidade do argumento.
    """
    return pecas_iguais(obter_peca(t, p), cria_peca(' '))


def tabuleiros_iguais(t1, t2):
    """
    Teste.

    Recebe dois tabuleiro e devolve True se correspondem a um tabuleiro e sao
    iguais e False caso contrario.

    :param t1: list, tabuleiro 1.
    :param t2: list, tabuleiro 2.
    :return: bool, veracidade dos argumentos.
    """
    return eh_tabuleiro(t1) and eh_tabuleiro(t2) and all(pecas_iguais(j1, j2) for linhas1 in t1 for j1 in linhas1
                                                         for linhas2 in t2 for j2 in linhas2)


def tabuleiro_para_str(t):
    """
    Tranformador tabuleiro.

    Recebe um tabuleiro e devolve a cadeia de caracteres que o representa.

    :param t: list, tabuleiro.
    :return: string, representacao externa do tabuleiro.
    """
    return '   a   b   c\n1 {}-{}-{}\n   | \\ | / |\n2 {}-{}-{}' \
           '\n   | / | \\ |\n3 {}-{}-{}'.format(*(peca_para_str(peca) for linhas in t for peca in linhas))


def tuplo_para_tabuleiro(t):
    """
    Tranformador tuplo -> tabuleiro.

    Recebe um tuplo com 3 tuplos, cada um deles contendo 3 valores inteiros
    iguais a 1, -1 ou 0, e devolve o tabuleiro que o representa.

    :param t: tuple.
    :return: list, tabuleiro.
    """
    tab = []
    for i in t:
        for e in i:
            tab += [cria_peca(inteiro_para_peca(e))]
    return [tab[0:3]] + [tab[3:6]] + [tab[6:9]]


def obter_ganhador(t):
    """
    Funcao de alto nivel.

    Recebe um tabuleiro e devolve uma peca do jogador que tenha as suas 3 pecas
    em linha na vertical ou na horizontal no tabuleiro. Se nao existir nenhum
    ganhador, devolve uma peca livre.

    :param t: list, tabuleiro.
    :return: list, peca do jogador ganhador ou peca livre.
    """
    if ha_ganhador(t) == 1 or ha_ganhador(t) == -1:
        return cria_peca(inteiro_para_peca(ha_ganhador(t)))
    return cria_peca(' ')


def obter_posicoes_livres(t):
    """
    Funcao de alto nivel.

    Recebe um tabuleiro e devolve um tuplo com as posicoes nao ocupadas pelas pecas
    de qualquer um dos dois jogadores na ordem de leitura do tabuleiro.

    :param t: list, tabuleiro.
    :return: tuple, posicoes livres do tabuleiro.
    """
    return tuple(cria_posicao(c, l) for l in ('1', '2', '3') for c in ('a', 'b', 'c')
                 if eh_posicao_livre(t, cria_posicao(c, l)))



def obter_posicoes_jogador(t, j):
    """
    Funcao de alto nivel.

    Recebe um tabuleiro e uma peca, e devolve um tuplo com as posicoes ocupadas pelas pecas
    j de um dos dois jogadores na ordem de leitura do tabuleiro.

    :param t: list, tabuleiro.
    :param j: list, peca.
    :return: tuple, posicoes do jogador do tabuleiro.
    """
    return tuple(cria_posicao(c, l) for l in ('1', '2', '3') for c in ('a', 'b', 'c')
                 if pecas_iguais(obter_peca(t, cria_posicao(c, l)), j))


# Funcoes adicionais
def obter_movimento_manual(t, j):
    """
    Funcao auxiliar.

    Recebe um tabuleiro e uma peca de um jogador, e devolve um tuplo com uma ou duas
    posicoes que representam uma posicao ou um movimento introduzido manualmente pelo
    jogador.

    Fase de colocacao: o tuplo apenas contem apenas a posicao escolhida pelo utilizador
                       onde colocar uma nova peca.
    Fase de movimento: o tuplo contem a posicao de origem da peca que se deseja movimentar
                       e a posicao de destino.

    Se nao for possivel movimentar nenhuma peca por estarem todas bloqueadas, o jogador
    pode passar turno escolhendo como movimento a posicao duma peca propria seguida da mesma
    posicao que ocupa.

    Se o valor introduzido pelo jogador nao corresponder a uma posicao ou movimento validos,
    a funcao gera um erro com a mensagem 'obter_movimento_manual: escolha invalida'.

    :param t: list, tabuleiro.
    :param j: list, peca.
    :return: tuple, posicao de colocao ou posicoes de movimento.
    """
    if len(obter_posicoes_jogador(t, j)) < 3:
        p = input('Turno do jogador. Escolha uma posicao: ')
        if len(p) != 2 or not eh_posicao(str_para_posicao(p)) or not eh_posicao_livre(t, str_para_posicao(p)):
            raise ValueError('obter_movimento_manual: escolha invalida')
        return cria_posicao(p[0], p[1]),
    p = input('Turno do jogador. Escolha um movimento: ')
    block = ()
    for pos_j in obter_posicoes_jogador(t, j):
        for adj in obter_posicoes_adjacentes(cria_posicao(pos_j[0], pos_j[1])):
            if eh_posicao_livre(t, adj):
                block += adj,
    if len(p) != 4 or not eh_posicao(str_para_posicao(p[0:2])) or not eh_posicao(str_para_posicao(p[2:4])) \
            or (block and str_para_posicao(p[2:4]) not in obter_posicoes_adjacentes(str_para_posicao(p[0:2]))) \
            or str_para_posicao(p[0:2]) not in obter_posicoes_jogador(t, j):
        raise ValueError('obter_movimento_manual: escolha invalida')
    if (not eh_posicao_livre(t, cria_posicao(p[2:4][0], p[2:4][1])) and block) or (not block
        and not posicoes_iguais(cria_posicao(p[0:2][0], p[0:2][1]), cria_posicao(p[2:4][0], p[2:4][1]))):
        raise ValueError('obter_movimento_manual: escolha invalida')
    return cria_posicao(p[0:2][0], p[0:2][1]), cria_posicao(p[2:4][0], p[2:4][1])


def obter_movimento_auto(t, j, estr):
    """
    Funcao auxiliar.

    Recebe um tabuleiro, uma peca de um jogador e uma cadeia de caracteres representado
    o nivel de dificuldade do jogo, e devolve um tuplo com uma ou duas posicoes que
    representam uma posicao ou um movimento escolhido automaticamente.

    Fase de colocacao: o tuplo apenas comtem apenas a posicao escolhida automaticamente
                       onde colocar uma nova peca seguindo as regras da seccao.
    Fase de movimento: o tuplo contem a posicao de origem da peca a movimentar e a posicao
                       de destino.

    Se nao for possivel movimentar nenhuma peca por estarem todas bloqueadas, a funcao
    devolve como movimento a posicao da primeira peca do jogador seguida da mesma posicao
    que ocupa.

    :param t: list, tabuleiro.
    :param j: list, peca.
    :param estr: string, nivel de dificuldade do jogo.
    :return:
    """
    def vitoria(t, j):  # regra 1
        livres = obter_posicoes_livres(t)
        res = ()
        for l in livres:
            if obter_ganhador(coloca_peca(t, j, l)) == j:
                res += (l,)
            remove_peca(t, l)
        return res

    def bloqueio(t, j):  # regra 2
        return vitoria(t, cria_peca(inteiro_para_peca(-peca_para_inteiro(j))))

    def centro(t, j):  # regra 3
        return (cria_posicao('b', '2'),) if eh_posicao_livre(t, cria_posicao('b', '2')) else ()

    def canto_vazio(t, j):  # regra 4
        cantos = (cria_posicao('a', '1'), cria_posicao('c', '1'), cria_posicao('a', '3'), cria_posicao('c', '3'))
        return tuple(c for c in cantos if eh_posicao_livre(t, c))

    def lateral_vazio(t, j):  # regra 5
        laterais = (cria_posicao('b', '1'), cria_posicao('a', '2'), cria_posicao('c', '2'), cria_posicao('b', '3'))
        return tuple(l for l in laterais if eh_posicao_livre(t, l))

    def facil(t, j):  # movimentacao a nivel facil
        for peca_atual in obter_posicoes_jogador(t, j):
            for pos_adjacente in obter_posicoes_adjacentes(peca_atual):
                if eh_posicao_livre(t, pos_adjacente):
                    return peca_atual, pos_adjacente

    def minimax(t, j, prof, seq_mov):
        if not pecas_iguais(obter_ganhador(t), cria_peca(' ')) or prof == 0:
            return peca_para_inteiro(obter_ganhador(t)), seq_mov
        else:
            melhor_resultado = -peca_para_inteiro(j)
            melhor_seq_mov = []
            for peca_atual in obter_posicoes_jogador(t, j):
                for pos_adjacente in obter_posicoes_adjacentes(peca_atual):
                    if eh_posicao_livre(t, pos_adjacente):
                        copia = cria_copia_tabuleiro(t)
                        new_tab = move_peca(copia, peca_atual, pos_adjacente)
                        novo_resultado, nova_seq_movimentos = \
                            minimax(new_tab, cria_peca(inteiro_para_peca(-peca_para_inteiro(j))), prof - 1
                                    , seq_mov + [(peca_atual, pos_adjacente)])
                        if not melhor_seq_mov or (pecas_iguais(j, cria_peca('X'))
                                                  and novo_resultado > melhor_resultado) \
                                or (pecas_iguais(j, cria_peca('O')) and novo_resultado < melhor_resultado):
                            melhor_resultado, melhor_seq_mov = novo_resultado, nova_seq_movimentos

            return melhor_resultado, melhor_seq_mov

    if len(obter_posicoes_jogador(t, j)) < 3:
        for regra in (vitoria, bloqueio, centro, canto_vazio, lateral_vazio):
            colocacao = regra(t, j)
            if colocacao:
                return colocacao[0],

    profundidade = {'facil': 0, 'normal': 1, 'dificil': 5}
    seq_mov = minimax(t, j, profundidade[estr], [])
    if not seq_mov[1]:
        return facil(t, j)
    return seq_mov[1][0]


def moinho(j_str, estr):
    """
    Funcao principal.

    Recebe duas cadeias de carcateres e devolve a representacao externa da peca
    ganhadora ('[X]' ou '[O]'). O primeiro argumento corresponde a representacao
    externa da peca com que deseja jogar o humano, e o segundo argumento seleciona
    o nivel de dificuldade do jogo.

    O jogo comeca sempre com o jogador 'X' a marcar uma posicao livre.

    Se algum dos argumentos dados forem invalidos a funcao gera um erro.

    :param j_str: string, jogador humano.
    :param estr: string, nivel de dificuldade.
    :return: string, jogo do moinho.

    ...
    ValueError: moinho: argumentos invalidos
    """
    if not isinstance(j_str, str) and j_str not in (peca_para_str(cria_peca('X')), peca_para_str(cria_peca('O'))) \
            and not isinstance(estr, str) and estr not in ('facil', 'normal', 'dificil'):
        raise ValueError('moinho: argumentos invalidos')

    print('Bem-vindo ao JOGO DO MOINHO. Nivel de dificuldade ' + estr + '.')
    t = cria_tabuleiro()
    jog_atual = cria_peca('X')
    jog = cria_peca(j_str[1])
    print(tabuleiro_para_str(t))

    while pecas_iguais(obter_ganhador(t), cria_peca(' ')):
        if pecas_iguais(jog, jog_atual):
            m = obter_movimento_manual(t, jog_atual)
        else:
            print('Turno do computador (' + estr + '):')
            m = obter_movimento_auto(t, jog_atual, estr)

        if len(obter_posicoes_jogador(t, jog_atual)) < 3:
            t = coloca_peca(t, jog_atual, m[0])
        else:
            if posicoes_iguais(m[0], m[1]):
                t = t
            else:
                t = move_peca(t, m[0], m[1])

        print(tabuleiro_para_str(t))
        jog_atual = cria_peca(inteiro_para_peca(-peca_para_inteiro(jog_atual)))

    if pecas_iguais(obter_ganhador(t), cria_peca('X')):
        return peca_para_str(cria_peca('X'))
    elif pecas_iguais(obter_ganhador(t), cria_peca('O')):
        return peca_para_str(cria_peca('O'))
    return 'EMPATE'
