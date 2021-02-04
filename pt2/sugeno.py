import numpy as np
from matplotlib import pyplot as plt

class Sugeno():
    def __init__(consequents, antecedents):
        assert(len(consequents) == len(antecedents))
        self.consequents = consequents
        self.antedecents = antecedents

    def infer(x):
        weights = [ant(x) for ant in self.antecedent]
        consequent_memberships = [con(x) for cor in self.consequents]

        output = 0
        for (w, cm) in zip(weights, consequent_memberships):
            output += w*cm

        normal_output = output/sum(weights)
