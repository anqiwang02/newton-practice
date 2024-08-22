x0 = 1


# a function of choice
def f(x):
    y = 2 * x**2
    return y


def d_f(x):
    h = 10 ** (-5)  # make it infintely small
    return (f(x + h) - f(x)) / h  # first derivative of fun(x)


def dd_f(x):
    h = 10 ** (-5)
    return (d_f(x + h) - d_f(x)) / h  # second derivative of fun(x)


for i in range(10):
    xt = x0 - d_f(x0) / dd_f(x0)
    # update the new xt to be x0
    x0 = xt
    if abs(xt - x0) == 0:
        break

xt


# ignore below
# from sympy import diff, ln
# from sympy.abc import x
# import math

# f = 2*x**2 #function
# df = diff(f) #first derivative
# ddf = diff(df) #second derivative
# print(df)
# print(ddf)
