import numpy as np
from shared.kernel import kernel


def oneDFT(data, nSamples, freqVar):
  total = 0
  coefficient = (-1)**freqVar / nSamples
  for nIndex in range(0, nSamples):
    tempKernel = kernel(nIndex, freqVar, nSamples, -1)
    total += data[nIndex] * tempKernel
  return coefficient * total
  