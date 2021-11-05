import numpy as np


def fn2Arr(fn, nSamples=37, start=0, end=2*np.pi):
  arr = np.zeros(nSamples, complex)
  tempXVal = start
  delta = (end - start)/nSamples

  for nIndex in range(0, nSamples):
    arr[nIndex] = fn(tempXVal)
    tempXVal += delta
  return arr
