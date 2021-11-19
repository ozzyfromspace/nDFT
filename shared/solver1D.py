
import numpy as np
from oneIDFT.oneIDFT import oneIDFT


def solver1D(data, x, period=2*np.pi):
  return oneIDFT(data, x, period)
