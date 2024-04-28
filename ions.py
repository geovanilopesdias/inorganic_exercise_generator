from enum import Enum
from random import choice


class Ion():
    # Índices subscritos em unicode de 2 a 8
    i = ['', '', u'\u2082', u'\u2083', u'\u2084', u'\u2085' , u'\u2086', u'\u2087', '\u2088']

    def __init__(self, n, s, c, m):
        self.name = n
        self.symbol = s
        self.charge = c
        self.molar_mass = m


    @staticmethod
    def random_ion(an_anion=True):
        if an_anion:
            return choice(list(AnionTable)).value
        else:
            return choice(list(CationTable)).value


    def is_atomic(self):
        return len(self.symbol) == 1 or (len(self.symbol) == 2 and self.symbol.istitle())


    @staticmethod
    def get_base_formula(cation):
        i = Ion.i  # Lista de Índices subscritos unicode pra fórmulas químicas
        return f'{cation.symbol}OH' if cation.charge == 1 else f'{cation.symbol}(OH){i[cation.charge]}'


    @staticmethod
    def get_acid_formula(anion):
        i = Ion.i  # Lista de Índices subscritos unicode pra fórmulas químicas
        if anion.symbol[0] == 'H' and anion.symbol[1] not in i:  # Ânions que começam com 'H'
            return f'H{i[anion.charge+1]}{anion.symbol}'
        elif anion.symbol[0] == 'H' and anion.symbol[1] in i:    # Ânions que começam com 'H2' etc.
            return f'H{i[anion.charge+i.index(anion.symbol[1])]}{anion.symbol}'
        else:
            return f'H{anion.symbol}' if anion.charge == 1 else f'H{i[anion.charge]}{anion.symbol}'
        

    @staticmethod
    def get_salt_formula(cation, anion):
        i = Ion.i  # Lista de Índices subscritos unicode pra fórmulas químicas
        if cation.charge == anion.charge:
            return cation.symbol+anion.symbol

        elif cation.charge/anion.charge in (.5, 2):
            if cation.charge > anion.charge:
                cation_part = cation.symbol
                anion_part = anion.symbol+Ion.i[cation.charge] if anion.is_atomic() else f'({anion.symbol})'+i[cation.charge]
            else:
                anion_part = anion.symbol
                cation_part = cation.symbol+Ion.i[anion.charge] if cation.is_atomic() else f'({cation.symbol})'+i[anion.charge]

        else:
            anion_part = anion.symbol+Ion.i[cation.charge] if anion.is_atomic() else f'({anion.symbol})'+i[cation.charge]
            cation_part = cation.symbol+Ion.i[anion.charge] if cation.is_atomic() else f'({cation.symbol})'+i[anion.charge]

        return cation_part+anion_part


    @staticmethod
    def salt_name(cation, anion):
        pass


    @staticmethod
    def acid_name(anion):
        if anion.endswith('ato'):
            if anion[len(anion)-5] == 'a':
                ultima = anion[len(anion)-4]
                anion = anion[:-5]
                nome = 'ácido ' + anion + 'â' + ultima + 'ico'
            elif anion[len(anion)-5] == 'e':
                ultima = anion[len(anion)-4]
                anion = anion[:-5]
                nome = 'ácido ' + anion + 'é' + ultima + 'ico'
            elif anion[len(anion)-5] == 'i':
                ultima = anion[len(anion)-4]
                anion = anion[:-5]
                nome = 'ácido ' + anion + 'í' + ultima + 'ico'
            elif anion[len(anion)-5] == 'o':
                ultima = anion[len(anion)-4]
                anion = anion[:-5]
                nome = 'ácido ' + anion + 'ô/ó' + ultima + 'ico'
            elif anion[len(anion) - 5] == 'u':
                print(anion)
                ultima = anion[len(anion) - 4]
                anion = anion[:-5]
                nome = 'ácido ' + anion + 'ú' + ultima + 'ico'
            elif anion[len(anion) - 5] not in ['a', 'e', 'i', 'o', 'u']:
                if 'nitr' in anion:
                    nome = 'ácido nítrico'
                elif 'sulf' in anion:
                    anion = anion[:-3]
                    nome = 'ácido ' + anion + 'úrico'
                elif 'fosf' in anion:
                    anion = anion[:-3]
                    nome = 'ácido ' + anion + 'órico'
                else:
                    pass
            else:
                pass
        elif anion.endswith('eto'):
            anion = anion[:-3]
            nome = 'ácido ' + anion + 'ídrico'
        elif anion.endswith('ito'):
            anion = anion[:-3]
            if 'sulf' in anion:
                nome = 'ácido ' + anion + 'uroso'
            elif 'fosf' in anion:
                nome = 'ácido ' + anion + 'oroso'
            else:
                nome = 'ácido ' + anion + 'oso'
        return nome


    def __str__(self):
        return f'{self.name} ({self.symbol}) | Charge: {self.charge}; Mass: {self.molar_mass}'



class AnionTable(Enum):    
    fluoride = Ion('fluoreto', 'F', 1, 19)
    chloride = Ion('cloreto', 'Cl', 1, 35.5)
    bromide = Ion('brometo', 'Br', 1, 79.9)
    iodite = Ion('iodeto', 'I', 1, 126.9)
    hypochlorite = Ion('hipoclorito', 'ClO', 1, 51.5)
    chlorite = Ion('clorito', 'ClO'+Ion.i[2], 1, 67.5)
    chlorate = Ion('clorato', 'ClO'+Ion.i[3], 1, 83.5)
    perchlorate = Ion('perclorato', 'ClO'+Ion.i[4], 1, 99.5)
    hypobromite = Ion('hipobromito', 'BrO', 1, 95.9)
    bromate = Ion('bromato', 'BrO'+Ion.i[3], 1, 127.9)
    hypoiodite = Ion('hipoiodito', 'IO', 1, 142.9)
    iodate = Ion('iodato', 'IO'+Ion.i[3], 1, 174.9)
    periodate = Ion('periodato', 'IO'+Ion.i[4], 1, 190.9)
    cyanide = Ion('cianeto', 'CN', 1, 26)
    cyanate = Ion('cianato', 'CNO', 1, 42)
    thiocyanate = Ion('tiocianato', 'CNS', 1, 58.1)
    acetate = Ion('acetato', 'C'+Ion.i[2]+'H'+Ion.i[3]+'O'+Ion.i[2], 1, 59)
    carbonate = Ion('carbonato', 'CO'+Ion.i[3], 1, 60)
    ferricyanide = Ion('ferricianeto', 'Fe(CN)'+Ion.i[6], 3, 211.8)
    ferrocyanide = Ion('ferrocianeto', 'Fe(CN)'+Ion.i[6], 4, 211.8)
    nitrite = Ion('nitrito', 'NO'+Ion.i[2], 1, 46)
    nitrate = Ion('nitrato', 'NO'+Ion.i[3], 1, 62)
    nitride = Ion('nitreto', 'N'+Ion.i[3], 1, 42)
    methaphospate = Ion('metafosfato', 'PO'+Ion.i[3], 1, 79)
    hypophosphite = Ion('hipofosfito', 'H'+Ion.i[2]+'PO'+Ion.i[2], 1, 65)
    phosphite = Ion('fosfito', 'HPO'+Ion.i[3], 2, 80)
    phosphate = Ion('fosfato', 'PO'+Ion.i[4], 3, 95)
    phosphide = Ion('fosfeto', 'P'+Ion.i[3], 3, 93)
    pyrophosphate = Ion('pirofosfato', 'P'+Ion.i[2]+'O'+Ion.i[7], 4, 174)
    hypophosphate = Ion('hipofosfato', 'P'+Ion.i[2]+'O', 4, 78)
    sulphide = Ion('sulfeto', 'S', 2, 32.1)
    sulphite = Ion('sulfito', 'SO'+Ion.i[3], 2, 80.1)
    sulphate = Ion('sulfato', 'SO'+Ion.i[4], 2, 96.1)
    thiosulphate = Ion('tiossulfato', 'S'+Ion.i[2]+'O'+Ion.i[3], 2, 112.2)
    hyposulphite = Ion('hipossulfito', 'S'+Ion.i[2]+'O'+Ion.i[4], 2, 128.2)
    persulphate = Ion('persulfato', 'S'+Ion.i[2]+'O'+Ion.i[8], 2, 192.2)
    tetrathionate = Ion('tetrationato', 'S'+Ion.i[4]+'O'+Ion.i[6], 2, 224)
    permanganate = Ion('permanganato', 'MnO'+Ion.i[4], 1, 118.9)
    manganate = Ion('manganato', 'MnO'+Ion.i[4], 2, 118.9)
    manganite = Ion('manganito', 'MnO'+Ion.i[3], 2, 102.9)
    #hydroxide = Ion('hidróxido', 'OH', 1, 17)
    #oxide = Ion('óxido', 'O', 2, 16)
    #hydride = Ion('hidreto', 'H', 1, 1)
    chromate = Ion('cromato', 'CrO'+Ion.i[4], 2, 116) 
    dichromate = Ion('dicromato', 'Cr'+Ion.i[2]+'O'+Ion.i[7], 2, 216)
    arsenite = Ion('arsenito', 'AsO'+Ion.i[3], 3, 74.9)
    arsenate = Ion('arsenato', 'AsO'+Ion.i[4], 3, 138.9)
    arsenide = Ion('arsenieto', 'As', 3, 122.9)
    borate = Ion('borato', 'BO'+Ion.i[3], 3, 58.8)



class CationTable(Enum):
    lithium = Ion('litio', 'Li', 1, 9.4)
    sodium = Ion('sódio', 'Na', 1, 23)
    potassium = Ion('potássio', 'K', 1, 39.1)
    rubidium = Ion('rubídio', 'Rb', 1, 85.8)
    cesium = Ion('césio', 'Cs', 1, 132.9)
    silver = Ion('prata', 'Ag', 1, 107.9)
    copper1 = Ion('cobre I', 'Cu', 1, 63.5)
    gold1 = Ion('ouro I', 'Au', 1, 197)
    ammonium = Ion('amônio', u'NH\u2084', 1, 18)
    beryllium = Ion('berílio', 'Be', 2, 9)
    magnesium = Ion('magnésio', 'Mg', 2, 24.3)
    calcium = Ion('cálcio', 'Ca', 2, 40)
    strontium = Ion('estrôncio', 'Sr', 2, 87.6)
    barium = Ion('bário', 'Ba', 2, 137.3)
    radium = Ion('rádio', 'Ra', 2, 226)
    zinc = Ion('zinco', 'Zn', 2, 65.4)
    cadmium = Ion('cádmio', 'Cd', 2, 112.4)
    copper2 = Ion('cobre II', 'Cu', 2, 63.5)
    quicksilver2 = Ion('mercúrio II', 'Hg', 2, 200.6)
    iron2 = Ion('ferro II', 'Fe', 2, 55.8)
    cobalt2 = Ion('cobalto II', 'Co', 2, 58.9)
    nickel2 = Ion('níquel II', 'Ni', 2, 58.7)
    chromium2 = Ion('cromo II', 'Cr', 2, 52)
    manganese2 = Ion('manganês II', 'Mn', 2, 54.9)
    tin2 = Ion('estanho II', 'Sn', 2, 118.7)
    lead2 = Ion('chumbo II', 'Pb', 2, 207.2)
    titanium2 = Ion('titânio II', 'Ti', 2, 47.9)
    platinum2 = Ion('platina II', 'Pt', 2, 195)
    aluminium = Ion('alumínio', 'Al', 3, 27)
    bismuth = Ion('bismuto', 'Bi', 3, 209)
    gold3 = Ion('ouro III', 'Au', 3, 197)
    iron3 = Ion('ferro III', 'Fe', 3, 55.8)
    cobalt3 = Ion('cobalto III', 'Co', 3, 58.9)
    nickel3 = Ion('níquel III', 'Ni', 3, 58.7)
    chromium3 = Ion('cromo III', 'Cr', 3, 52)
    tin4= Ion('estanho IV', 'Sn', 4, 118.7)
    titanium4 = Ion('titânio IV', 'Ti', 4, 47.9)
    lead4 = Ion('chumbo IV', 'Pb', 4, 207.2)
    platinum4 = Ion('platina IV', 'Pt', 4, 195)
    manganese4 = Ion('manganês IV', 'Mn', 4, 54.9)

