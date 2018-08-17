import numpy as np  
import matplotlib.pyplot as plt  
def graph(formula, x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x, y)  
    plt.show()




graph('10*(55./3)**2 + 5*(115./3)+x*0', range(10, 20))