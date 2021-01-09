import numpy as np
import matplotlib.pyplot as plt

class SimulatingAnneling:
    
    def __init__(self,epochs,  T = 1000000):
        self.T = T   # T is the temperate and i defined the defalt value of T is 1000
        self.epochs = epochs # epochs is number of iterations that how much time we want to interate loop 

    @staticmethod
    def huristic_function(x):
        return -1/89*x**2 + np.cos(x)**2 - np.sin(x*9)/5

    def sigmoid(self, E):    # sigmoid function 
        return 1/(1+np.exp(-1*(E/self.T))) 

    def algorithm(self):
        node = np.random.uniform(-1*10, 10, (1))   # genrating a number between -10 and 10
        bestnode = node
        ybestlist = []
        xbestlist = []

        for _ in range(self.epochs):
            j = 0
            while j < 16:
                j = j + 1
                neighbour = np.random.uniform(node-5, node+5, (1))   # genrating  neighbour between currentnode-2 to currentnode+2

                deltaE = self.huristic_function(neighbour) - self.huristic_function(node)

                if np.random.uniform(0,1,(1)) < self.sigmoid(deltaE):
                    node = neighbour
                    if self.huristic_function(node) > self.huristic_function(bestnode):
                        bestnode = node
                        y_value = self.huristic_function(bestnode)
                        ybestlist.append(y_value)
                        xbestlist.append(bestnode)

            self.T = self.T*0.9

        return xbestlist, ybestlist
