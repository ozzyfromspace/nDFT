import numpy as np
from matplotlib.pyplot import grid, plot, show

from shared.fn2Arr import fn2Arr
from shared.solver1D import solver1D

nInputSamples = 51 # this must be an odd number
nOutputSamples = 180


def randomFn(x):
  if x < np.pi/2:
    return x
  elif x < np.pi:
    return (x**2)
  elif x < 3/2 * np.pi:
    return np.sin(7.2*x**2)
  return 3-x/2


inputData = fn2Arr(randomFn, nInputSamples)

print(inputData, np.shape(inputData))

domainInput = np.linspace(0, 2*np.pi, nInputSamples)
domainOutput = np.linspace(0, 2*np.pi, nOutputSamples)

# print(domainInput)


# Example usage
def model(x): return solver1D(inputData, x)
outArr = fn2Arr(model, nOutputSamples)


plot(domainOutput, outArr.real, 'r-')
plot(domainInput, inputData.real, 'b*')
grid(color='gray', linestyle='-', linewidth=0.5)
show()
