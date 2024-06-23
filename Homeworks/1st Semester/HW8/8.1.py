import numpy
from matplotlib import pyplot as plt
import scipy

def func(x) -> float:
    #Отображаемая фукнция
    return 7 * numpy.log2(4*x) * numpy.cos(3*x - 1)

def tgn(x0, x) -> float:
    fx_der = scipy.misc.derivative(func, x0, dx = 1e-6)
    fx0 = func(x0)
    return fx0 + fx_der * (x-x0)


def normal(x0, x) -> float:
    f = scipy.misc.derivative(func, x0, dx = 1e-6)
    f_0 = func(x0)
    return f_0 - 1/f * (x-x0)

def derivatives_display(x) -> None:
    plt.figure()
    plt.plot(x,scipy.misc.derivative(func, x),label = "1-st derivative function")
    plt.plot(x,scipy.misc.derivative(func, x, n=2), label="2-nd derivative function")
    plt.legend()
    return

def base_function_display(x, y) -> None:

    max = [x[numpy.argmax(y)],numpy.max(y)]
    min = [x[numpy.argmin(y)],numpy.min(y)]

    plt.figure()
    plt.plot(x,y,label = "Base function")
    plt.plot([max[0]], [max[1]], 'o', color='g', label='Max point')
    plt.plot(min[0], [min[1]], 'o', color='r', label='Min point')
    plt.legend()
    return

def tangent_display(x):
    plt.figure()
    plt.plot(x,tgn(1.2,1.2))
    plt.plot(x, tgn(1.2,x),linestyle = "--",label="Tangent")
    plt.legend()
    return

def normal_display(func, x, y):
    pass

def main() -> None:
    x = numpy.arange(0, 5, 0.1)
    y = func(x)


    base_function_display(x, y)
    derivatives_display(x)
    tangent_display(x)


    # norm_figure = plt.figure()
    # plt.plot(label = "Normal function")

    plt.show()
if __name__ == '__main__':
    main()


