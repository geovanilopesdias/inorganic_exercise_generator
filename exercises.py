from random import choice, randint
from reactions import ChemicalEquation


def random_stoic_exerc_variables():
    equation = ChemicalEquation.random_reaction()
    substances = [s for s in equation.reactants + equation.products]
    sub1 = choice(substances)
    while True:
        sub2 = choice(substances)
        if sub1 != sub2:
            return {"reaction": equation, "known_variable": sub1, "unknown_variable": sub2}


def stoichiometry_exercise():
    known_variable_value = randint(100, 500)
    data = random_stoic_exerc_variables()
    statement_elements = [f"Sabendo a reação: \n\t {data['reaction']} \ncalcula a massa de {data['unknown_variable'].formula} "]
    answer = known_variable_value * data['unknown_variable'].molar_mass * data['unknown_variable'].coefficient
    answer /= (data['known_variable'].molar_mass * data['known_variable'].coefficient)

    ## Statement construction
    if data["unknown_variable"] in data['reaction'].reactants:
        statement_elements.append("necessária, sabendo que ")
    else:
        statement_elements.append("produzida, sabendo que ")

    statement_elements.append(f"{known_variable_value} g de {data['known_variable'].formula} é ")
        
    if data['known_variable'] in data['reaction'].reactants:
        statement_elements.append("consumida.")
    else:
        statement_elements.append("produzida.")
    return {"statement": "".join(statement_elements), "answer": round(answer, 1)}
