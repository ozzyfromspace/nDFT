
import numpy as np
from twoIDFT.twoIDFT import twoIDFT


def solver2D(data2D, x, y, periodX=2*np.pi, periodY=2*np.pi):
  return twoIDFT(data2D, x, y, periodX, periodY)
