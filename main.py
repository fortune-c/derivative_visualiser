import matplotlib.pyplot as plt
from sympy import *
from sympy.abc import x
from sympy.core import sympify

## user enters the function in a string
function = str(input("Enter function: "))
## turns the string into a mathematical expression through `sympify`
original_func = sympify(function)
# print(original_func)



## now we will turn the function into a derivative
derivation_func = Derivative(original_func, x, evaluate=True)
print(derivation_func)

# =========================
# ORIGINAL FUNCTION EVALUATION
# =========================

f = lambdify(x, original_func)

x_axis = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
y_axis = []
# # This automatically loops, evaluates, and fills the array
# y_axis = [f(val) for val in x_axis]

for val in x_axis:
    result = f(val)
    y_axis.append(result)

print(x_axis)
print(y_axis)

# =========================
# DERIVATIVE EVALUATION
# =========================

df = lambdify(x, derivation_func)

dy_axis = []

for val in x_axis:
    result = df(val)
    dy_axis.append(result)


# =========================
# VISUALIZATION
# =========================

plt.figure(figsize=(10, 10))

# plot original function
plt.plot(x_axis, y_axis, label="f(x)", color="blue")

# add grid and labels
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Function Visualization")
plt.legend()

plt.savefig("./graphs/func_visualization.png")

plt.figure(figsize=(10, 10))

plt.plot(x_axis, y_axis, label="f(x)", color="blue")
plt.plot(x_axis, dy_axis, label="f'(x)", color="red")

plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Function vs Derivative")
plt.legend()

plt.savefig("./graphs/func_vs_deri.png")

##

a = 2  # chosen x-position (simulate slider)
slope = df(a) ## compute slope at that point
y_point = f(a) ## compute point on curve

##Build a tangent line
tangent_y = []

for val in x_axis:
    t = y_point + slope * (val - a)
    tangent_y.append(t)

## Plot tangent line
plt.figure(figsize=(8, 5))

plt.plot(x_axis, y_axis, label="f(x)", color="blue")
plt.plot(x_axis, tangent_y, label="tangent", color="green")

plt.scatter([a], [y_point], color="black", label="point")

plt.grid(True)
plt.legend()
plt.title("Tangent Line Visualization")

plt.savefig("./graphs/tangent_line_visualization.png")