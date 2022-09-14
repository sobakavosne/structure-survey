import os as OS
import sys as SYS
import numpy as NP
import pylab as PYLAB
import dotenv as DOTENV
import matplotlib as MPL
import matplotlib.pyplot as PLT
import matplotlib.animation as ANI
import mpl_toolkits.mplot3d.proj3d as PROJ3D

SYS.path.append('./bvisualizer')
import utils.general_helper as H


DOTENV.load_dotenv('.env')
PLT.style.use([PLT.style.available[0]])
MPL.rcParams['font.size'] = 8
MPL.rcParams['axes.edgecolor'] = 'black'
# MPL.rcParams['figure.autolayout'] = True
# MPL.rcParams['figure.constrained_layout.use'] = True
# MPL.rcParams['figure.dpi'] = 300

ITER_MAX = int(OS.getenv('ITER_MAX'))
ITER_STEP = int(OS.getenv('ITER_STEP'))
STRUCT_MAX = int(OS.getenv('STRUCT_MAX'))
STRUCT_STEP = int(OS.getenv('STRUCT_STEP'))


def visualize_sinle_planeIO():
  fig = PLT.figure(figsize=(12, 12))

  ax = fig.add_subplot(projection='3d')

  PLT.subplots_adjust(right=1, left=0.03, bottom=0.00,
                        top=1, wspace=0.0, hspace=0.0)

  x = NP.arange(100, 1100, 100)   # structure size axe
  y = NP.arange(1, 11, 1)          # iteration axe

  X, Y = NP.meshgrid(x, y)

  Z1 = NP.array([
    # [ 42577, 28941, 17747, 16104, 12126, 9241, 8751, 7990, 6775, 6184],
    [ 22681, 14165, 9174, 6672, 5522, 4606, 4003, 3428, 3072, 2667],
    [ 18546, 9223, 6079, 4657, 3689, 3060, 2635, 2260, 2011, 1785],
    [ 14065, 6961, 4601, 3498, 2643, 2254, 2023, 1608, 1481, 1319],
    [ 10295, 5733, 3968, 2674, 2137, 1703, 1460, 1405, 1120, 1042],
    [ 8772, 4244, 2711, 2201, 1638, 1439, 1280, 1087, 1027, 786],
    [ 7430, 3447, 2583, 1947, 1515, 1234, 1084, 937, 851, 733],
    [ 6385, 3367, 2290, 1706, 1308, 1149, 929, 863, 756, 569],
    [ 5944, 2939, 1984, 1484, 1175, 979, 805, 736, 674, 595],
    [ 5174, 2583, 1684, 1160, 1038, 952, 815, 707, 631, 475],
    [ 5155, 2179, 1706, 1285, 1034, 858, 740, 639, 558, 511]
  ])

  # Z1 = NP.array([
  #   [ 22681, 14165],
  #   [ 18546, 9223],
  #   [ 14065, 6961],
  #   [ 10295, 5733],
  #   [ 8772, 4244],
  #   [ 7430, 3447],
  #   [ 6385, 3367],
  #   [ 5944, 2939],
  #   [ 5174, 2583],
  #   [ 5155, 2179]
  # ])

  Z2 = NP.array([
    # [ 72361, 36007, 23976, 17803, 13808, 11248, 9723, 8535, 7582, 6849],
    [ 19563, 9903, 6399, 4821, 3978, 3210, 2832, 2403, 2129, 1894],
    [ 11990, 5015, 3410, 2691, 2237, 1854, 1730, 1497, 1265, 1084],
    [ 7626, 4269, 2604, 2081, 1480, 1540, 1213, 1037, 951, 817],
    [ 5826, 3098, 2235, 1258, 1048, 1150, 886, 852, 659, 638],
    [ 4977, 2519, 1653, 1320, 1050, 909, 738, 618, 598, 515],
    [ 4197, 1915, 1302, 1064, 602, 628, 611, 493, 461, 398],
    [ 3316, 1794, 1176, 899, 627, 372, 432, 376, 401, 355],
    [ 2377, 1319, 865, 721, 670, 493, 450, 403, 362, 157],
    [ 2552, 1284, 665, 562, 569, 458, 390, 337, 286, 256],
    [ 2200, 1098, 731, 615, 482, 383, 318, 280, 256, 203]
  ])

  # Z2 = NP.array([
  #   [ 19563, 9903],
  #   [ 11990, 5015],
  #   [ 7626, 4269],
  #   [ 5826, 3098],
  #   [ 4977, 2519],
  #   [ 4197, 1915],
  #   [ 3316, 1794],
  #   [ 2377, 1319],
  #   [ 2552, 1284],
  #   [ 2200, 1098]
  # ])

  # Z3 = NP.array([
  #   [20,  19,  19,  18,  17,  17,  15,  17,  18,  19],
  #   [20,  19,  19,  18,  17,  17,  15,  17,  18,  19],
  #   [20,  9,  8,  6, 18, 10, 12, 14, 16, 18],
  #   [20,  17,  16,  9, 20, 21, 25, 30, 35, 40],
  #   [20,  17,  18, 14, 20, 21, 25, 30, 35, 40],
  #   [20,  17, 10, 14, 15, 15, 25, 30, 50, 55],
  #   [20,  17, 12, 14, 15, 15, 25, 30, 58, 64],
  #   [20,  17, 14, 21, 28, 35, 52, 59, 66, 73],
  #   [20,  17, 16, 24, 32, 40, 58, 66, 74, 82],
  #   [20,  17, 18, 27, 36, 45, 64, 73, 82, 91]
  # ])
  # Z4 = NP.array([
  #   [30,  19,  19,  18,  17,  17,  15,  17,  18,  19],
  #   [30,  19,  19,  18,  17,  17,  15,  17,  18,  19],
  #   [30,  9,  8,  6, 18, 10, 12, 14, 16, 18],
  #   [30,  27,  16,  9, 20, 21, 25, 30, 35, 40],
  #   [30,  27,  18, 14, 20, 21, 25, 30, 35, 40],
  #   [30,  27, 20, 24, 25, 15, 25, 30, 70, 75],
  #   [30,  27, 22, 24, 25, 15, 25, 30, 78, 84],
  #   [30,  27, 24, 31, 38, 35, 52, 59, 76, 83],
  #   [30,  27, 26, 34, 42, 50, 78, 86, 94, 100],
  #   [30,  27, 28, 37, 46, 55, 74, 83, 92, 100]
  # ])

  surf1 = ax.plot_surface(X, Y, Z1, cmap=PLT.cm.cividis)
  surf2 = ax.plot_surface(X, Y, Z2, cmap=PLT.cm.inferno)
  # surf3 = ax.plot_surface(X, Y, Z3, cmap=PLT.cm.viridis)
  # surf4 = ax.plot_surface(X, Y, Z4, cmap=PLT.cm.hot)
  # surf5 = ax.plot_surface(X, Y, Z5, cmap=PLT.cm.magma)
  # surf6 = ax.plot_surface(X, Y, Z6, cmap=PLT.cm.plasma)
  
  ax.set_xlabel('x', labelpad=5)
  ax.set_ylabel('y', labelpad=5)
  ax.set_zlabel('z', labelpad=5)
  
  # ax.text(8, 10, 100, 'annotate', color='k')
  
  fig.colorbar(surf1, shrink=0.4, aspect=6,label='Surface 1', anchor=(0.5, 0.5), pad=0.04)
  fig.colorbar(surf2, shrink=0.4, aspect=6,label='Surface 2', anchor=(1.5, 0.5), pad=0.03)
  # fig.colorbar(surf3, shrink=0.4, aspect=6,label='Surface 3', anchor=(2.0, 0.5), pad=0.02)
  # fig.colorbar(surf4, shrink=0.4, aspect=6,label='Surface 4', anchor=(3.0, 0.5), pad=0.01)
  
  # ani = ANI.FuncAnimation(fig, V_HELPER.updateAnimation, 100, fargs=(
  #     [X, Y, Z1], surf1), interval=10000/100, blit=False)
  
  x2, y2, _ = PROJ3D.proj_transform(0, 0, 10, ax.get_proj())
  
  annotation_label = PYLAB.annotate(
      "this",
      xy=(x2, y2), xytext=(-30, 40),
      textcoords='offset points', ha='right', va='bottom', fontsize=10,
      # bbox=dict(boxstyle='round,pad=0.5', fc='yellow', alpha=0.5),
      # arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0')
      arrowprops=dict(headlength=10,connectionstyle='angle3'),
      # xycoords=("data")
  )
  
  def update_position(e):
      x2, y2, _ = PROJ3D.proj_transform(0, 0, 10, ax.get_proj())
      annotation_label.xy = x2, y2
      annotation_label.update_positions(fig.canvas.renderer)
      fig.canvas.draw()
  
  fig.canvas.mpl_connect('button_release_event', update_position)
  
  # PLT.axis('off')
  # PLT.show()
