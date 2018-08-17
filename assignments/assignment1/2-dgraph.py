import numpy as np  
import matplotlib.pyplot as plt  
def graph(formula, x_range):  
    x = np.array(x_range)  
    y = eval(formula)
    plt.plot(x, y)  
    plt.show()



graph('10*(((55/3)-(x/3))*((55/3)-(x/3))) + 5*((135/3)-(x/3))', range(10, 21))