from enum import Enum
from elements import Element, PeriodicTable
from inorganics import *
from fuels import OrganicFuel


class ChemicalEquation():
    def __init__(self, r, p, eqb = False, etp = None):
        self.reactants = r
        self.products = p
        self.is_equilibrium = eqb
        self.enthalpy = etp


    class Reactions(Enum):
        NEUTRALIZATION = {"method": 'random_neutralization', "name": 'neutralização'}
        COMBUSTION = {"method": 'random_combustion', "name": 'combustão'}
    
    
    @staticmethod
    def random_reaction():
        return getattr(__class__, choice(list(__class__.Reactions)).value["method"])()


    @staticmethod
    def random_neutralization():
        ANION = random_anion_for_acid()
        CATION = random_cation()

        # Coeficientes dos ácidos, base e água:
        ac = 1 if ANION.charge == CATION.charge else CATION.charge
        bc = 1 if ANION.charge == CATION.charge else ANION.charge
        wc = CATION.charge * bc

        # Instâncias das substâncias da neutralização:
        acid = ChemicalEquationSubstance(
            get_acid_formula(ANION),
            StatesOfMatter.AQUEOUS.value,
            m = ANION.molar_mass + ANION.charge,
            c = ac)
        base = ChemicalEquationSubstance(
            get_base_formula(CATION),
            StatesOfMatter.SOLID.value,
            m = CATION.molar_mass + CATION.charge * 17,  # 17 is the hidroxide molar mass
            c = bc)
        salt = ChemicalEquationSubstance(
            get_salt_formula(CATION, ANION),
            StatesOfMatter.AQUEOUS.value,
            m = ANION.molar_mass * CATION.charge + CATION.molar_mass * ANION.charge)
        water = ChemicalEquationSubstance(
            'H\u2082O',
            StatesOfMatter.LIQUID.value,
            m = 18,  # Molar mass of water
            c = wc)
        return ChemicalEquation(r = (acid, base), p = (salt, water))


    def _set_combustion_coefficients(fuel):
        c = Element.get_element_index(PeriodicTable.CARBON, fuel.atoms)
        h = Element.get_element_index(PeriodicTable.HYDROGEN, fuel.atoms)
        o = Element.get_element_index(PeriodicTable.OXYGEN, fuel.atoms)
        if o is None:
            o = 0
            
        if (c % 2 == 0 and o == 1):
            fc = 1
        elif (c % 2 != 0 and o == 0) or (c % 2 == 0 and o in (0, 2)) or (c % 2 == 0 and o == 1 and h/c == 2):
            fc = 2
        else:
            fc = 4
        return {"fuel": fc,
                "carbon dioxide": fc * c,
                "water": int(.5 * fc * h),
                "oxygen": int(.5 * ((.5 * fc * h) + (2 * fc * c) - (fc * o)))}
    

    @staticmethod
    def random_combustion():
        CARBON_DIOXIDE_ENTHALPY = 394
        WATER_ENTHALPY = 286        
        ORG_FUEL = OrganicFuel.random_fuel()
        coefficients = __class__._set_combustion_coefficients(ORG_FUEL)

        # Instâhydrogens_in_fuelias das substâncias da combustão:
        fuel = ChemicalEquationSubstance(
            ORG_FUEL.formula,
            '',  # Implementar estados físicos devidamente para diferentes funções orgânicas
            m = ORG_FUEL.molar_mass,
            c = coefficients["fuel"])
        carbon_dioxide = ChemicalEquationSubstance(
            'CO\u2082',
            StatesOfMatter.GAS.value,
            m = 44,
            c = coefficients["carbon dioxide"])
        water = ChemicalEquationSubstance(
            'H\u2082O',
            StatesOfMatter.LIQUID.value,
            m = 18,  # Molar mass of water
            c = coefficients["water"])
        oxygen = ChemicalEquationSubstance(
            'O\u2082',
            StatesOfMatter.GAS.value,
            m = 32,  # Molar mass of oxygen gas
            c = coefficients["oxygen"])  # All water and CO2 oxygens come from oxygen gas or the fuel

        enthalpy = ORG_FUEL.enthalpy * coefficients["fuel"] - CARBON_DIOXIDE_ENTHALPY * coefficients["carbon dioxide"] - WATER_ENTHALPY * coefficients["water"]
        return ChemicalEquation(r = (fuel, oxygen), p = (carbon_dioxide, water), etp = enthalpy)


    def __str__(self):
        reactants_str = ' + '.join([str(r) for r in self.reactants])
        products_str = ' + '.join([str(p) for p in self.products])
        arrow = '\u2192' if not self.is_equilibrium else '\u2194'

        if self.enthalpy is None:
            return f'{reactants_str} {arrow} {products_str}'
        else:
            return f'{reactants_str} {arrow} {products_str} \u0394H\u2080 = -{self.enthalpy} kJ'



class StatesOfMatter(Enum):
    SOLID = u'\u208D\u209B\u208E'
    LIQUID = u'\u208D\u2097\u208E'
    GAS = u'\u208D\u2099\u208E'
    AQUEOUS = u'\u208D\u2090\u208E'



class ChemicalEquationSubstance():
    def __init__(self, f, sm, m, c = 1):
        self.coefficient = c
        self.formula = f
        self.molar_mass = m
        self.state_of_matter = sm


    def __str__(self):
        if self.coefficient > 1:
            return str(self.coefficient) + ' ' + self.formula + self.state_of_matter
        else:
            return self.formula
        


class RedoxSemiReaction():
    pass  # Implementar módulo ionstable



class RedoxTable(Enum):
    pass


## Transformar para a classe RedoxTable acima:
# Índices do cadastro redox:

# 0: Lista com reagentes cadastros em sublistas (0: símbolo, 1: coeficiente, 2: nome, 3: massa molar)
# 1: Lista com produtos cadastros em sublistas (0: símbolo, 1: coeficiente, 2: nome, 3: massa molar)
# 2: potencial-padrão de redução (25 ºC)
# 3: número de elétrons da redução
# Exemplos:
# cadastro_redox[0][2] → Potencial-padrão (E) da primeira semireação
# cadastro_redox[0][0] → Lista de reagentes da primeira semireação
# cadastro_redox[0][0][0] → Lista de dados do primeiro reagente da primeira semireação
# cadastro_redox[0][0][0][0] → Símbolo do primeiro reagente da primeira semireação

cadastro_redox = [[[['F\u2082', 1, 'flúor', 19]], [['F\u207B', 2, 'íon fluoreto', 19]], 2.87, 2],
                  [[['O\u2083', 1, 'ozônio', 48], ['H\u207A', 2, 'íon hidrogênio', 1]], [['O\u2082', 1, 'oxigênio', 32], ['H\u2082', 1, 'água', 18]], 2.07, 2],
                  [[['Co\u00B3\u207A', 1, 'íon cobalto III', 58.9]], [['Co\u00B2\u207A', 1, 'íon cobalto II', 58.9]], 1.82, 1],
                  [[['H\u2082O\u2082', 1, 'peróxido de hidrogênio', 19], ['H\u207A', 2, 'íon hidrogênio', 1]], [['H\u2082O', 2, 'água', 18]], 1.77, 2],
                  [[['MnO\u2084\u207B', 1, 'íon manganato', 188.9], ['H\u207A', 8, 'íon hidrogênio', 1]], [['Mn 2\u207A', 1, 'íon manganês', 54.9], ['H\u2082O', 4, 'água', 18]], 1.51, 5],
                  [[['Au\u00B3\u207A', 1, 'íon ouro III', 197]], [['Au', 1, 'ouro', 197]], 1.5, 3],
                  [[['Cl\u2082', 1, 'cloro', 71]], [['Cl\u207B', 2, 'íon cloreto', 35.5]], 1.36, 2],
                  [[['(Cr\u2082O\u2087)\u00B2\u207B', 1, 'íon dicromato', 216], ['H\u207A', 14, 'íon hidrogênio', 1]], [['Cr\u00B3\u207A', 2, 'íon cromo III', 52], ['H\u2082O', 7, 'água', 18]], 1.33, 6],
                  [[['MnO\u2082', 1, 'óxido de manganês IV', 86.9], ['H\u207A', 4, 'íon hidrogênio', 1]], [['Mn 2\u207A', 1, 'íon manganês II', 54.9], ['H\u2082O', 2, 'água', 18]], 1.232, 2],
                  [[['O\u2082', 1, 'oxigênio', 32], ['H\u207A', 4, 'íon hidrogênio', 1]], [['H\u2082O', 2, 'água', 18]], 1.231, 4],
                  [[['Br\u2082', 1, 'bromo', 79.9]], [['Br\u207B', 2, 'íon brometo', 79.9]], 1.07, 2],
                  [[['(NO\u2083)\u207B', 1, 'íon nitrato', 62], ['H\u207A', 4, 'íon hidrogênio', 1]], [['NO', 1, 'monóxido de nitrogênio', 30], ['H\u2082O', 2, 'água', 18]], 0.96, 3],
                  [[['Ag\u207A', 1, 'íon prata', 107.9]], [['Ag', 1, 'prata', 107.9]], 0.8, 1],
                  [[['Fe\u00B3\u207A', 1, 'íon ferro III', 55.8]], [['Fe\u00B2\u207A', 1, 'íon ferro II', 55.8]], 0.77, 1],
                  [[['O\u2082', 1, 'oxigênio', 32], ['H\u207A', 2, 'íon hidrogênio', 1]], [['H\u2082O\u2082', 2, 'peróxido de hidrogênio', 19]], 0.68, 2],
                  # [[['MnO\u2084 -', 1, 'óxido de manganês IV'], ['H\u2082O', 2, 'água']], [['MnO\u2082', 1, 'óxido de manganês IV'], ['HO\u207B', 4, 'íon hidróxido']], 0.59, 3],
                  [[['I\u2082', 1, 'iodo', 253.8]], [['I -', 2, 'íon iodeto', 126.9]], 0.53, 2],
                  [[['O\u2082', 1, 'oxigênio', 32], ['H\u2082O', 2, 'água', 18]], [['HO\u207B', 4, 'íon hidróxido', 17]], 0.4, 4],
                  [[['Cu\u00B2\u207A', 1, 'íon cobre II', 63.5]], [['Cu', 1, 'cobre', 63.5]], 0.34, 2],
                  [[['AgCl', 1, 'cloreto de prata', 143.4]], [['Ag', 1, 'prata', 107.9], ['Cl\u207B', 1, 'íon cloreto', 35.5]], 0.22, 1],
                  [[['(SO\u2084)\u00B2\u207B', 1, 'íon sulfato', 96.2], ['H\u207A', 4, 'íon hidrogênio', 1]], [['SO\u2082', 1, 'dióxido de enxofre', 64.1], ['H\u2082O', 2, 'água', 18]], 0.2, 2],
                  [[['Cu\u00B2\u207A', 1, 'íon cobre II', 63.5]], [['Cu\u207A', 1, 'íon cobre I', 63.5]], 0.15, 1],
                  [[['Sn\u2074\u207A', 1, 'íon estanho IV', 118.7]], [['Sn\u00B2\u207A', 1, 'íon estanho II', 118.7]], 0.13, 2],
                  [[['H\u207A', 2, 'íon hidrogênio', 1]], [['H\u2082', 1, 'hidrogênio', 2]], 0, 2],
                  [[['Pb\u00B2\u207A', 1, 'íon chumbo II', 207.2]], [['Pb', 1, 'chumbo', 207.2]], -0.13, 2],
                  [[['Sn\u00B2\u207A', 1, 'íon estanho II', 118.7]], [['Sn', 1, 'estanho', 118.7]], -0.14, 2],
                  [[['Ni\u00B2\u207A', 1, 'íon níquel II', 58.7]], [['Ni', 1, 'níquel', 58.7]], -0.25, 2],
                  [[['Co\u00B2\u207A', 1, 'íon cobalto II', 58.9]], [['Co', 1, 'cobalto', 58.9]], -0.28, 2],
                  [[['PbSO\u2084', 1, 'sulfato de chumbo II', 303.2]], [['Pb', 1, 'chumbo', 207.2], ['(SO\u2084)\u00B2\u207B', 1, 'íon sulfato', 96]], -0.31, 2],
                  [[['Cd\u00B2\u207A', 1, 'íon cádmio II', 112.4]], [['Cd', 1, 'cádmio', 112.4]], -0.40, 2],
                  [[['Fe\u00B2\u207A', 1, 'íon ferro II', 55.8]], [['Fe', 1, 'ferro', 55.8]], -0.44, 2],
                  [[['Cr\u00B3\u207A', 1, 'íon cromo III', 52]], [['Cr', 1, 'cromo', 52]], -0.74, 3],
                  [[['Zn\u00B2\u207A', 1, 'íon zinco', 65.4]], [['Zn', 1, 'zinco', 65.4]], -0.76, 2],
                  # [[['H\u2082', 2, 'hidrogênio', 2]], [['H\u2082', 1, 'hidrogênio'], ['HO -', 2, 'íon hidróxido', 17]], -0.83, 2],
                  [[['Mn\u00B2\u207A', 1, 'íon manganês II', 54.9]], [['Mn', 1, 'manganês', 54.9]], -1.18, 2],
                  [[['Al\u00B3\u207A', 1, 'íon alumínio', 27]], [['Al', 1, 'alumínio', 27]], -1.66, 3],
                  [[['Be\u00B2\u207A', 1, 'íon berílio', 9]], [['Be', 1, 'berílio', 9]], -1.85, 2],
                  [[['Mg\u00B2\u207A', 1, 'íon magnésio', 24.3]], [['Mg', 1, 'magnésio', 24.3]], -2.37, 2],
                  [[['Na\u207A', 1, 'íon sódio', 23]], [['Na', 1, 'sódio', 23]], -2.71, 1],
                  [[['Ca\u00B2\u207A', 1, 'íon cálcio', 40.1]], [['Ca', 1, 'cálcio', 40.1]], -2.87, 2],
                  [[['Sr\u00B2\u207A', 1, 'íon estrôncio', 87.6]], [['Sr', 1, 'estrôncio', 87.6]], -2.89, 2],
                  [[['Ba\u00B2\u207A', 1, 'íon bário', 137.3]], [['Ba', 1, 'bário', 137.3]], -2.90, 2],
                  [[['K\u207A', 1, 'íon potássio', 39.1]], [['K', 1, 'potássio', 39.1]], -2.93, 1],
                  [[['Li\u207A', 1, 'íon lítio', 6.9]], [['Li', 1, 'lítio', 6.9]], -3.05, 1]]

