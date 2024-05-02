from enum import Enum
from random import choice


class Element():
    def __init__(self, n, s, z, m, e):
        self.name = n
        self.symbol = s
        self.molar_number = z
        self.atomic_mass = m
        self.electronegativity = e


    @staticmethod
    def set_index(number):
        if type(number) is not int:
            raise TypeError('Número de átomos deve ser um inteiro')
        if number < 1:
            raise ValueError('Número de átomos deve ser superior à 1')
        
        UNICODE_ALGARISMS = [u'\u2080', u'\u2081', u'\u2082', u'\u2083', u'\u2084', u'\u2085' , u'\u2086', u'\u2087', '\u2088', '\u2089']
        return ''.join([UNICODE_ALGARISMS[int(digit)] for digit in str(number)]) if number > 1 else ''


    @staticmethod
    def set_molar_mass(atoms):
        """
        Given a list of dictionaries contaning an Element instance at the key 'element' and
        its number of atoms in the key 'quantity', returns the molecular/ionic molar mass.
        """
        if type(atoms) is not list:
            raise TypeError
        try:
            return sum(atom["element"].get_molar_mass() * atom["quantity"] for atom in atoms)
        except TypeError as e:
            print(f'{e}: values of the dicts in list do not match the proper type.')


    @staticmethod
    def get_element_index(element, substance):
        """
        Given a list of dictionaries contaning an Element instance at the key 'element' and
        its number of atoms in the key 'quantity', returns the quantity value of the given element.
        """
        if not isinstance(element, PeriodicTable) or type(substance) is not list:
            raise TypeError(f'Element is {type(element)} (should be PeriodicTable) or substance is {type(substance)} should be list.')

        index = next(filter(lambda atom: atom["element"] == element, substance), None)
        return index["quantity"] if index is not None else 0


    @staticmethod
    def set_formula(atoms):
        return ''.join([f'{atom["element"].get_symbol()}{Element.set_index(atom["quantity"])}' for atom in atoms])



class PeriodicTable(Enum):
    # Alkalines
    LITHIUM = Element('lítio', 'Li', 3, 6.9, 1.0)
    BERILLIUM = Element('berílio', 'Be', 4, 9.0, 1.5)
    SODIUM = Element('sódio', 'Na', 11, 23.0, .9)
    MAGNESIUM = Element('magnésio', 'Mg', 12, 24.3, 1.2)
    POTASSIUM = Element('potássio', 'K', 19, 39.1, .8) 
    CALCIUM = Element('cálcio', 'Ca', 20, 40.1, 1.0)
    RUBIDIUM = Element('rubídio', 'Rb', 37, 85.5, .8)
    STRONTIUM = Element('estrôncio', 'Sr', 38, 87.6, 1.0)
    CESIUM = Element('césio', 'Cs', 55, 132.9, .7)
    BARIUM = Element('bário', 'Ba', 56, 137.3, .9)
    RADIUM = Element('rádio', 'Ra', 88, 226.0, .9)

    # Non-metals
    HYDROGEN = Element('hidrogênio', 'H', 1, 1.0, 2.1)
    BORON = Element('boro', 'B', 5, 10.8, 2.0)
    CARBON = Element('carbono', 'C', 6, 12.0, 2.5)
    NITROGEN = Element('nitrogênio', 'N', 7, 14.0, 3.0)
    OXYGEN = Element('oxigênio', 'O', 8, 16.0, 3.5)
    SILICON = Element('silício', 'Si', 14, 28.1, 1.8)
    PHOSPHORUS = Element('fósforo', 'P', 15, 31.0, 2.1)
    SULFUR = Element('enxofre', 'S', 16, 32.1, 2.5)
    ARSENIC = Element('arsênio', 'As', 33, 74.9, 2.0)
    SELENIUM = Element('selênio', 'Se', 34, 78.9, 2.4)
    ANTIMONIUM = Element('antimônio', 'Sb', 51, 121.7, 1.9)

    # Halogens
    FLUORINE = Element('flúor', 'F', 9, 19.0, 4.0)
    CHLORINE = Element('cloro', 'Cl', 17, 35.5, 3.0)
    BROMINE = Element('bromo', 'Br', 35, 79.9, 2.8)
    IODINE = Element('iodo', 'I', 53, 126.9, 2.5)
    
    # Commom Metals
    ALUMINIUM = Element('alumínio', 'Al', 13, 27.0, 1.5)     
    TITANIUM = Element('titânio', 'Ti', 22, 47.9, 1.5)
    CHROMIUM = Element('cromo', 'Cr', 24, 52.0, 1.6)
    MANGANESE = Element('manganês', 'Mn', 25, 54.9, 1.5)
    IRON = Element('ferro', 'Fe', 26, 55.8, 1.8)
    COBALT = Element('cobalto', 'Co', 27, 58.9, 1.8)
    NICKEL = Element('níquel', 'Ni', 28, 58.7, 1.8)
    COPPER = Element('zinco', 'Zn', 30, 65.4, 1.6)
    ZINC = Element('zinco', 'Zn', 30, 65.4, 1.6)
    SILVER = Element('prata', 'Ag', 47, 107.9, 1.9)
    CADMIUM = Element('cádmio', 'Cd', 48, 112.4, 1.7)
    TIN = Element('estanho', 'Sn', 50, 118.6, 1.8)
    PLATINUM = Element('platina', 'Pt', 78, 195.0, 2.2)
    GOLD = Element('ouro', 'Au', 79, 197.0, 2.4)
    QUICKSILVER = Element('mercúrio', 'Hg', 80, 200.5, 1.9)
    LEAD = Element('chumbo', 'Pb', 82, 207.2, 1.8)
    BISMUTH = Element('bismuto', 'Bi', 83, 207, 1.9)


    def get_symbol(self):
        return self.value.symbol


    def get_name(self):
        return self.value.name


    def get_molar_mass(self):
        return self.value.atomic_mass



class CovalentBondType(Enum):
    SIMPLE = 1
    DOUBLE = 2
    TRIPLE = 3
    QUADRUPLE = 4



class CovalentBond():
    def __init__(self, e1, e2, t, e):
        self.element1 = e1
        self.element2 = e2
        self.type = t
        self.energy = e



class BondEnergyTable(Enum):
    HYDROGEN_S = CovalentBond(PeriodicTable.HYDROGEN, PeriodicTable.HYDROGEN, CovalentBondType.SIMPLE, 436)
    OXYGEN_S = CovalentBond(PeriodicTable.OXYGEN, PeriodicTable.OXYGEN, CovalentBondType.SIMPLE, 142)
    NITROGEN_S = CovalentBond(PeriodicTable.NITROGEN, PeriodicTable.NITROGEN, CovalentBondType.SIMPLE, 163)
    NITROGEN_D = CovalentBond(PeriodicTable.NITROGEN, PeriodicTable.NITROGEN, CovalentBondType.DOUBLE, 418)
    OXYGEN_HYDROGEN = CovalentBond(PeriodicTable.OXYGEN, PeriodicTable.OXYGEN, CovalentBondType.SIMPLE, 464) 
    NITROGEN_HYDROGEN = CovalentBond(PeriodicTable.NITROGEN, PeriodicTable.OXYGEN, CovalentBondType.SIMPLE, 389) 

    CARBON_S = CovalentBond(PeriodicTable.CARBON, PeriodicTable.CARBON, CovalentBondType.SIMPLE, 347)
    CARBON_D = CovalentBond(PeriodicTable.CARBON, PeriodicTable.CARBON, CovalentBondType.DOUBLE, 611)
    CARBON_T = CovalentBond(PeriodicTable.CARBON, PeriodicTable.HYDROGEN, CovalentBondType.TRIPLE, 837)
    CARBON_HYDROGEN = CovalentBond(PeriodicTable.CARBON, PeriodicTable.OXYGEN, CovalentBondType.SIMPLE, 414)
    CARBON_OXYGEN_S = CovalentBond(PeriodicTable.CARBON, PeriodicTable.OXYGEN, CovalentBondType.SIMPLE, 360)
    CARBON_OXYGEN_D = CovalentBond(PeriodicTable.CARBON, PeriodicTable.OXYGEN, CovalentBondType.DOUBLE, 736)
    CARBON_NITROGEN_S = CovalentBond(PeriodicTable.CARBON, PeriodicTable.NITROGEN, CovalentBondType.SIMPLE, 305)
    CARBON_NITROGEN_D = CovalentBond(PeriodicTable.CARBON, PeriodicTable.NITROGEN, CovalentBondType.DOUBLE, 615)
    CARBON_FLUORINE = CovalentBond(PeriodicTable.CARBON, PeriodicTable.FLUORINE, CovalentBondType.SIMPLE, 485)


    def get_bond_energy(self):
        return self.value.energy
