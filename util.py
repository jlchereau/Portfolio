import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# To tune xi (exploration/expoitation),
# read https://github.com/fmfn/BayesianOptimization/blob/master/examples/exploitation_vs_exploration.ipynb

# Sources:
#   - https://github.com/romylorenz/AcquisitionFunction/blob/master/AcquisitionFunctions.py
#   - https://github.com/fmfn/BayesianOptimization/blob/master/bayes_opt/util.py 

def ucb(mean, std, xi=1.96):
    '''
    Upper confidence Bound
    Exploitation xi = 0.1
    Exploration xi = 10
    '''
    return mean + xi * std

def ei(mean, std, y_max, xi=0.0):
    '''
    Expected Improvement
    Exploitation xi = 0.0
    Exploration xi = 0.1
    '''
    a = (mean - y_max - xi)
    z = a / std
    return a * norm.cdf(z) + std * norm.pdf(z)

def poi (mean, std, y_max, xi=0.0):
    '''
    Probability of Improvement
    Exploitation xi = 0.0
    Exploration xi = 0.1
    '''
    z = (mean - y_max - xi)/std
    return norm.cdf(z)

def plot_convergence(Y, n_init=0):
    y = np.max(Y) - Y[n_init:]
    x = np.arange(1, 1+len(y))
    plt.plot(x, y, marker='x')
    plt.title('Convergence')