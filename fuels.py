from elements import *
from enum import Enum
from random import randint, choice


class FuelFunction(Enum):
    ALKANE = 'alcano'
    ALKENE = 'alceno'
    ALKINE = 'alcino'
    ALCOHOL = 'álcool'
    #KETONE = 'cetona'
    #ETHER = 'éter'
    #ALDEHYDE = 'aldeído'
    #CARBOX = 'ácido carboxílico'



class OrganicFuel():
    # Índices subscritos em unicode de 2 a 8
    C_PREFIX = ['', 'met', 'et', 'prop', 'but', 'pent', 'hex', 'hept', 'oct', 'non', 'dec']
    ## C_SPECIAL_RADICALS = ['vinil', 'isopropil', 'isobutil', 'isopentil']

    
    def __init__(self, n, a, b, fc):
        self.name = n
        self.atoms = a
        self.bonds = b
        self.function = fc
        self.formula = self.set_formula()
        self.enthalpy = self.set_enthalpy()
        self.molar_mass = self.set_molar_mass()


    def set_enthalpy(self):
        return sum(bond["bond"].get_bond_energy() * bond["quantity"] for bond in self.bonds)


    def set_molar_mass(self):
        return sum(atom["element"].get_molar_mass() * atom["quantity"] for atom in self.atoms)


    def set_formula(self):
        return ''.join([f'{atom["element"].get_symbol()}{self.set_index(atom["quantity"])}' for atom in self.atoms])


    def __str__(self):
        return f'{self.name.title()} ({self.formula}) é um {self.function.value};\nEntalpia: {self.enthalpy} kJ/mol; Massa molar: {self.molar_mass} g/mol.'


    @staticmethod
    def set_index(number):
        if type(number) is not int:
            raise TypeError('Número de átomos deve ser um inteiro')
        if number < 1:
            raise ValueError('Número de átomos deve ser superior à 1')
        
        UNICODE_ALGARISMS = [u'\u2080', u'\u2081', u'\u2082', u'\u2083', u'\u2084', u'\u2085' , u'\u2086', u'\u2087', '\u2088', '\u2089']
        return ''.join([UNICODE_ALGARISMS[int(digit)] for digit in str(number)]) if number > 1 else ''


    @staticmethod
    def test_function_building_arguments(c, p = 0, insaturated = False):
        if type(c) is not int or type(p) is not int:
            raise TypeError('Número de carbonos e posição da insaturação devem ser inteiros.')
        if insaturated:
            if c < 2:
                raise ValueError('Número de carbonos deve ser superior à 2')
        else:
            if c < 1:
                raise ValueError('Número de carbonos deve ser superior à 1')
        if c > 10:
            raise ValueError('Função não implementada para funções acima de 10 carbonos')
        if c > 3 and p > (c/2):
            raise ValueError('Posição da insaturação fixada em local inadequado')

    
    @staticmethod
    def alkane(c):
        OrganicFuel.test_function_building_arguments(c)
        return OrganicFuel(f'{OrganicFuel.C_PREFIX[c]}ano',
                            [{"element": PeriodicTable.CARBON, "quantity": c}, {"element": PeriodicTable.HYDROGEN, "quantity": (2 * c + 2)}],
                            [{"bond": BondEnergyTable.CARBON_S, "quantity": (c-1)}, {"bond": BondEnergyTable.CARBON_HYDROGEN, "quantity": (2 * c + 2)}],
                            FuelFunction.ALKANE)


    @staticmethod
    def alkene(c, p = 0):
        OrganicFuel.test_function_building_arguments(c, p, True)
        name = f'{OrganicFuel.C_PREFIX[c]}eno' if c < 3 else f'{OrganicFuel.C_PREFIX[c]}-{p}-eno'
        return OrganicFuel(name,
                            [{"element": PeriodicTable.CARBON, "quantity": c}, {"element": PeriodicTable.HYDROGEN, "quantity": (2 * c)}],
                            [{"bond": BondEnergyTable.CARBON_S, "quantity": (c-2)},
                             {"bond": BondEnergyTable.CARBON_D, "quantity": 1},
                             {"bond": BondEnergyTable.CARBON_HYDROGEN, "quantity": (2 * c)}],
                            FuelFunction.ALKENE)


    @staticmethod
    def alkine(c, p = 0):
        OrganicFuel.test_function_building_arguments(c, p, True)
        name = f'{OrganicFuel.C_PREFIX[c]}ino' if c < 3 else f'{OrganicFuel.C_PREFIX[c]}-{p}-ino'
        return OrganicFuel(name,
                            [{"element": PeriodicTable.CARBON, "quantity": c}, {"element": PeriodicTable.HYDROGEN, "quantity": (2 * c - 2)}],
                            [{"bond": BondEnergyTable.CARBON_S, "quantity": (c-2)},
                             {"bond": BondEnergyTable.CARBON_T, "quantity": 1},
                             {"bond": BondEnergyTable.CARBON_HYDROGEN, "quantity": (2 * c - 2)}],
                            FuelFunction.ALKINE)


    @staticmethod
    def monoalcohol(c, p):
        OrganicFuel.test_function_building_arguments(c, p)
        name = f'{OrganicFuel.C_PREFIX[c]}anol' if c < 3 else f'{OrganicFuel.C_PREFIX[c]}an-{p}-ol'
        return OrganicFuel(name,
                            [{"element": PeriodicTable.CARBON, "quantity": c},
                             {"element": PeriodicTable.HYDROGEN, "quantity": (2 * c + 2)},
                             {"element": PeriodicTable.OXYGEN, "quantity": 1}],
                            [{"bond": BondEnergyTable.CARBON_S, "quantity": (c-1)},
                             {"bond": BondEnergyTable.CARBON_HYDROGEN, "quantity": (2 * c + 1)},
                             {"bond": BondEnergyTable.CARBON_OXYGEN_S, "quantity": 1},
                             {"bond": BondEnergyTable.OXYGEN_HYDROGEN, "quantity": 1}],
                            FuelFunction.ALKANE)
    
    
    @staticmethod
    def random_fuel():
        function = choice(list(FuelFunction))
        match function:
            case FuelFunction.ALKENE, FuelFunction.ALKINE:
                carbon = randint(2, 10)
##            case FuelFunction.KETONE:
##                carbon = randint(3, 10)
            case _:
                carbon = randint(1, 10)        
        
        special_position = 0 if carbon < 3 else randint(1, int(carbon/2))

        match function:
            case FuelFunction.ALKANE:
                return OrganicFuel.alkane(carbon)
            case FuelFunction.ALKENE:
                return OrganicFuel.alkene(carbon, special_position)
            case FuelFunction.ALKINE:
                return OrganicFuel.alkine(carbon, special_position)
            case FuelFunction.ALCOHOL:
                return OrganicFuel.monoalcohol(carbon, special_position)


for c in range (10):
    print(OrganicFuel.random_fuel())
