import matplotlib.pyplot as plt
import numpy as np 

class Graph:

	def __init__(self, func = lambda x: x, x_range = np.linspace(0, 5)):  
		self.func = func
		self.x_range = x_range
 

	def plot(self):
		y_range = []
		for i in self.x_range:
			y_range.append(self.func(i))
			
		plt.plot(self.x_range, y_range)
		plt.show()
