from math import exp, isinf, isnan, log

def bounded_linear(low, high, *, c_m=1, no_m=0, inverse=False):
    """Variant of the linear function with gradient being determined by bounds.

    The bounds determine minimum and maximum value-mappings,
    but also the gradient. As [0, 1] must be the bounds for y-values,
    left and right bounds specify 2 points on the graph, for which the formula
    f(x) = y = (y2 - y1) / (x2 - x1) * (x - x1) + y1 = (y2 - y1) / (x2 - x1) *
                                                                (x - x2) + y2

    (right_y - left_y) / ((right - left) * (x - self.left) + left_y)
    works.
    
    >>> f = bounded_linear(2, 3)
    >>> f(1)
    0.0
    >>> f(2)
    0.0
    >>> f(2.5)
    0.5
    >>> f(3)
    1.0
    >>> f(4)
    1.0
    """
    assert low < high, "low must be less than high"
    assert c_m > no_m, "core_m must be greater than unsupported_m"

    if inverse:
        c_m, no_m = no_m, c_m
    
    gradient = (c_m - no_m) / (high - low)
    
    # special cases found by hypothesis
    
    def g_0(_):
        return (c_m + no_m) / 2
    
    if gradient == 0:
        return g_0
    
    def g_inf(x):
        asymptode = (high + low) / 2
        if x < asymptode:
            return no_m
        elif x > asymptode:
            return c_m
        else:
            return (c_m + no_m) / 2
    
    if isinf(gradient):
        return g_inf
    
    def f(x):
        y = gradient * (x - low) + no_m
        if y < 0:
            return 0.
        if y > 1:
            return 1.
        return y
    return f