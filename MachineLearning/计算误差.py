def error(f,x,y):
    import scipy
    return scipy.sum((f(x)-y)**2)
