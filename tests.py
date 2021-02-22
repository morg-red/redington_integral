from integration import integral, integral_aux
import numpy as np

print("Integral_aux Tests")
print("integral_aux(lambda x : 1*x**2,0,1,10)")
print(integral_aux(lambda x : 1*x**2,0,1,10)) #Tests int_-^1 { 1*x^2 } = ( 1/3 )* x^3

print("integral_aux(np.cos,0,np.pi,10)")
print(integral_aux(np.cos,0,np.pi,10)) #Tests a trigonometric function

print("integral_aux(lambda x : 1/(1+np.exp(x)),0,1,10)")
print(integral_aux(lambda x : 1/(1+np.exp(x)),0,1,10)) #tests 1/1+e^x

print("Integral Tests")

print("integral(lambda x : 1*x**2,0,1,1e-10)")
print(integral(lambda x : 1*x**2,0,1,1e-10)) #Tests int_-^1 { 1*x^2 } = ( 1/3 )* x^3

print("integral_aux(np.cos,0,np.pi,1e-10)")
print(integral(np.cos,0,np.pi,1e-10)) #Tests a trigonometric function

print("integral_aux(lambda x : 1/(1+np.exp(x)),0,1,1e-10)")
print(integral(lambda x : 1/(1+np.exp(x)),0,1,1e-10)) #tests 1/1+e^x
