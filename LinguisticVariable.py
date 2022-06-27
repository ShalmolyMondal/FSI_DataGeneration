import matplotlib.pyplot as plt

class FuzzyTerms:
    """describes a crisp value with """
    def __init__(self, name:str, membership_function):
        self.name = name
        self.func = membership_function
        
    def __str__(self):
        return self.name
    
class LinguisticVariable:
    """Defining Linguistic variables using fuzzy sets using the associated membership functions"""
    def __init__(self, name:str, *terms):
        self.adjectives = terms
        self.name = name
        self.value = None

    def __str__(self):
        return self.name

    def type(self, value):
        'Given a value, returns the adjective that best represent it'
        max_value = -1
        terms = None
        for term in self.terms:
            x = term.func(value)
            if x > max_value:
                max_value = x
                terms = term
        return terms
    
    def plot(self, sample):
        'Plot the adjective functions'
        fig = plt.figure()
        for term in self.terms:
            y = [term.func(x) for x in sample]
            plt.plot(sample, y)
        plt.legend([term.name for term in self.terms])
        fig.savefig(f'img/{self.name}')
        plt.close(fig)