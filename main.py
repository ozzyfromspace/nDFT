import numpy as np
from matplotlib.pyplot import grid, plot, show

from oneIDFT.oneIDFT import oneIDFT
from shared.fn2Arr import fn2Arr
from shared.solver import solver

nInputSamples = 51 # this must be an odd number
nOutputSamples = 180


def randomFn(x):
  if x < np.pi/2:
    return x
  elif x < np.pi:
    return (x**2)
  return 3


inputData = fn2Arr(randomFn, nInputSamples)
domainInput = np.linspace(0, 2*np.pi, nInputSamples)
domainOutput = np.linspace(0, 2*np.pi, nOutputSamples)


# Example usage
def model(x): return solver(inputData, x)
outArr = fn2Arr(model, nOutputSamples)


plot(domainOutput, outArr.real, 'r-')
plot(domainInput, inputData.real, 'b*')
grid(color='gray', linestyle='-', linewidth=0.5)
show()
