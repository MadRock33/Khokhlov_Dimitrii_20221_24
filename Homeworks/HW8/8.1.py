import numpy
from matplotlib import pyplot as plt
import scipy

def func(x):
    #Отображаемая фукнция
    return 7 * numpy.log2(4*x) * numpy.cos(3*x - 1)

def tangent(x0, x):
    f = scipy.misc.derivative(func, x0, dx = 1e-6)
    f_0 = func(x0)
    tangent_result = f_0 + f * (x-x0)
    return tangent_result
def normal(x0, x):
    f = scipy.misc.derivative(func, x0, dx = 1e-6)
    f_0 = func(x0)
    normal_result = f_0 - 1/f * (x-x0)
    return normal_result
def diff(f,x,n):
    #Производная функции
    return scipy.misc.derivative(f, x, dx = 1e-6, n = n)
def main():
    x = numpy.arange(0, 5, 0.1)
    y = func(x)
    max = [x[numpy.argmax(y)],numpy.max(y)]
    min = [x[numpy.argmin(y)],numpy.min(y)]

    base_figure = plt.figure()
    plt.plot(x,y,label = "Base function")
    plt.plot(max[0], max[1], 'o', color='g', label='т.max')
    plt.plot(min[0], min[1], 'o', color='r', label='т.min')

    diff_figure = plt.figure()
    plt.plot(x,diff(func,x,1),label = "Derivative function")
    plt.plot(x, diff(func, x, 2), label="Derivative function 2")

    tang_figure = plt.figure()
    plt.plot(label = "Tangent function")
    # norm_figure = plt.figure()
    # plt.plot(label = "Normal function")
    plt.legend()
    plt.show()
if __name__ == '__main__':
    main()


