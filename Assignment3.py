import pylab as pl
import numpy
from matplotlib import pyplot as plt

X = numpy.linspace(-5,5,11)
Y = 2*X**2-20

plt.plot(X, Y,color="r")
plt.show()