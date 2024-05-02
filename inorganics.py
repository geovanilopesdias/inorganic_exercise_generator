from iontable import *
from elements import Element
from random import choice

def random_anion_for_salt():
    anion = choice(list(AnionTable)).value
    while anion in (AnionTable.OXIDE.value, AnionTable.HYDROXIDE.value):
        anion = choice(list(AnionTable)).value
    return anion


def random_anion_for_acid():
    anion = choice(list(AnionTable)).value
    while anion in (AnionTable.HYDRITE.value, AnionTable.OXIDE.value, AnionTable.HYDROXIDE.value):
        anion = choice(list(AnionTable)).value
    return anion


def random_cation():
    return choice(list(CationTable)).value
        

def get_base_formula(cation):
    return f'{cation.formula}OH' if cation.charge == 1 else f'{cation.formula}(OH){Element.set_index(cation.charge)}'


def get_base_name(cation):
    return f'hidróxido de {cation.name}'


def get_acid_formula(anion):
    if anion in (AnionTable.HYDRITE.value, AnionTable.OXIDE.value, AnionTable.HYDROXIDE.value):
        raise ValueError(f'Íon "{anion}" inapropriado para instanciamento de ácidos.')

    if PeriodicTable.HYDROGEN not in anion.atoms:
        return f'H{Element.set_index(anion.charge)}{anion.formula}'
    
    hydrogens_in_anion = next(filter(lambda x: x["element"] == PeriodicTable.HYDROGEN, anion.atoms), None)["quantity"]
    return f'H{Element.set_index(anion.charge) + hydrogens_in_anion}{anion.formula}'           


def get_acid_name(anion):
    if anion in (AnionTable.HYDRITE.value, AnionTable.OXIDE.value, AnionTable.HYDROXIDE.value):
        raise ValueError(f'Íon inapropriado para instanciamento de ácidos.')
    match anion.name[len(anion.name)-3:]:
        case 'ato':
            if 'sulf' in anion.name:
                return f'ácido {anion.name[:len(anion.name)-3]}úrico'
            if 'fosf' in anion.name:
                return f'ácido {anion.name[:len(anion.name)-3]}órico'
            if 'acet' in anion.name:
                return f'ácido {anion.name[:len(anion.name)-3]}ético'
            if 'nitr' in anion.name:
                return 'ácido nítrico'

            match anion.name[len(anion.name)-5]:
                case 'a':
                    vowel = 'â'
                case 'e':
                    vowel = 'é'
                case 'i':
                    vowel = 'í'
                case 'u':
                    vowel = 'ú'
                case 'o':
                    vowel = 'ó' if anion.atoms[0]["element"] not in (PeriodicTable.BROMINE,
                                                                     PeriodicTable.CARBON,
                                                                     PeriodicTable.CHROMIUM,
                                                                     PeriodicTable.SULFUR) else 'ô'
            return f'ácido {anion.name[:-5]}{vowel}{anion.name[len(anion.name)-4]}ico'
        
        case 'eto':
            return f'ácido {anion.name[:len(anion.name)-3]}ídrico'
        case 'ito':
            if 'sulf' in anion.name:
                return f'ácido {anion.name[:len(anion.name)-3]}uroso'
            if 'fosf' in anion.name:
                return f'ácido {anion.name[:len(anion.name)-3]}oroso'

            return f'ácido {anion.name[:len(anion.name)-3]}oso'
        

def get_salt_formula(cation, anion):
    if anion in (AnionTable.OXIDE, AnionTable.HYDROXIDE):
        raise ValueError(f'Íons inadequados para instanciamento de sais.')
    
    if cation.charge == anion.charge:
        return cation.formula + anion.formula

    if cation.charge/anion.charge in (.5, 2):
        if cation.charge > anion.charge:
            cation_part = cation.formula
            anion_part = anion.formula + Element.set_index(2) if anion.is_atomic() else f'({anion.formula})' + Element.set_index(2)
        else:
            anion_part = anion.formula
            cation_part = cation.formula + Element.set_index(2) if cation.is_atomic() else f'({cation.formula})' + Element.set_index(2)

    else:
        anion_part = anion.formula + Element.set_index(cation.charge) if anion.is_atomic() else f'({anion.formula})' + Element.set_index(cation.charge)
        cation_part = cation.formula + Element.set_index(anion.charge) if cation.is_atomic() else f'({cation.formula})' + Element.set_index(anion.charge)

    return cation_part+anion_part
        
        
def get_salt_name(cation, anion):
    if anion in (AnionTable.OXIDE, AnionTable.HYDROXIDE):
        raise ValueError(f'Íons inadequados para instanciamento de sais.')
    return f'{anion.name} de {cation.name}'
