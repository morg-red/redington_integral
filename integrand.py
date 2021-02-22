def my_pow(x,n):
    """
    Computes the nth power of x

    Args:
        x (float/int): the base number
        n (float/int): the exponent

    Returns:
        result (float/int): the nth power of x
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

    Returns:
        result (float/int): the nth power of x times a
    """
    A = params["prefactor"]
    n = params["power"]
    return A * x**n
