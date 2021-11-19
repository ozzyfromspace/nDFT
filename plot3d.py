import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.ticker import LinearLocator


def plot3d(X, Y, fn):
  fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
  X, Y = np.meshgrid(X, Y)
  Z = fn(X, Y).real

  plt.xlabel("x")
  plt.ylabel("y")
  surf = ax.plot_surface(X, Y, Z, cmap=cm.rainbow, linewidth=0, antialiased=False)
  ax.zaxis.set_major_locator(LinearLocator(10))
  ax.zaxis.set_major_formatter('{x:.02f}')

  fig.colorbar(surf, shrink=0.5, aspect=5)

  plt.show()

