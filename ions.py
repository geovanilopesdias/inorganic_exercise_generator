from elements import *
from random import choice

class Ion():
    def __init__(self, a, n, c):
        self.name = n
        self.atoms = self.set_atoms(a)
        self.charge = c
        self.formula = Element.set_formula(self.atoms)
        self.molar_mass = Element.set_molar_mass(self.atoms)


    def __str__(self):
        return f'{self.name} ({self.formula}) | Charge: {self.charge}; Mass: {self.molar_mass}'


    def set_atoms(self, atoms):
        if type(atoms) is list and atoms is not None:
            return atoms
        else:
            raise TypeError('A list of PeriodicTable values should be passed to Ion construction.')


    def is_atomic(self):
        return len(self.atoms) == 1 and self.atoms[0]["quantity"] == 1
