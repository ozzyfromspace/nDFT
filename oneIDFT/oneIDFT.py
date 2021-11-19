
import numpy as np
from oneDFT.oneDFT import oneDFT
from shared.kernel import kernel


def oneIDFT(data, x, period=2*np.pi):
  total = 0
  nSamples = len(data) # ensure this is odd
  N = int((nSamples - 1)/2)
  for kIndex in range(-N, N + 1):
    c_k = oneDFT(data, nSamples, kIndex)
    tempKernel = kernel(kIndex, x - np.pi, period, 1)
    total += c_k * tempKernel
  return total
