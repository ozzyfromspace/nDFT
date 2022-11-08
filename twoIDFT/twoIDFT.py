import numpy as np
from shared.kernel import kernel
from twoDFT.twoDFT import twoDFT


def twoIDFT(data2D, x, y, periodX=2*np.pi, periodY=2*np.pi):
  data2DShape = np.shape(data2D)
  vDim = data2DShape[0]
  uDim = data2DShape[1]

  N_x = int((uDim - 1)/2)
  N_y = int((vDim - 1)/2)
  vTotal = 0

  for vIndex in range(-N_y, N_y + 1):
    uTotal = 0 
    vKernel = kernel(vIndex, y, periodY, 1)
    for uIndex in range(-N_x, N_x + 1):
      c_uv = twoDFT(data2D, uIndex, vIndex)
      uKernel = kernel(uIndex, x, periodX, 1)
      uTotal += c_uv * uKernel
    vTotal += uTotal * vKernel
  return vTotal




