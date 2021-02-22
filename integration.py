import numpy as np #imports numpy for use of linspace (and to aid in testing)

def integral_aux(func, a, b, N=100): #default is 100 integration points
    """
    Computes a definite integral of 1D function func on the interval [a, b] for use with integral function

    Args:
        func ( function_object ): the function to integrate. The author suggests using lambda
        a, b ( float ): start and end points of the integration
        N (int): number of sections the integration space is divided into
    """
    if N % 2 == 1:
        raise ValueError("N must be an even integer") #see above equations
    if N == 0:
        raise ValueError("N must be an even non-zero integer") #see above equations
    h = (b-a)/N
    x = np.linspace(a,b,N+1) #evenly slices the interval from a to b into N+1 pieces
    y = func(x) #solves the function for each sliced value
    result = h/3 * np.sum(y[0:-1:2] + 4*y[1::2] + y[2::2]) #these are set up so that each list is offset, avoiding triple counting
    return result

def integral(func, a, b, precision):
    """
    Computes a definite integral of 1D function func on the interval [a, b] with the precision of "precision"
    Args:
        func ( function_object ): the function to integrate. The author suggests using lambda
        a, b ( float ): start and end points of the integration
        precision ( float ): the condition for finishing the integration,
        such that | integral_aux(... npoints) - integral_aux(... 2*npoints)| < precision
    """
    N = 100
    result_1 = integral_aux(func, a, b, N)
    #print(result_1) #debug line
    N = 2*N
    result_2 = integral_aux(func, a, b, N)
    #print(result_2) #debug line
    while abs(result_1 - result_2) > precision: #repeats while ∆ results > precision
        N = 2*N
        result_1 = integral_aux(func, a, b, N)
        #print(result_1) #debug line
        N = 2*N
        result_2 = integral_aux(func, a, b, N)
        #print(result_2) #debug line
    return result_2
