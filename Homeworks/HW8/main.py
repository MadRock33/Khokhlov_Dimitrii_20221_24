import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

def f(x:int) -> float|int:
    return 7 * np.log2(4*x) * np.cos(3*x - 1)

def diff(x:int) -> float | int:
    return -21*x*np.log(4*x) * np.cos(3*x - 1)/np.log(2)*x

def diff2(x:int)-> float | int:
    return -42*x*np.sin(3*x-1) + (63*x**2*np.log(4*x) + 7)*np.cos(3*x - 1)/np.log(2)*x**2

def tangent_form(x, x0, y0):
    return y0 + diff(x0) * (x - x0)

def normal_form(x, x0, y0):
    return y0 - 1 / diff(x0) * (x - x0)

def plot_function(x_val, y_val, label, linestyle="-", color=None):
    plt.plot(x_val, y_val, label=label, linestyle=linestyle, color=color)

def plot_tangent_and_normal(x_val, x0, y0):
    plot_function(x_val, tangent_form(x_val, x0, y0), "Касательная", "--", "orange")
    plot_function(x_val, normal_form(x_val, x0, y0), "Нормаль", "--", "purple")


if __name__ == "__main__":
    x_val = np.linspace(0, 5, 1000)
    y_val = f(x_val)


    plt.figure(figsize=(8, 6))
    plot_function(x_val, y_val, "Function")
    plt.title("Graph function (fx)")
    plt.legend()


    plt.figure(figsize=(8, 6))
    plot_function(x_val, diff(x_val), "Derivative 1", linestyle="-", color="blue")
    plt.title("The First Derivative (df1)")
    plt.legend()


    plt.figure(figsize=(8, 6))
    plot_function(x_val, diff2(x_val), "Derivative 2", linestyle="-", color='red')
    plt.title("The Second Derivative (df2)")
    plt.legend()


    plt.figure(figsize=(8, 6))
    plot_function(x_val, diff(x_val), "Derivative 1", linestyle="-", color="blue")
    plot_function(x_val, diff2(x_val), "Derivative 2", linestyle="--", color="red")
    plt.title("The Derivative 1 and Derivative 2")
    plt.legend()


    min_index = np.argmin(y_val)
    min_point = (x_val[min_index], y_val[min_index])
    x0, y0 = min_point

    plt.figure(figsize=(8, 6))
    plot_function(x_val, f(x_val), "Function")
    plot_tangent_and_normal(x_val, x0, y0)
    plt.plot(x0, y0, "ro", label="Min")
    plt.title("Tangent and normal")
    plt.legend()


    plt.figure(figsize=(8, 6))
    plot_function(x_val, f(x_val), "Function")
    for x in np.linspace(0, 5, 5):
        plot_function(x_val, tangent_form(x_val, x, f(x)), f"tg() in point x={x:.1f}")
    plt.title("Tangent bundle")
    plt.legend()


    curve_length, _ = integrate.quad(lambda x: np.sqrt(1 + diff(x) ** 2), 0, 5)
    print(f"Длина кривой: {curve_length:.2f}")

    plt.show()
