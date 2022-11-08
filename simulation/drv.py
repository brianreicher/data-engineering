
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 13:50:40 2021
@author: rachlin
"""

import random as rnd
import matplotlib.pyplot as plt 
from collections import Counter
import seaborn as sns 
import copy
import numpy as np

def E(X):
    return X.E()

class DRV:
    
    def __init__(self, dist = {}, **kwargs):
        """ Constructor """
        self.dist = copy.deepcopy(dist)
        type = kwargs.get('type', 'discrete')

        if type == 'uniform':
            minval = kwargs.get('min', 0.0)
            maxval = kwargs.get('max', 1.0)
            bins = kwargs.get('bins', 10)
            self.dist = {k:1/bins for k in np.linspace(minval, maxval, bins)}

        elif type == 'normal':
            self.dist = {}
            mean = kwargs.get('mean', 0.0)
            stdev = kwargs.get('stdev', 1.0)
            bins = kwargs.get('bins', 20)

            sample = np.random.normal(mean, stdev, 100000)
            minval = min(sample)
            maxval = max(sample)
            vals = np.linspace(minval, maxval, bins)

            found = []
            for s in sample:
                finder = lambda x: abs(x - s)
                closest = min(vals, key=finder)
                found.append(closest)

            self.dist = DRV.toDRV(found).dist


    def add_value(self, x, p):
        """ Add a value to the DRV with probability p
        if value exists, probability is added """
        self.dist[x] = self.dist.get(x,0)+p
        
    def p(self, x):
        """ Get the probability associated with the value x """
        return self.dist.get(x, 0)

    def random(self):
        """ return a random value in accordance with the DRV probability 
        distribution """
        return rnd.choices(list(self.dist.keys()), list(self.dist.values()))[0]
            
    def E(self):
        """ Expected value """
        ev = 0.0
        for (x,p) in self.dist.items():
            ev += x * p
        return ev

    @staticmethod
    def toDRV(vals):
        """ Convert a series of values to the corresponding discrete random variable """
        cnt = Counter(vals)
        total = sum(dict(cnt).values())
        dist = {x:c/total for (x,c) in dict(cnt).items()}
        return DRV(dist)

    def apply(self, other, f):
        """ Apply a binary function to self and other """
        X = DRV()
        for x, px in self.dist.items():
            for y, py in other.dist.items():
                X.add_value(f(x,y), px*py)
        return X
    
    def applyscalar(self, a, f):
        """ Apply a binary function to self and a scalar a """
        X = DRV()
        for (x,p) in self.dist.items():
            X.add_value(f(x,a), p)
        return X

    def __add__(self, other):
        """ Add two discrete random variables """
        return self.apply(other, lambda x,y : x + y)

    def __radd__(self, a):
        """ Add a scalar, a, by the DRV """
        return self.applyscalar(a, lambda x, c: c + x)

    def __sub__(self, other):
        """ Subtract two discrete random variables  """
        return self.apply(other, lambda x, y: x - y)

    def __gt__(self, a):
        return self.applyscalar(a, lambda x, c: int(x>c))

    def __rsub__(self, a):
        """ Subtract scalar - drv """
        return self.applyscalar(a, lambda x, c: c - x)

    def __mul__(self, other):
        """ Multiply two discrete random variables  """
        return self.apply(other, lambda x, y: x * y)

    def __rmul__(self, a):
        """ Multiply a scalar, a, by the DRV """
        return self.applyscalar(a, lambda x, c: c * x)

    def __truediv__(self, other):
        """ Divide two discrete random variables  """
        return self.apply(other, lambda x, y: x / y)

    def __pow__(self, other):
        """ power function on two discrete random variables  """
        if type(other)=='DRV':
            return self.apply(other, lambda x,y : x ** y)
        else:
            return self.applyscalar(other, lambda x,a : x ** a)

    def __repr__(self):
        """ String representation of the DRV """
        
        xp = sorted(self.dist.items())
        
        rslt = ''
        for x,p in xp:
            rslt += str(x) + ' : '+ str(round(p,8)) + '\n'
        return rslt 

    def plot(self, title='', xscale='', yscale='', trials=100000, bins=20, show_cumulative = True):
        """ Display the DRV distribution """

        sample = [self.random() for i in range(trials)]

        # plt.yticks(np.arange(0, 1, step=0.1))
        plt.figure(figsize=(5,5), dpi=200)
        plt.yticks([0.0, .2, .4, .6, .8, 1.0])
        g = sns.displot(sample, kind='hist', stat='probability', bins=bins)
        g.fig.subplots_adjust(top=0.95, bottom=0.15)
        plt.title(title)
        plt.xlabel('value')
        # plt.yticks(np.arange(0,1,step=0.1))

        plt.grid()
        
        
        if xscale == 'log':
            plt.xscale(xscale)
            
        if yscale == 'log':
            plt.yscale(yscale)
          
        if show_cumulative: 
            plt.yticks([0.0, 0.25, 0.50, 0.75, 1.00])
            xp = sorted(list(self.dist.items()))
            xval = [t[0] for t in xp]
            pval = [t[1] for t in xp]
            totalp = 0.0
            pcumul = []
            for p in pval:
                totalp += p
                pcumul.append(totalp)
            sns.lineplot(x=xval, y=pcumul) 

        plt.show()