from FuzzyRules import FuzzyRule


class Situations{

    private String situation = ""
    private LinguisticVariable var
    private String FuzzyTerms = ""
    private String weight
}


situations.addElement("low traffic")
situations.addElement("moderate traffic")
situations.addElement("high traffic")

for (i=0
     i < situations.size()
     i++){
    FuzzyRule rule = new FuzzyRule((String)situations.elementAt(i))
    if (rule.getName().equalsIgnoreCase("low traffic")){
        rule.addCondition(CA1, normal, 0.2)  # CA1 - speed
        rule.addCondition(CA2, less, 0.4)  # CA2 - density
    }
}


# Situation low_traffic
FuzzyRule rule = new FuzzyRule(situation: "low_traffic")
rule.addRules(CA1, fuzzy_term: "normal", weight: "0.2")

# Situation moderate_traffic
FuzzyRule rule = new FuzzyRule(situation: "moderate_traffic")
rule.addRules(CA1, fuzzy_term: "normal", weight: "0.2")

# Situation high_traffic
FuzzyRule rule = new FuzzyRule(situation: "high_traffic")
rule.addCondition(CA1, fuzzy_term: "normal", weight: "0.2")
