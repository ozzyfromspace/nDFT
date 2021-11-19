
import numpy as np
from oneDFT.oneDFT import oneDFT
from shared.kernel import kernel


def twoDFT(data2D, alpha, beta):
  data2DShape = np.shape(data2D)
  yDim = data2DShape[0]
  xDim = data2DShape[1]
  total = 0
  coefficient = (-1)**beta / yDim
  for wIndex in range(0, yDim):
    data1D = data2D[wIndex]
    DFT_data1D = oneDFT(data1D, xDim, alpha)
    tempKernel = kernel(wIndex, beta, yDim, -1)
    total += DFT_data1D * tempKernel
  return coefficient * total
