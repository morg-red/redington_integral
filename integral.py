def my_pow(x, n):
    """
    Computes x^n , for non-negative n values
    """

    res = 1
    return res

my_res = my_pow(0.0, 3)  # 0.0
my_res = my_pow(5.0, 0)  # 1.0
my_res = my_pow(5.0, 3)  # 125.0​


#=========== The HOMEWORK ASSIGNMENT ============
# Complete the my_pow function and test it for a variety of conditions

# Develop the integration function below, the function would take another function as an argument - see the example below

def integral_aux(func, func_params, a, b, npoints):
    """
    This will be similar to your target function, but with a finite number of integration points
    """
    return 0.0

def integral(func, func_params, a, b, precision):
    """
    Computes a definite integral of 1D function func on the interval [a, b]
    with the precision of "precicion"
​
    Args:
        func ( function_object ): the function to integrate
        func_params ( dictionary ): the additional parameters of the function
        a, b ( float ): end points of the integration
        precision ( float ): the consition for finishing the integration
            such that | integral_aux(... npoints) - integral_aux(... 2*npoints)| < precision
​
    To obey the precision, you would need to vary the number of integration points (related to dx)
    to reach the convergence to that specified threshold
​
    Info: https://en.wikipedia.org/wiki/Simpson%27s_rule
    """

    res = 0.0

    return res


# Here is how this should work

def my_super_power(x, params):
    # f(x) = A * x ^n
    A = params["prefactor"]
    n = params["power"]
    return A * x**n

# this would compute int_-^1 { 1*x^2 } = ( 1/3 )* x^3 | _0 ^1 = 1/3  <- the result you should get

my_integral = integral( my_super_power, {"prefactor":1.0, "power":2}, 0, 1, 1e-10)
