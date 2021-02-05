import numpy as np
from matplotlib import pyplot as plt

class Sugeno():
    def __init__(self, consequents, antecedents):
        #eh mt noia ficar incomodado com os consequentes antes dos antecedentes?
        assert(len(consequents) == len(antecedents))
        self.consequents = consequents
        self.antecedents = antecedents

    def infer(self, x):
        # weights = [ant(x) for ant in self.antecedents]
        weights = self.antecedents
        # consequent_memberships = [con(x) for cor in self.consequents]
        consequent_memberships = self.consequents

        output = 0
        for (w, cm) in zip(weights, consequent_memberships):
            output += w*cm

        normal_output = output/sum(weights)
        return normal_output