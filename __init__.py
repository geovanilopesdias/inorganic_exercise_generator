# Fontes:
# http://dequi.eel.usp.br/domingos/tabelapdf.pdf
# https://static.todamateria.com.br/upload/ta/be/tabela-periodica-og.jpg
# Unicode Table: https://unicode-table.com/pt/#superscripts-and-subscripts
# Sobrescrito: \u207 ou \u00B (consultar necessidade)
# Subscrito: \u208 (consultar necessidade)

# CADASTROS
cadastro_anions = [['fluoreto', 'F', 1, 19],
                ['cloreto', 'Cl', 1, 35.5],
                ['brometo', 'Br', 1, 79.9],
                ['iodeto', 'I', 1, 126.9],
                ['hipoclorito', 'ClO', 1, 51.5],
                ['clorito', 'ClO\u2082', 1, 67.5],
                ['clorato', 'ClO\u2083', 1, 83.5],
                ['perclorato', 'ClO\u2084', 1, 99.5],
                ['hipobromito', 'BrO', 1, 95.9],
                ['bromato', 'BrO\u2083', 1, 127.9],
                ['hipoiodito', 'IO', 1, 142.9],
                ['iodato', 'IO\u2083', 1, 174.9],
                ['periodato', 'IO\u2084', 1, 190.9],
                ['cianeto', 'CN', 1, 26],
                ['cianato', 'CNO', 1, 42],
                ['tiocianato', 'CNS', 1, 58.1],
                ['acetato', 'C\u2082H\u2083O\u2082', 1, 59],
                ['carbonato', 'CO\u2083', 1, 60],
                ['ferricianeto', '[Fe(CN)\u2086]', 3, 211.8],
                ['ferrocianeto', '[Fe(CN)\u2086]', 4, 211.8],
                ['nitrito', 'NO\u2082', 1, 46],
                ['nitrato', 'NO\u2083', 1, 62],
                ['nitreto', 'N\u2083', 1, 42],
                ['metafosfato', 'PO\u2083', 1, 79],
                ['hipofosfito', 'H\u2082PO\u2082', 1, 65],
                ['fosfito', 'HPO\u2083', 2, 80],
                ['fosfato', 'PO\u2084', 3, 95],
                ['fosfeto', 'P\u2083', 3, 93],
                ['pirofosfato', 'P\u2082O\u2087', 4, 174],
                ['hipofosfato', 'P\u2082O', 4, 78],
                ['sulfeto', 'S', 2, 32.1],
                ['sulfito', 'SO\u2083', 2, 80.1],
                ['sulfato', 'SO\u2084', 2, 96.1],
                ['tiossulfato', 'S\u2082O\u2083', 2, 112.2],
                ['hipossulfito', 'S\u2082O\u2084', 2, 128.2],
                ['persulfato', 'S\u2082O\u2088', 2, 192.2],
                ['tetrationato', 'S\u2084O\u2086', 2, 224],
                ['permanganato', 'MnO\u2084', 1, 118.9],
                ['manganato', 'MnO\u2084', 2, 118.9],
                ['manganito', 'MnO\u2083', 2, 102.9],
                ['hidr??xido', 'OH', 1, 17],
                ['??xido', 'O', 2, 16],
                ['hidreto', 'H', 1, 1],
                ['cromato', 'CrO\u2084', 2, 116],
                ['dicromato', 'Cr\u2082O\u2087', 2, 216],
                ['arsenito', 'AsO\u2083', 3, 122.9],
                ['arsenato', 'AsO\u2084', 3, 138.9],
                ['borato', 'BO\u2083', 3, 58.8]]

cadastro_cations = [['litio', 'Li', 1, 9.4],
                ['s??dio', 'Na', 1, 23],
                ['pot??ssio', 'K', 1, 39.1],
                ['rub??dio', 'Rb', 1, 85.8],
                ['c??sio', 'Cs', 1, 132.9],
                ['prata', 'Ag', 1, 107.9],
                ['cobre I', 'Cu', 1, 63.5],
                ['ouro I', 'Au', 1, 197],
                ['am??nio', u'NH\u2084', 1, 18],
                ['ber??lio', 'Be', 2, 9],
                ['magn??sio', 'Mg', 2, 24.3],
                ['c??lcio', 'Ca', 2, 40],
                ['estr??ncio', 'Sr', 2, 87.6],
                ['b??rio', 'Ba', 2, 137.3],
                ['r??dio', 'Ra', 2, 226],
                ['zinco', 'Zn', 2, 65.4],
                ['c??dmio', 'Cd', 2, 112.4],
                ['cobre II', 'Cu', 2, 63.5],
                ['merc??rio II', 'Hg', 2, 200.6],
                ['ferro II', 'Fe', 2, 55.8],
                ['cobalto II', 'Co', 2, 58.9],
                ['n??quel II', 'Ni', 2, 58.7],
                ['cromo II', 'Cr', 2, 52],
                ['mangan??s II', 'Mn', 2, 54.9],
                ['estanho II', 'Sn', 2, 118.7],
                ['chumbo II', 'Pb', 2, 207.2],
                ['tit??nio II', 'Ti', 2, 47.9],
                ['platina II', 'Pt', 2, 195],
                ['alum??nio', 'Al', 3, 27],
                ['bismuto', 'Bi', 3, 209],
                ['ouro III', 'Au', 3, 197],
                ['ferro III', 'Fe', 3, 55.8],
                ['cobalto III', 'Co', 3, 58.9],
                ['n??quel III', 'Ni', 3, 58.7],
                ['cromo III', 'Cr', 3, 52],
                ['estanho IV', 'Sn', 4, 118.7],
                ['chumbo IV', 'Pb', 4, 207.2],
                ['tit??nio IV', 'Ti', 4, 47.9],
                ['platina IV', 'Pt', 4, 195],
                ['mangan??s IV', 'Mn', 4, 54.9]]

cadastro_aplicacoes = [['cloreto de s??dio', ],
                       []]

cadastro_prefixo_iupac = ['met', 'et', 'prop', 'but', 'pent',
                          'hex', 'hept', 'oct', 'non', 'dec',
                          'undec', 'dodec', 'tridec', 'tetradec', 'pentadec',
                          'hexadec', 'heptadec', 'octadec', 'nonadec', 'eicos']

cadastro_prefixo_subst = ['', 'di', 'tri', 'tetra', 'penta',
                          'hexa', 'hepta', 'octa', 'nona', 'deca',
                          'undeca', 'dodeca', 'trideca', 'tetradeca', 'pentadeca',
                          'hexadeca', 'heptadeca', 'octadeca', 'nonadeca', 'icosa']

# ??ndices do cadastro redox:

# 0: Lista com reagentes cadastros em sublistas (0: s??mbolo, 1: coeficiente, 2: nome, 3: massa molar)
# 1: Lista com produtos cadastros em sublistas (0: s??mbolo, 1: coeficiente, 2: nome, 3: massa molar)
# 2: potencial-padr??o de redu????o (25 ??C)
# 3: n??mero de el??trons da redu????o
# Exemplos:
# cadastro_redox[0][2] ??? Potencial-padr??o (E) da primeira semirea????o
# cadastro_redox[0][0] ??? Lista de reagentes da primeira semirea????o
# cadastro_redox[0][0][0] ??? Lista de dados do primeiro reagente da primeira semirea????o
# cadastro_redox[0][0][0][0] ??? S??mbolo do primeiro reagente da primeira semirea????o

cadastro_redox = [[[['F\u2082', 1, 'fl??or', 19]], [['F\u207B', 2, '??on fluoreto', 19]], 2.87, 2],
                  [[['O\u2083', 1, 'oz??nio', 48], ['H\u207A', 2, '??on hidrog??nio', 1]], [['O\u2082', 1, 'oxig??nio', 32], ['H\u2082', 1, '??gua', 18]], 2.07, 2],
                  [[['Co\u00B3\u207A', 1, '??on cobalto III', 58.9]], [['Co\u00B2\u207A', 1, '??on cobalto II', 58.9]], 1.82, 1],
                  [[['H\u2082O\u2082', 1, 'per??xido de hidrog??nio', 19], ['H\u207A', 2, '??on hidrog??nio', 1]], [['H\u2082O', 2, '??gua', 18]], 1.77, 2],
                  [[['MnO\u2084\u207B', 1, '??on manganato', 188.9], ['H\u207A', 8, '??on hidrog??nio', 1]], [['Mn 2\u207A', 1, '??on mangan??s', 54.9], ['H\u2082O', 4, '??gua', 18]], 1.51, 5],
                  [[['Au\u00B3\u207A', 1, '??on ouro III', 197]], [['Au', 1, 'ouro', 197]], 1.5, 3],
                  [[['Cl\u2082', 1, 'cloro', 71]], [['Cl\u207B', 2, '??on cloreto', 35.5]], 1.36, 2],
                  [[['(Cr\u2082O\u2087)\u00B2\u207B', 1, '??on dicromato', 216], ['H\u207A', 14, '??on hidrog??nio', 1]], [['Cr\u00B3\u207A', 2, '??on cromo III', 52], ['H\u2082O', 7, '??gua', 18]], 1.33, 6],
                  [[['MnO\u2082', 1, '??xido de mangan??s IV', 86.9], ['H\u207A', 4, '??on hidrog??nio', 1]], [['Mn 2\u207A', 1, '??on mangan??s II', 54.9], ['H\u2082O', 2, '??gua', 18]], 1.232, 2],
                  [[['O\u2082', 1, 'oxig??nio', 32], ['H\u207A', 4, '??on hidrog??nio', 1]], [['H\u2082O', 2, '??gua', 18]], 1.231, 4],
                  [[['Br\u2082', 1, 'bromo', 79.9]], [['Br\u207B', 2, '??on brometo', 79.9]], 1.07, 2],
                  [[['(NO\u2083)\u207B', 1, '??on nitrato', 62], ['H\u207A', 4, '??on hidrog??nio', 1]], [['NO', 1, 'mon??xido de nitrog??nio', 30], ['H\u2082O', 2, '??gua', 18]], 0.96, 3],
                  [[['Ag\u207A', 1, '??on prata', 107.9]], [['Ag', 1, 'prata', 107.9]], 0.8, 1],
                  [[['Fe\u00B3\u207A', 1, '??on ferro III', 55.8]], [['Fe\u00B2\u207A', 1, '??on ferro II', 55.8]], 0.77, 1],
                  [[['O\u2082', 1, 'oxig??nio', 32], ['H\u207A', 2, '??on hidrog??nio', 1]], [['H\u2082O\u2082', 2, 'per??xido de hidrog??nio', 19]], 0.68, 2],
                  # [[['MnO\u2084 -', 1, '??xido de mangan??s IV'], ['H\u2082O', 2, '??gua']], [['MnO\u2082', 1, '??xido de mangan??s IV'], ['HO\u207B', 4, '??on hidr??xido']], 0.59, 3],
                  [[['I\u2082', 1, 'iodo', 253.8]], [['I -', 2, '??on iodeto', 126.9]], 0.53, 2],
                  [[['O\u2082', 1, 'oxig??nio', 32], ['H\u2082O', 2, '??gua', 18]], [['HO\u207B', 4, '??on hidr??xido', 17]], 0.4, 4],
                  [[['Cu\u00B2\u207A', 1, '??on cobre II', 63.5]], [['Cu', 1, 'cobre', 63.5]], 0.34, 2],
                  [[['AgCl', 1, 'cloreto de prata', 143.4]], [['Ag', 1, 'prata', 107.9], ['Cl\u207B', 1, '??on cloreto', 35.5]], 0.22, 1],
                  [[['(SO\u2084)\u00B2\u207B', 1, '??on sulfato', 96.2], ['H\u207A', 4, '??on hidrog??nio', 1]], [['SO\u2082', 1, 'di??xido de enxofre', 64.1], ['H\u2082O', 2, '??gua', 18]], 0.2, 2],
                  [[['Cu\u00B2\u207A', 1, '??on cobre II', 63.5]], [['Cu\u207A', 1, '??on cobre I', 63.5]], 0.15, 1],
                  [[['Sn\u2074\u207A', 1, '??on estanho IV', 118.7]], [['Sn\u00B2\u207A', 1, '??on estanho II', 118.7]], 0.13, 2],
                  [[['H\u207A', 2, '??on hidrog??nio', 1]], [['H\u2082', 1, 'hidrog??nio', 2]], 0, 2],
                  [[['Pb\u00B2\u207A', 1, '??on chumbo II', 207.2]], [['Pb', 1, 'chumbo', 207.2]], -0.13, 2],
                  [[['Sn\u00B2\u207A', 1, '??on estanho II', 118.7]], [['Sn', 1, 'estanho', 118.7]], -0.14, 2],
                  [[['Ni\u00B2\u207A', 1, '??on n??quel II', 58.7]], [['Ni', 1, 'n??quel', 58.7]], -0.25, 2],
                  [[['Co\u00B2\u207A', 1, '??on cobalto II', 58.9]], [['Co', 1, 'cobalto', 58.9]], -0.28, 2],
                  [[['PbSO\u2084', 1, 'sulfato de chumbo II', 303.2]], [['Pb', 1, 'chumbo', 207.2], ['(SO\u2084)\u00B2\u207B', 1, '??on sulfato', 96]], -0.31, 2],
                  [[['Cd\u00B2\u207A', 1, '??on c??dmio II', 112.4]], [['Cd', 1, 'c??dmio', 112.4]], -0.40, 2],
                  [[['Fe\u00B2\u207A', 1, '??on ferro II', 55.8]], [['Fe', 1, 'ferro', 55.8]], -0.44, 2],
                  [[['Cr\u00B3\u207A', 1, '??on cromo III', 52]], [['Cr', 1, 'cromo', 52]], -0.74, 3],
                  [[['Zn\u00B2\u207A', 1, '??on zinco', 65.4]], [['Zn', 1, 'zinco', 65.4]], -0.76, 2],
                  # [[['H\u2082', 2, 'hidrog??nio', 2]], [['H\u2082', 1, 'hidrog??nio'], ['HO -', 2, '??on hidr??xido', 17]], -0.83, 2],
                  [[['Mn\u00B2\u207A', 1, '??on mangan??s II', 54.9]], [['Mn', 1, 'mangan??s', 54.9]], -1.18, 2],
                  [[['Al\u00B3\u207A', 1, '??on alum??nio', 27]], [['Al', 1, 'alum??nio', 27]], -1.66, 3],
                  [[['Be\u00B2\u207A', 1, '??on ber??lio', 9]], [['Be', 1, 'ber??lio', 9]], -1.85, 2],
                  [[['Mg\u00B2\u207A', 1, '??on magn??sio', 24.3]], [['Mg', 1, 'magn??sio', 24.3]], -2.37, 2],
                  [[['Na\u207A', 1, '??on s??dio', 23]], [['Na', 1, 's??dio', 23]], -2.71, 1],
                  [[['Ca\u00B2\u207A', 1, '??on c??lcio', 40.1]], [['Ca', 1, 'c??lcio', 40.1]], -2.87, 2],
                  [[['Sr\u00B2\u207A', 1, '??on estr??ncio', 87.6]], [['Sr', 1, 'estr??ncio', 87.6]], -2.89, 2],
                  [[['Ba\u00B2\u207A', 1, '??on b??rio', 137.3]], [['Ba', 1, 'b??rio', 137.3]], -2.90, 2],
                  [[['K\u207A', 1, '??on pot??ssio', 39.1]], [['K', 1, 'pot??ssio', 39.1]], -2.93, 1],
                  [[['Li\u207A', 1, '??on l??tio', 6.9]], [['Li', 1, 'l??tio', 6.9]], -3.05, 1]]


def monta_semireducao():
    from random import randint
    cr = cadastro_redox.copy()
    sr = randint(0, len(cr)-1)
    rg = s = 0  # ??ndices de reagentes e s??mbolos em geral
    pd = c = 1  # ??ndices de produtos e coeficientes em geral
    pt = 2  # ??ndice geral dos potenciais
    e = 3  # indice geral dos el??trons

    if len(cr[sr][0]) == len(cr[sr][1]) == 1:  # Um reagente e um produto
        return f'{cr[sr][rg][0][c]} {cr[sr][rg][0][s]} + {cr[sr][e]} e ??? '+\
               f'{cr[sr][pd][0][c]} {cr[sr][pd][0][s]}  |  E = {cr[sr][pt]} V'

    elif len(cr[sr][0]) == 2 and len(cr[sr][1]) == 1:  # Dois reagentes e um produto
        return f'{cr[sr][rg][0][c]} {cr[sr][rg][0][s]} + '+\
                f'{cr[sr][rg][1][c]} {cr[sr][rg][1][s]} + '+\
                f'{cr[sr][e]} e ??? '+\
                f'{cr[sr][pd][0][c]} {cr[sr][pd][0][s]}  |  E = {cr[sr][pt]} V'
    elif len(cr[sr][0]) == 1 and len(cr[sr][1]) == 2:  # Um reagente e dois produtos
        return f'{cr[sr][rg][0][c]} {cr[sr][rg][0][s]} + {cr[sr][e]} e ??? '+\
               f'{cr[sr][pd][0][c]} {cr[sr][pd][0][s]} + '+\
               f'{cr[sr][pd][1][c]} {cr[sr][pd][1][s]}  |  E = {cr[sr][pt]} V'

    elif len(cr[sr][0]) == len(cr[sr][1]) == 2:  # Dois reagente e dois produtos
        return f'{cr[sr][rg][0][c]} {cr[sr][rg][0][s]} + '+\
               f'{cr[sr][rg][1][c]} {cr[sr][rg][1][s]} + '+\
               f'{cr[sr][e]} e ??? '+\
               f'{cr[sr][pd][0][c]} {cr[sr][pd][0][s]} + '+\
               f'{cr[sr][pd][1][c]} {cr[sr][pd][1][s]}  |  E = {cr[sr][pt]} V'


def sorteia_redox():
    from random import randint
    # ??ndices ??teis
    rg = s = 0  # ??ndices de reagentes e s??mbolos em geral
    pd = c = 1  # ??ndices de produtos e coeficientes em geral
    n = pt = 2  # ??ndice de nomes de subst??ncias e dos potenciais em geral
    m = e = 3  # indice das massas molares e dos el??trons em geral

    # sorteio dos ??ndices das semi-rea????es
    cr = cadastro_redox.copy()
    ia = randint(0, len(cr)-1)
    ib = randint(0, len(cr)-1)
    while ia == ib:
        ib = randint(0, len(cr) - 1)

    # defini????o das semi-re????es direta e inversa com base no potencial-padr??o
    if cr[ia][pt] > cr[ib][pt]:
        dir = cr[ia]
        ind = cr[ib]
    else:
        dir = cr[ib]
        ind = cr[ia]

    # Defini????o dos fatores de multiplica????o dos coeficientes com base no n??mero de el??trons
    primos = (2, 3, 5, 7)
    if dir[e] == ind[e]:
        fdir = find = 1
    elif int(dir[e]/ind[e]) - dir[e]/ind[e] == 0 or int(ind[e]/dir[e]) - ind[e]/dir[e] == 0:
        if dir[e] < ind[e]:
            fdir = int(ind[e] / dir[e])
            find = 1
        else:
            fdir = 1
            find = int(dir[e] / ind[e])
    elif (dir[e] in primos and ind[e] in primos) or\
            (dir[e] == 3 or dir[e] == 5 or dir[e] == 6 and ind[e] == 4) or\
            (dir[e] == 4 and ind[e] == 3 or ind[e] == 5 or ind[e] == 6):
        fdir = ind[e]
        find = dir[e]

    # Constru????o da "rea????o" (string pronta) e dos "dados" (lista com nomes e produtos das massas molares com coeficientes)
    reacao = ''
    dados = [[], []]  # ??ndice 0: Nome, ??ndice 1: Massa molar; 2: Coeficientes
    for indice in range(0, len(dir[rg])):
        reacao = reacao+f'{"" if fdir * dir[rg][indice][c] == 1 else fdir * dir[rg][indice][c]} {dir[rg][indice][s]} + '
        dados[0].append(dir[rg][indice][n])
        dados[1].append(round(fdir * dir[rg][indice][m] * dir[rg][indice][c], 1))
    for indice in range(0, len(ind[pd])):
        reacao = reacao + f'{"" if find * ind[pd][indice][c] == 1 else find * ind[pd][indice][c]} {ind[pd][indice][s]} + '
        dados[0].append(ind[pd][indice][n])
        dados[1].append(round(find * ind[pd][indice][m] * ind[pd][indice][c], 1))
    reacao = reacao[:-2]+'??? '  # Troca do ??ltimo sinal de soma por seta.
    for indice in range(0, len(dir[pd])):
        reacao = reacao + f'{"" if fdir * dir[pd][indice][c] == 1 else fdir * dir[pd][indice][c]} {dir[pd][indice][s]} + '
        dados[0].append(dir[pd][indice][n])
        dados[1].append(round(fdir * dir[pd][indice][m] * dir[pd][indice][c], 1))
    for indice in range(0, len(ind[rg])):
        reacao = reacao + f'{"" if find * ind[rg][indice][c] == 1 else find * ind[rg][indice][c]} {ind[rg][indice][s]} + '
        dados[0].append(ind[rg][indice][n])
        dados[1].append(round(find * ind[rg][indice][m] * ind[rg][indice][c], 1))
    reacao = reacao[:-3]  # Exclui ??ltimo sinal de soma.

    return reacao, dados


def cadastro_tamanho():
    anions_totais = len(cadastro_anions)
    cations_totais = len(cadastro_cations)
    comb_totais = len(cadastro_prefixo_iupac)+16  # Alcanos e polialcoois de at?? 4 carbonos e 4 hidroxilas
    subst_totais = comb_totais + (len(cadastro_cations)+1)*(len(cadastro_anions)-3)
    print(f'O n??mero de ??nions cadastrados ?? {anions_totais}\n'
          f'O n??mero de c??tions cadastrados ?? {cations_totais}\n'
          f'O n??mero de combust??veis sorte??veis ?? {comb_totais}\n'
          f'O n??mero de subst??ncias/rea????es sorte??veis (combust??o ou salifica????o) ??: {subst_totais}')


class Ion():
    def __init__(self, simbolo, nome, carga, id, massa):
        self._s = simbolo
        self._n = nome
        self._c = carga
        self._id = id
        self._m = massa

    @property
    def s(self):
        return self._s

    @s.setter
    def s(self, s):
        self._s = s

    @property
    def n(self):
        return self._n

    @n.setter
    def n(self, n):
        self._n = n

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c):
        self._c = c

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def m(self):
        return self._m

    @m.setter
    def m(self, m):
        self._m = m


def sorteia_cation():
    from random import randint
    ion = Ion
    ion.id = randint(0, len(cadastro_cations)-1)
    ion.n = cadastro_cations[ion.id][0]
    ion.s = cadastro_cations[ion.id][1]
    ion.c = cadastro_cations[ion.id][2]
    ion.m = cadastro_cations[ion.id][3]
    return [ion.n, ion.s, ion.c, ion.m]


def sorteia_anion():
    from random import randint
    ion = Ion
    ion.id = randint(0, len(cadastro_anions)-1)
    ion.n = cadastro_anions[ion.id][0]
    ion.s = cadastro_anions[ion.id][1]
    ion.c = cadastro_anions[ion.id][2]
    ion.m = cadastro_anions[ion.id][3]
    return [ion.n, ion.s, ion.c, ion.m]


def sorteia_ionico():
    """
    Usa as fun????es sorteia_cation e sorteia_anion para construir um composto i??nico aleat??rio.
    :return: Lista com nome, f??rmula e massa molar do composto.
    """
    anion = sorteia_anion()
    cation = sorteia_cation()
    if anion[2] == cation[2]:  # cargas iguais
        return anion[0] + ' de '+cation[0], cation[1] + anion[1], cation[3]+anion[3]
    else:
        if anion[2] == 1 and cation[2] == 2 or cation[2] == 3 or cation[2] == 4:
            return anion[0] + ' de ' + cation[0], cation[1]+'('+anion[1]+')'+str(cation[2]), \
                   cation[3] + anion[3] * cation[2]
        elif cation[2] == 1 and anion[2] == 2 or anion[2] == 3:
            return anion[0] + ' de ' + cation[0], '(' + cation[1] + ')' + str(anion[2]) + anion[1], \
                   cation[3] * anion[2] + anion[3]
        elif (cation[2] == 2 or cation[2] == 4 and anion[2] == 3) or (cation[2] == 3 and anion[2] == 2):
            return anion[0] + ' de ' + cation[0], \
                   '(' + cation[1] + str(anion[2]) + ')' + '('+anion[1] + ')' + str(cation[2]), \
                   cation[3] * anion[2] + anion[3] * cation[2]


def nomeia_acido(anion):
    if anion.endswith('ato'):
        if anion[len(anion)-5] == 'a':
            ultima = anion[len(anion)-4]
            anion = anion[:-5]
            nome = '??cido ' + anion + '??' + ultima + 'ico'
        elif anion[len(anion)-5] == 'e':
            ultima = anion[len(anion)-4]
            anion = anion[:-5]
            nome = '??cido ' + anion + '??' + ultima + 'ico'
        elif anion[len(anion)-5] == 'i':
            ultima = anion[len(anion)-4]
            anion = anion[:-5]
            nome = '??cido ' + anion + '??' + ultima + 'ico'
        elif anion[len(anion)-5] == 'o':
            ultima = anion[len(anion)-4]
            anion = anion[:-5]
            nome = '??cido ' + anion + '??/??' + ultima + 'ico'
        elif anion[len(anion) - 5] == 'u':
            print(anion)
            ultima = anion[len(anion) - 4]
            anion = anion[:-5]
            nome = '??cido ' + anion + '??' + ultima + 'ico'
        elif anion[len(anion) - 5] not in ['a', 'e', 'i', 'o', 'u']:
            if 'nitr' in anion:
                nome = '??cido n??trico'
            elif 'sulf' in anion:
                anion = anion[:-3]
                nome = '??cido ' + anion + '??rico'
            elif 'fosf' in anion:
                anion = anion[:-3]
                nome = '??cido ' + anion + '??rico'
    elif anion.endswith('eto'):
        anion = anion[:-3]
        nome = '??cido ' + anion + '??drico'
    elif anion.endswith('ito'):
        anion = anion[:-3]
        if 'sulf' in anion:
            nome = '??cido ' + anion + 'uroso'
        elif 'fosf' in anion:
            nome = '??cido ' + anion + 'oroso'
        else:
            nome = '??cido ' + anion + 'oso'
    return nome


def sorteia_acido():
    """
    Usa as fun????o sorteia_anion para construir um composto ??cido inorg??nico aleat??rio.
    :return: Lista com nome, f??rmula e massa molar do ??cido.
    """
    while True:
        anion = sorteia_anion()
        if anion[0] in ('??xido', 'hidr??xido', 'hidreto'):
            continue
        else:
            break
    if anion[2] == 1:  # carga unit??ria
        formula = 'H'+anion[1]
    else:
        formula = 'H' + str(anion[2]) + anion[1]
    massa = anion[2] + anion[3]
    nome = nomeia_acido(anion[0])
    return nome, formula, massa


# REA????ES
def sorteia_salificacao():
    n = 0  # nome
    s = 1  # simbolo
    c = 2  # carga
    m = 3  # massa
    anion = sorteia_anion()
    cation = sorteia_cation()

    # defini????o dos coeficientes
    if anion[c] == 1 or anion[c] == cation[c]:
        coef_base = 1
    else:
        coef_base = anion[c]

    if coef_base == 1 and cation[c] == 1:
        coef_agua = 1
    else:
        coef_agua = cation[c] * coef_base

    if cation[c] == 1 or anion[c] == cation[c]:
        coef_acido = 1
    else:
        coef_acido = cation[c]

    # defini????o das f??rmulas
    if anion[c] == cation[c]:  # F??RMULA DO SAL  |  CORRIGIR PAR??NTESES NO M??TODO I??NICO E PASSAR PARA C??
        formula_sal = cation[1] + anion[1]
    else:
        if anion[c] == 1 and cation[c] == 2 or cation[c] == 3 or cation[c] == 4:
            formula_sal = cation[s]+'('+anion[1]+')'+str(cation[2])
        elif cation[c] == 1 and anion[c] == 2 or anion[c] == 3 or anion[c] == 4:
            formula_sal = '(' + cation[s] + ')' + str(anion[c]) + anion[s]
        elif (cation[c] == 2 or cation[c] == 4 and anion[c] == 3) or (cation[c] == 3 and anion[c] == 2 or anion[c] == 4):
            formula_sal = '(' + cation[s] + str(anion[c]) + ')' + '('+anion[s] + ')' + str(cation[c])

    if anion[c] == 1:  # F??RMULA DO ??CIDO
        formula_acido = 'H' + anion[s]
    else:
        formula_acido = 'H' + str(anion[c]) + anion[s]

    if cation[c] == 1:  # F??RMULA DA BASE
        formula_base = cation[s] + 'OH'
    else:
        formula_base = cation[s] + '(OH)' + str(cation[c])

    # DEFINI????O DOS NOMES
    nome_acido = nomeia_acido(anion[n])
    nome_base = 'hidr??xido de ' + cation[n]
    nome_sal = anion[n] + ' de ' + cation[n]

    # MASSAS
    # acido, base, sal, agua
    massas = (round(anion[m]+anion[c], 1), round(cation[m]+17*cation[c], 1), \
              round(cation[m]*anion[c]+anion[m]*cation[c], 1), 18)

    nomes = (nome_acido, nome_base, nome_sal, '??gua')
    formulas = (formula_acido, formula_base, formula_sal, 'H\u2082O')
    coefs = (coef_acido, coef_base, 1, coef_agua)

    return formulas, nomes, coefs, massas


def sorteia_combustao():
    from random import randint as r
    tipos = ['alcano', 'alcool']
    tipo_sorteado = tipos[r(0, len(tipos) - 1)]
    if tipo_sorteado == 'alcano':
        x = r(1, 20)  # ??ndice do carbono
        formula = f'C{x}H{2*x+2}'
        massas = (12*x+2, 32, 44, 18)
        nome = f'{cadastro_prefixo_iupac[x-1]}ano'
        # rea????o: a comb + b oxig ??? c diox + d agua | indice C: x
        coef_comb = ''
        coef_diox = x
        coef_agua = x+1
        coef_oxig = x + (x+1)/2
        if coef_oxig != int(coef_oxig):  # Coeficiente fracion??rio para g??s oxig??nio
            coef_comb = 2
            coef_diox = coef_diox*2
            coef_agua = coef_agua*2
            coef_oxig = coef_oxig*2
    elif tipo_sorteado == 'alcool':
        x = r(1, 4)  # ??ndice do carbono
        y = r(1, x)  # ??ndice do oxig??nio
        massas = (12*x+2+16*y, 32, 44, 18)
        if y == 1:
            nome = f'{cadastro_prefixo_iupac[x-1]}anol'
            formula = f'C{x}H{2 * x + 2}O'
        else:
            nome = f'{cadastro_prefixo_iupac[x - 1]}ano-{cadastro_prefixo_subst[y-1]}-ol'
            formula = f'C{x}H{2 * x + 2}O{y}'
        coef_comb = ''
        coef_diox = x
        coef_agua = x + 1
        coef_oxig = x + (x+1-y)/2
        if coef_oxig != int(coef_oxig):  # Coeficiente fracion??rio para g??s oxig??nio
            coef_comb = 2
            coef_diox = coef_diox * 2
            coef_agua = coef_agua * 2
            coef_oxig = coef_oxig * 2
    coefs = (1 if coef_comb == '' else 2, int(coef_oxig), coef_diox, coef_agua)
    formulas = (formula, 'O\u2082', 'CO\u2082', 'H\u2082O')
    nomes = (nome, 'oxig??nio', 'di??xido de carbono', '??gua')
    return formulas, nomes, coefs, massas


def monta_reacao(coef, form):
    """
    Retorna a estrutura de uma rea????o qu??mica com base em arrays gerados por m??todos de sorteio de rea????es.
    :param coefs: Array com coeficientes das subst??ncias.
    :param formulas: Array com f??rmulas das subst??ncias.
    :return: string pronta para ser impressa (print()) adequadamente.
    """
    # ??NDICE GERAL DAS TUPLAS (combust??o/salifica????o):
    # 0: combust??vel/??cido   |   1: oxig??nio/base   |   2: di??xido de carbono/sal   |   3: ??gua
    if len(coef) == 4:
        return ('' if coef[0] == 1 else str(coef[0])) + ' ' + form[0] + ' + ' + \
               ('' if coef[1] == 1 else str(coef[1])) + ' ' + form[1] + ' ??? ' + \
               ('' if coef[2] == 1 else str(coef[2])) + ' ' + form[2] + ' + ' + \
               ('' if coef[3] == 1 else str(coef[3])) + ' ' + form[3]
    else:
        print('Formata????o de rea????es com mais ou menos que quatro subst??ncias ainda n??o gerada.')


# GERADOR DE ATIVIDADES
def exercicio_nome_formula():
    from random import randint
    n = int(input('N??mero de atividades: '))
    nf = int(input('Treinar nome (1), f??rmula (2) ou massa molar (3): '))
    if nf == 1:
        print('D?? o nome dos compostos abaixo:')
        gabarito = []
        for c in range(1, n+1):
            caraoucoroa = randint(1, 3)
            if caraoucoroa == 1 or caraoucoroa == 2:
                composto = sorteia_ionico()
            else:
                composto = sorteia_acido()
            gabarito.append(composto[0])
            print(f'{c}) {composto[1]}')
        for indice, resposta in enumerate(gabarito):
            print(f'{indice+1}) {resposta}', end=('.' if indice == len(gabarito)-1 else '; '))

    elif nf == 2:
        print('Escreva a f??rmula dos compostos abaixo:')
        gabarito = []
        for c in range(1, n+1):
            composto = sorteia_ionico()
            gabarito.append(composto[1])
            print(f'{c}) {composto[0]}')
        for indice, resposta in enumerate(gabarito):
            print(f'{indice+1}) {resposta}', end=('.' if indice == len(gabarito)-1 else '; '))

    elif nf == 3:
        print('Calcula a massa molar dos compostos abaixo:')
        gabarito = []
        for c in range(1, n + 1):
            composto = sorteia_ionico()
            gabarito.append(round(composto[2], 1))
            print(f'{c}) {composto[1]}')
        for indice, resposta in enumerate(gabarito):
            print(f'{indice+1}) {resposta}', end=('.' if indice == len(gabarito)-1 else '; '))


def dados_estequiometria():
    """
    Sorteia o tipo de rea????o entre salifica????o e combust??o para gerar dados a um exerc??cio t??pico de
    estequiometria (f??rmulas, nomes, rea????o e massas molares).
    :return: lista dos dados dos reagentes e produtos (tuplas na ordem: f??rmulas, nomes, coeficientes e massas molares)
    e rea????o montada pela fun????o monta_reacao.
    """
    from random import randint
    sorteio = randint(1, 3)
    if sorteio in (1, 2):
        # PADR??O DOS ??NDICES DE RETORNO DAS FUN????ES SALIFICA????O E COMBUST??O:
        # ??NDICE GERAL DO RETORNO:
        # 0: f??rmula/s   |   1: nome/s   |   2: coeficientes   |   3: massas molares
        if sorteio == 1:  # SALIFICA????O
            reacao = sorteia_salificacao()
        elif sorteio == 2:  # COMBUST??O
            reacao = sorteia_combustao()
        return reacao[0], reacao[1], reacao[2], reacao[3], monta_reacao(reacao[2], reacao[0])
    elif sorteio == 3:
        return sorteia_redox()


def exerc_esteq(formula_oculta=True):
    """
    Gera exerc??cio de estequiometria com base em dados gerados pela fun????o dados_estequiometria.
    :param formula_oculta: Oculta (True como default) f??rmula qu??mica entre par??nteses logo ap??s nome das subst??ncias
    citadas.
    :return: Arquivo .txt com n exerc??cios com gabarito ao final.
    """
    # PADR??O DOS ??NDICES DE RETORNO DAS FUN????ES:
    # ??NDICE GERAL DO RETORNO:
    # 0: f??rmula/s   |   1: nome/s   |   2: coeficientes   |   3: massas molares
    # ??NDICE GERAL DAS TUPLAS:
    # 0: combust??vel/??cido   |   1: oxig??nio/base   |   2: di??xido de carbono/sal   |   3: ??gua
    from random import randint
    contador = 0
    gabarito = []
    while True:
        quantidade = int(input('Insira o n??mero de exerc??cios desejados: '))
        if isinstance(quantidade, int) is True and quantidade > 0:
            break
        else:
            print(f'\033[31mInsira um valor num??rico, inteiro e n??o nulo!\033[m')
            continue

    with open('exerc_mru.txt', 'w'): pass

    while True:
        # Sorteios:
        dados = dados_estequiometria()  # Sorteio da rea????o
        if len(dados) == 5:  # Salifica????o ou combust??o
            ip = randint(0, 3)  # Sorteio do ??ndice da subst??ncia com dado inc??gnito (problema)
            mid = randint(2, 500)  # Sorteio da massa da subst??ncia com dado informado
            while True:
                id = randint(0, 3)  # Sorteio do ??ndice da subst??ncia com dado conhecido
                if id == ip:
                    continue
                else:
                    break
            contador += 1
            with open('exerc_esteq.txt', 'a', encoding="utf-8") as arquivo:
                if formula_oculta:
                    exercicio = f'Sabendo que {mid} g de {dados[1][id]} s??o {"consumidos" if id <= 1 else "produzidos"} na rea????o\n'+\
                                f'{dados[4].center(40)} \ncalcula a massa de {dados[1][ip]} {"consumida" if ip <= 1 else "produzida"}.\n'
                else:
                    exercicio = f'Sabendo que {mid} g de {dados[1][id]} ({dados[0][id]}) s??o {"consumidos" if id <= 1 else "produzidos"} na rea????o\n'+\
                                f'{dados[4].center(40)} \ncalcula a massa de {dados[1][ip]} ({dados[0][ip]}) {"consumida" if ip <= 1 else "produzida"}.\n'
                arquivo.write(str(contador) + ') ' + exercicio)
                gabarito.append(str(round(mid * (dados[2][ip] * dados[3][ip]) / (dados[2][id] * dados[3][id]), 1)) + ' g')
            if contador == quantidade:
                break
        else:
            ip = randint(0, len(dados[1][0])-1)  # Sorteio do ??ndice da subst??ncia com dado inc??gnito (problema)
            mid = randint(2, 500)  # Sorteio da massa da subst??ncia com dado informado
            while True:
                id = randint(0, len(dados[1][0])-1)  # Sorteio do ??ndice da subst??ncia com dado conhecido
                if id == ip:
                    continue
                else:
                    break
            contador += 1
            with open('exerc_esteq.txt', 'a', encoding="utf-8") as arquivo:
                if formula_oculta:
                    exercicio = f'Sabendo que {mid} g de {dados[1][0][id]} s??o {"consumidos" if id <= 1 else "produzidos"} na rea????o\n' + \
                                f'{dados[0].center(40)} \ncalcula a massa de {dados[1][0][ip]} {"consumida" if ip <= 1 else "produzida"}.\n'
                else:
                    pass
                arquivo.write(str(contador) + ') ' + exercicio)
                gabarito.append(
                    str(round(mid * dados[1][1][ip] / dados[1][1][id], 1)) + ' g')
            if contador == quantidade:
                break
    with open('exerc_esteq.txt', 'a') as arquivo:
        for indice in range(0, len(gabarito)):
            arquivo.write(str(indice+1)+') ' + str(gabarito[indice]) +
                          ('.' if indice == (len(gabarito) - 1) else '; ') +
                          ('\n' if (indice+1) % 5 == 0 else ''))
