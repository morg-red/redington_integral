def my_pow(x,n):
    """
    Computes the nth power of x

    Args:
        x (float): the base number
        n (float): the exponent
    """
    result = x**n
    return result

def my_super_power(x, params):
    """
    Returns the nth power of x multiplied by a prefactor term

    Args:
        x (float): exponent base
        params:
            n (float): exponent power
            A (float): prefactor term

    """
    A = params["prefactor"]
    n = params["power"]
    return A * x**n
