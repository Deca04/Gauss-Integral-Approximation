#https://github.com/deca04-code

import numpy as np  
from scipy.integrate import quad    
from scipy.optimize import fsolve   
import matplotlib.pyplot as plt     

def function(x):
    return np.exp(-x**2)

def second_derivate(x):
    return 2*(2*x**2 - 1)*np.exp(-x**2)

def f(x):
   return function(x)-0.5 
x_half = fsolve(f, [-2, 2])

#extremes of integration
a = 0
b = 1
c = 5

#precision for definite and improper integration
n = 100
n2=1000 

#Calculation of the width = height of the trapezoids
h = (b-a)/n
h1 = (c-a)/n2 

#definite integration with trapezoid rule
integral = (h/2 )*(function(a) + function(b) + 2*np.sum(function(np.linspace(a, b, n, endpoint=False)[1:])))

improper_integral, Eimp = quad(function, 0, np.inf) 
imp_int_trap = (h1/2)*(function(a) + function(c) + 2*np.sum(function(np.linspace(a, c, n2, endpoint=False)[1:]))) 

#flexes and max error committed in definite integration
E = ((b-a)**3 / (12*n**2)) * max(abs(second_derivate(np.linspace(a, b, n+1))))
infl = fsolve(second_derivate, [-1, 1])

#max error in improper integration
Eimp_trap = ((c-a)**3 / (12*n2**2)) * max(abs(second_derivate(np.linspace(a, c, n2+1))))

print("\nValue of Gauss integral in [0;1]:", integral)
print("\nValue of improper integration from 0 to + infinite:", improper_integral)
print("Value of improper integration from 0 to + infinite, with trapezoid rule:", imp_int_trap)
print("\nabscissa of the inflections:", infl)
print("\nMaximum expected error of integral calculus:", E)
print("Maximum expected error of improper integral calculus:", Eimp)
print("Maximum expected error of improper integral calculus with trapezoid rule:", Eimp_trap)
print("\nAbscissa in which the integrand function assumes the value 1/2:", x_half)

x = np.linspace(-5, 5, 1000)
y = function(x)
fig, ax = plt.subplots()
ax.plot(x, y, label='Funzione integranda')
ax.fill_between(x, y, where=((x>=a)&(x<=b)), color='limegreen', alpha=0.3, label='Area limitata')
ax.fill_between(x, y, where=(x>=1), color='purple', alpha=0.3, label='Area illimitata')
ax.fill_between(x, y, where=((x>=0)&(x>=a)&(x<=b)), color='limegreen', alpha=0.3, label='Area in comune')
ax.set_title('Funzione integranda')
ax.set_xlabel('x')
ax.set_ylabel('y')

# style of x e y axes
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['bottom'].set_color('black')
ax.spines['left'].set_linewidth(1.5)
ax.spines['left'].set_color('black')
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

# style of x e y tags
ax.xaxis.label.set_color('black')
ax.yaxis.label.set_color('black')
ax.tick_params(axis='x', colors='black')
ax.tick_params(axis='y', colors='black')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Gauss Function')

plt.legend(['f(x)', 'Surface of integral from a to b', 'Surface of improper integral form a to + infinite'])
      
plt.show()