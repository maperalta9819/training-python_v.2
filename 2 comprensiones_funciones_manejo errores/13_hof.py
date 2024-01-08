#Higher order function: una función dentro de otra función

def increment(x):
    return x +1

def high_ord_func(x,func):
    return x + func(x)

result = high_ord_func(2,increment)
