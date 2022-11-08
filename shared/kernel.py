import numpy as np


def kernel(loopVar, staticVar, dataLen, sign=-1):
  return (np.e)**(sign * 2 * np.pi * 1j * loopVar * staticVar / dataLen)