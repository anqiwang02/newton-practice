x0 = 1


# a function of choice
def f(x):
    y = (x**4)/4-x**3-x
    return y

def d_f(x):
    h = 10 ** (-5)
    return (f(x + h) - f(x)) / h

def dd_f(x):
   h = 10 ** (-5)
   return (d_f(x + h) - d_f(x)) / h  # second derivative of fun(x)

def optimize(x0):
    h = 10 ** (-5)  # make it infintely small
    dev_1 = d_f(x0) # first derivative of fun(x)
    dev_2 = dd_f(x0)
    x1=x0-dev_1/dev_2

    while abs(x1-x0)>=0.01:
        x0=x1
        x1=x0-dev_1/dev_2
        return [x1,dev_1,dev_2]



#def dd_f(x):
   # h = 10 ** (-5)
    #return (d_f(x + h) - d_f(x)) / h  # second derivative of fun(x)
    
# ignore below
# from sympy import diff, ln
# from sympy.abc import x
# import math

# f = 2*x**2 #function
# df = diff(f) #first derivative
# ddf = diff(df) #second derivative
# print(df)
# print(ddf)
