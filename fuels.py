from elements import *
from enum import Enum
from random import randint, choice


class FuelFunction(Enum):
    ALKANE = {"method": 'alkane', "name": 'alcano'}
    ALKENE = {"method": 'alkene', "name": 'alceno'}
    ALKINE = {"method": 'alkine', "name": 'alcino'}
    ALCOHOL = {"method": 'monoalcohol', "name": 'álcool'}
    KETONE = {"method": 'ketone', "name": 'cetona'}
    ETHER = {"method": 'ether', "name": 'éter'}
    ALDEHYDE = {"method": 'aldehyde', "name": 'aldeído'}
    CARBOX = {"method": 'carbox', "name": 'ácido carboxílico'}



class OrganicFuel():

    C_PREFIX = ['', 'met', 'et', 'prop', 'but', 'pent', 'hex', 'hept', 'oct', 'non', 'dec', 'undec', 'dodec']
    ## C_SPECIAL_RADICALS = ['vinil', 'isopropil', 'isobutil', 'isopentil']
    
    def __init__(self, n, a, b, fc):
        self.name = n
        self.atoms = a
        self.bonds = b
        self.function = fc
        self.formula = Element.set_formula(self.atoms)
        self.enthalpy = self.set_enthalpy()
        self.molar_mass = Element.set_molar_mass(self.atoms)


    def set_enthalpy(self):
        return sum(bond["bond"].get_bond_energy() * bond["quantity"] for bond in self.bonds)


    def __str__(self):
        return f'\n{self.name.title()} ({self.formula}) é um {self.function.value["name"]};\nEntalpia: {self.enthalpy} kJ/mol; Massa molar: {self.molar_mass} g/mol.'


    def _test_function_building_arguments(c, p = 0, is_double_carbon_needed = False):
        if type(c) is not int or type(p) is not int:
            raise TypeError('Número de carbonos e posição da insaturação devem ser inteiros.')
        if is_double_carbon_needed:
            # This need occurs in carbon chains with insaturations, ethers etc.
            if c < 2:
                raise ValueError('Número de carbonos deve ser superior à 1')
        else:
            if c < 1:
                raise ValueError('Número de carbonos deve ser superior à 0')
        if c > len(OrganicFuel.C_PREFIX)-1:
            raise ValueError(f'Função não implementada para funções acima de {c} carbonos')
        if c > 3 and p > (c/2):
            raise ValueError('Posição da insaturação fixada em local inadequado')

    
    @staticmethod
    def alkane(c, p = 0):
        OrganicFuel._test_function_building_arguments(c)
        return OrganicFuel(f'{OrganicFuel.C_PREFIX[c]}ano',
                            [{"element": PeriodicTable.CARBON, "quantity": c}, {"element": PeriodicTable.HYDROGEN, "quantity": (2 * c + 2)}],
                            [{"bond": BondEnergyTable.CARBON_S, "quantity": (c-1)}, {"bond": BondEnergyTable.CARBON_HYDROGEN, "quantity": (2 * c + 2)}],
                            FuelFunction.ALKANE)


    @staticmethod
    def alkene(c, p):
        OrganicFuel._test_function_building_arguments(c, p, True)
        name = f'{OrganicFuel.C_PREFIX[c]}eno' if c < 3 else f'{OrganicFuel.C_PREFIX[c]}-{p}-eno'
        return OrganicFuel(name,
                            [{"element": PeriodicTable.CARBON, "quantity": c}, {"element": PeriodicTable.HYDROGEN, "quantity": (2 * c)}],
                            [{"bond": BondEnergyTable.CARBON_S, "quantity": (c-2)},
                             {"bond": BondEnergyTable.CARBON_D, "quantity": 1},
                             {"bond": BondEnergyTable.CARBON_HYDROGEN, "quantity": (2 * c)}],
                            FuelFunction.ALKENE)


    @staticmethod
    def alkine(c, p):
        OrganicFuel._test_function_building_arguments(c, p, True)
        name = f'{OrganicFuel.C_PREFIX[c]}ino' if c < 3 else f'{OrganicFuel.C_PREFIX[c]}-{p}-ino'
        return OrganicFuel(name,
                            [{"element": PeriodicTable.CARBON, "quantity": c}, {"element": PeriodicTable.HYDROGEN, "quantity": (2 * c - 2)}],
                            [{"bond": BondEnergyTable.CARBON_S, "quantity": (c-2)},
                             {"bond": BondEnergyTable.CARBON_T, "quantity": 1},
                             {"bond": BondEnergyTable.CARBON_HYDROGEN, "quantity": (2 * c - 2)}],
                            FuelFunction.ALKINE)
  

    @staticmethod
    def monoalcohol(c, p):
        OrganicFuel._test_function_building_arguments(c, p)
        name = f'{OrganicFuel.C_PREFIX[c]}anol' if c < 3 else f'{OrganicFuel.C_PREFIX[c]}an-{p}-ol'
        return OrganicFuel(name,
                            [{"element": PeriodicTable.CARBON, "quantity": c},
                             {"element": PeriodicTable.HYDROGEN, "quantity": (2 * c + 2)},
                             {"element": PeriodicTable.OXYGEN, "quantity": 1}],
                            [{"bond": BondEnergyTable.CARBON_S, "quantity": (c-1)},
                             {"bond": BondEnergyTable.CARBON_HYDROGEN, "quantity": (2 * c + 1)},
                             {"bond": BondEnergyTable.CARBON_OXYGEN_S, "quantity": 1},
                             {"bond": BondEnergyTable.OXYGEN_HYDROGEN, "quantity": 1}],
                            FuelFunction.ALCOHOL)


    @staticmethod
    def ketone(c, p):
        if c < 3:
            raise ValueError('Número de carbonos deve ser superior à 2')
        
        name = f'{OrganicFuel.C_PREFIX[c]}ona' if c < 5 else f'{OrganicFuel.C_PREFIX[c]}an-{p}-ona'
        return OrganicFuel(name,
                            [{"element": PeriodicTable.CARBON, "quantity": c},
                             {"element": PeriodicTable.HYDROGEN, "quantity": (2 * c)},
                             {"element": PeriodicTable.OXYGEN, "quantity": 1}],
                            [{"bond": BondEnergyTable.CARBON_S, "quantity": (c-1)},
                             {"bond": BondEnergyTable.CARBON_HYDROGEN, "quantity": (2 * c)},
                             {"bond": BondEnergyTable.CARBON_OXYGEN_D, "quantity": 1}],
                            FuelFunction.KETONE)


    @staticmethod
    def ether(c, p):
        OrganicFuel._test_function_building_arguments(c, p, True)
        name = f'{OrganicFuel.C_PREFIX[p]}oxi{OrganicFuel.C_PREFIX[c-p]}ano'
        return OrganicFuel(name,
                            [{"element": PeriodicTable.CARBON, "quantity": c},
                             {"element": PeriodicTable.HYDROGEN, "quantity": (2 * c + 2)},
                             {"element": PeriodicTable.OXYGEN, "quantity": 1}],
                            [{"bond": BondEnergyTable.CARBON_S, "quantity": (c-2)},
                             {"bond": BondEnergyTable.CARBON_HYDROGEN, "quantity": (2 * c + 2)},
                             {"bond": BondEnergyTable.CARBON_OXYGEN_S, "quantity": 2}],
                            FuelFunction.ETHER)


    @staticmethod
    def aldehyde(c, p):
        OrganicFuel._test_function_building_arguments(c, p)
        name = f'{OrganicFuel.C_PREFIX[c]}anal'
        return OrganicFuel(name,
                            [{"element": PeriodicTable.CARBON, "quantity": c},
                             {"element": PeriodicTable.HYDROGEN, "quantity": (2 * c)},
                             {"element": PeriodicTable.OXYGEN, "quantity": 1}],
                            [{"bond": BondEnergyTable.CARBON_S, "quantity": (c-1)},
                             {"bond": BondEnergyTable.CARBON_HYDROGEN, "quantity": (2 * c)},
                             {"bond": BondEnergyTable.CARBON_OXYGEN_D, "quantity": 1}],
                            FuelFunction.ALDEHYDE)

    @staticmethod
    def carbox(c, p):
        OrganicFuel._test_function_building_arguments(c, p)
        name = f'ácido {OrganicFuel.C_PREFIX[c]}anóico'
        return OrganicFuel(name,
                            [{"element": PeriodicTable.CARBON, "quantity": c},
                             {"element": PeriodicTable.HYDROGEN, "quantity": (2 * c)},
                             {"element": PeriodicTable.OXYGEN, "quantity": 2}],
                            [{"bond": BondEnergyTable.CARBON_S, "quantity": (c-1)},
                             {"bond": BondEnergyTable.CARBON_HYDROGEN, "quantity": (2 * c - 1)},
                             {"bond": BondEnergyTable.OXYGEN_HYDROGEN, "quantity": 1},
                             {"bond": BondEnergyTable.CARBON_OXYGEN_S, "quantity": 1},
                             {"bond": BondEnergyTable.CARBON_OXYGEN_D, "quantity": 1}],
                            FuelFunction.CARBOX)

    
    @staticmethod
    def get_organic_fuel(function, carbons, special_position):
        if type(function) is not FuelFunction:
            raise TypeError('A valid FuelFunction operator should be passed.')
        if carbons >= len(OrganicFuel.C_PREFIX):
            raise ValueError(f'Only chains below {len(OrganicFuel.C_PREFIX)} carbons are able to be created.')
        return getattr(OrganicFuel, function.value["method"])(carbons, special_position)

    
    @staticmethod
    def random_fuel():
        function = choice(list(FuelFunction))
        c_limit = len(OrganicFuel.C_PREFIX)-1
        match function:
            case FuelFunction.ALKENE | FuelFunction.ALKINE | FuelFunction.ETHER:
                carbon = randint(2, c_limit)                
            case FuelFunction.KETONE:
                carbon = randint(3, c_limit)
            case _:
                carbon = randint(1, c_limit)        
        
        special_position = 0 if carbon < 3 else randint(1, int(carbon/2))
        return getattr(OrganicFuel, function.value["method"])(carbon, special_position)
        
