import numpy as np

from plot3d import plot3d
from shared.solver2D import solver2D


nSamplesX = 31 # this should always be odd!
nSamplesY = nSamplesX
X = np.linspace(0, 2, nSamplesX)
Y = np.linspace(0, 3, nSamplesY)


# Create some 2D test data to work with
def testFn(x, y): return np.sin(np.pi * x + 2 * np.pi * y / 3)
meshX, meshY = np.meshgrid(X, Y)
testData = testFn(meshX, meshY)
plot3d(X, Y, testFn)
print(testData)
print(np.shape(testData))


# Create a model based on the test data and use it to generate a 3D plot
def model(x, y): return solver2D(testData, x, y, 2, 3)

outputX = np.linspace(0, 2, 10 * nSamplesX)
outputY = np.linspace(0, 3, 10 * nSamplesY)

# print(f'the expected value at stated coordinate is {model(-2.684, 6)}')

plot3d(outputX, outputY, model)


