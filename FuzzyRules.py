public class FuzzyRule{

    private String situation = ""
    private LinguisticVariable var
    private String FuzzyTerms = ""
    private String weight
}


public void addCondition(LinguisticVariable var, String FuzzyTerms, String weight){
    this.var = var
    this.FuzzyTerms = FuzzyTerms
    this.weight = weight
}

while


#####################################
class Antecedent:
    ''' 
    Antecedents are of the form: Linguistic Variables are adjective1 [op] variable2 is adjective2 
    Example: If density is less AND speed is normal
    '''

    def __init__(self, sentence: str, Linguisticvariables, FuzzyTerms):
        self.parse(sentence, Linguisticvariables, FuzzyTerms)

    def parse(self, sentence, LinguisticVariables, FuzzyTerms):
        words = sentence.split()
        self.LinguisticVariables = []
        self.FuzzyTerms = []
        self.operators = []


rating = Domain("ratings", 1, 10, res=0.1)
rating.norm = Set(bounded_linear(1, 10))

weights = {"beverage": 0.3,
           "atmosphere": 0.2,
           "looks": 0.2,
           "taste": 0.3}


def weighted_sum(weights, target):
    rsc = rescale(target._low, target._high)

    def f(factors):
        result = sum(r * weights[n] for n, r in factors.items())
        return round_partial(rsc(result), target._res)
    return f


print ("Situation" + situation + "is occurring with" +)
