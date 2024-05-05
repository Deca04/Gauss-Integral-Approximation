import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt

def f(x):
    return np.exp(-x**2)

#Int from -inf to +inf
int_inf, err_inf = spi.quad(f, -np.inf, np.inf)

#Int from 0 to +inf
int_0_inf, err_0_inf = spi.quad(f, 0, np.inf)

#f(a)=f(-a)=1/2
a = np.sqrt(2*np.log(2))

#x of flex points
x_flex = np.sqrt(2*np.log(2))/2

#set values for x
x = np.linspace(-5, 5, 1000)

#axis
fig, ax = plt.subplots()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

#Plot gauss function
ax.plot(x, f(x), color='r', label='f(x)')

#Area from 0 to +inf, drawings
x_inf = np.linspace(a, 5, 1000)
y_inf = f(x_inf)
ax.fill_between(x_inf, y_inf, color='g', alpha=0.3)
ax.text(a, 0.05, r'$a=\sqrt{2\ln(2)}$', fontsize=12)

#Area form -inf to +inf. drawings
x_both = np.linspace(-5, 5, 1000)
y_both = f(x_both)
ax.fill_between(x_both, y_both, color='b', alpha=0.1)

ax.axhline(y=0.5, color='navy', linestyle='--', alpha=0.5)

#flex points where f(a)=1/2
ax.plot([x_flex, x_flex], [0, f(x_flex)], color='navy', linestyle='--', alpha=0.5)
ax.plot([a, a], [0, f(a)], 'bo', markersize=5, label='f(a)=1/2')
ax.plot([-a, -a], [0, f(-a)], 'bo', markersize=5)

#legends
ax.legend()
plt.show()

print("Integral Values from -inf to +inf:", int_inf)
print("Error of the Integral Values from -inf to +inf", err_inf)
print("Integral Values from 0 to +inf:", int_0_inf)
print("Error of the Integral Values from 0 to +inf", err_0_inf)
print("Value of a so f(a)=1/2:", a)
print("x of flex points:", x_flex)
