import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Using Antecedent/Consequent objects to store the crisp variables and membership functions
speed = ctrl.Antecedent(np.arange(0, 160, 5), 'speed')
density = ctrl.Antecedent(np.arange(0, 60, 5), 'service')
#tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# Auto-membership function populates membership values automatically
speed.automf(3)

# Defining membership functions manually
density['less'] = fuzz.trapmf(density.universe, [0, 0, 15, 20])
# density['normal'] = fuzz.trapmf(density.universe, [0, 13, 25])
# density['high'] = fuzz.trapmf(density.universe, [13, 25, 25])


speed['average'].view()
