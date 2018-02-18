import numpy
import matplotlib
x=[2,1,3,4]
y=[5,6,3,4]
import matplotlib.pyplot as plt
fig, axScatter = plt.subplots(figsize=(500, 500))
axScatter.scatter(x, y)
plt.draw()
plt.show()
