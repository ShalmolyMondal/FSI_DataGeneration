#fuzz.membership
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

from math import exp, isinf, isnan, log
from functions import bounded_linear
# class MembershipFunction {

# }

class Triangular:
    """
    Fuzzy Set with Triangular-shape function defined with a, b, and m points
              .
             /|\
            / | \
           /  |  \
         _/   |   \_
          |   m   |
          a       b
    """
    def __init__(self, a:int, m:int, b:int):
        self.a = a
        self.b = b
        self.m = m
    
    def __call__(self, x:int) -> int:
        if x <= self.a or x >= self.b: 
            return 0
        elif self.a < x <= self.m:
            return (x-self.a) / (self.m-self.a)
        elif self.m < x < self.b:
            return (self.b-x) / (self.b-self.m)

        
class Trapezoidal:
    """
    Trapezoid-shape function defined with points a, b, c and d
               _____
              /     \
             /|     |\
            / |     | \
           /  |     |  \
         _/   |     |   \_
          |   b     c   |
          a             d
    """
    def __init__(self, a:int, b:int, c:int, d:int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def __call__(self, x:int) -> int:
        if x <= self.a or x >= self.d:
            return 0
        elif self.a < x <= self.b:
            return (x-self.a) / (self.b-self.a)
        elif self.b < x < self.c:
            return 1
        elif self.b < x < self.d:
            return (self.d-x) / (self.d-self.c)
    
# def trapezoid(start, c_low, c_high, high, *, c_m=1, no_m=0):   
#      """
#     Trapezoid-shape function defined with points a, b, c and d
#                _____
#               /     \
#              /|     |\
#             / |     | \
#            /  |     |  \
#          _/   |     |   \_
#           |   b     c   |
#           a             d
#     """ 
#     assert low < c_low <= c_high < high
#     assert 0 <= no_m < c_m <= 1 

#     left_slope = bounded_linear(low, c_low, c_m=c_m, no_m=no_m)
#     right_slope = bounded_linear(c_high, high, c_m=c_m, no_m=no_m,
#                                 inverse=True)

#     def f(x):
#         if x < low or high < x:
#             return no_m
#         elif x < c_low:
#             return left_slope(x)
#         elif x > c_high:
#             return right_slope(x)
#         else:
#             return c_m

#     return f  

  
# Function for traingular fuzzyfication  
# def triangular(x,a,b,c):
#     return max(min((x-a)/(b-a), (c-x)/(c-b)),0)


# Using Antecedent/Consequent objects to store the crisp variables and membership functions
# speed = ctrl.Antecedent(np.arange(0, 140, 5), 'speed')
# density = ctrl.Antecedent(np.arange(0, 70, 5), 'service')
# #tip = ctrl.Consequent(np.arange(0, 26, 1), 'tip')

# # Auto-membership function populates membership values automatically
# #speed.automf(3)

# # Defining membership function for speed
# speed['slow'] = fuzz.trapmf(speed.universe, [0, 0, 35, 45])
# speed['normal'] = fuzz.trapmf(speed.universe, [40, 45, 75, 80])
# speed['fast'] = fuzz.trapmf(speed.universe, [75, 85, 115, 130])

# # Defining membership function for density
# density['less'] = fuzz.trapmf(density.universe, [0, 0, 15, 20])
# density['normal'] = fuzz.trapmf(density.universe, [18, 20, 35, 40])
# density['high'] = fuzz.trapmf(density.universe, [35, 40, 55, 60])


# speed['slow'].view()
# density.view()