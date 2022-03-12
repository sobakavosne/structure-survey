import os as OS
import sys as SYS
import numpy as NP
import pylab as PYLAB
import dotenv as DOTENV
import matplotlib as MPL
import matplotlib.pyplot as PLT
import visualizer_helper as V_HELPER
import matplotlib.animation as ANI
import mpl_toolkits.mplot3d.proj3d as PROJ3D

# SYS.path.append('./bvisualizer')
# import utility.general_helper as H


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

    x = NP.arange(0, 10, 1)
    y = NP.arange(0, 10, 1)

    X, Y = NP.meshgrid(x, y)
    Z1 = NP.array([
        [0,  0,  0,  0,  0,  0,  0,  0,  0,  0],
        [0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
        [0,  2,  4,  6,  8, 10, 12, 14, 16, 18],
        [0,  3,  6,  9, 12, 15, 18, 21, 24, 27],
        [0,  4,  8, 10, 10, 10, 15, 20, 32, 36],
        [0,  5, 10, 10, 10, 10, 15, 20, 40, 45],
        [0,  6, 12, 10, 10, 10, 15, 20, 48, 54],
        [0,  7, 14, 21, 28, 35, 42, 49, 56, 63],
        [0,  8, 16, 24, 32, 40, 48, 56, 64, 72],
        [0,  9, 18, 27, 36, 45, 54, 63, 72, 81]
    ])

    Z2 = NP.array([
        [10,  9,  9,  8,  7,  7,  5,  7,  8,  9],
        [10,  9,  9,  8,  7,  7,  5,  7,  8,  9],
        [10,  9,  8,  6, 18, 10, 12, 14, 16, 18],
        [10,  7,  6,  9, 12, 15, 18, 21, 24, 27],
        [10,  7,  8, 14, 15, 15, 15, 20, 32, 36],
        [10,  7, 10, 14, 15, 15, 15, 20, 40, 45],
        [10,  7, 12, 14, 15, 15, 15, 20, 48, 54],
        [10,  7, 14, 21, 28, 35, 42, 49, 56, 63],
        [10,  7, 16, 24, 32, 40, 48, 56, 64, 72],
        [10,  7, 18, 27, 36, 45, 54, 63, 72, 81]
    ])
    Z3 = NP.array([
        [20,  19,  19,  18,  17,  17,  15,  17,  18,  19],
        [20,  19,  19,  18,  17,  17,  15,  17,  18,  19],
        [20,  9,  8,  6, 18, 10, 12, 14, 16, 18],
        [20,  17,  16,  9, 20, 21, 25, 30, 35, 40],
        [20,  17,  18, 14, 20, 21, 25, 30, 35, 40],
        [20,  17, 10, 14, 15, 15, 25, 30, 50, 55],
        [20,  17, 12, 14, 15, 15, 25, 30, 58, 64],
        [20,  17, 14, 21, 28, 35, 52, 59, 66, 73],
        [20,  17, 16, 24, 32, 40, 58, 66, 74, 82],
        [20,  17, 18, 27, 36, 45, 64, 73, 82, 91]
    ])
    Z4 = NP.array([
        [30,  19,  19,  18,  17,  17,  15,  17,  18,  19],
        [30,  19,  19,  18,  17,  17,  15,  17,  18,  19],
        [30,  9,  8,  6, 18, 10, 12, 14, 16, 18],
        [30,  27,  16,  9, 20, 21, 25, 30, 35, 40],
        [30,  27,  18, 14, 20, 21, 25, 30, 35, 40],
        [30,  27, 20, 24, 25, 15, 25, 30, 70, 75],
        [30,  27, 22, 24, 25, 15, 25, 30, 78, 84],
        [30,  27, 24, 31, 38, 35, 52, 59, 76, 83],
        [30,  27, 26, 34, 42, 50, 78, 86, 94, 100],
        [30,  27, 28, 37, 46, 55, 74, 83, 92, 100]
    ])

    surf1 = ax.plot_surface(X, Y, Z1, cmap=PLT.cm.cividis)
    surf2 = ax.plot_surface(X, Y, Z2, cmap=PLT.cm.inferno)
    surf3 = ax.plot_surface(X, Y, Z3, cmap=PLT.cm.viridis)
    surf4 = ax.plot_surface(X, Y, Z4, cmap=PLT.cm.hot)
    # surf5 = ax.plot_surface(X, Y, Z5, cmap=PLT.cm.magma)
    # surf6 = ax.plot_surface(X, Y, Z6, cmap=PLT.cm.plasma)

    ax.set_xlabel('x', labelpad=5)
    ax.set_ylabel('y', labelpad=5)
    ax.set_zlabel('z', labelpad=5)

    # ax.text(8, 10, 100, 'annotate', color='k')

    fig.colorbar(surf1, shrink=0.4, aspect=6,label='Surface 1', anchor=(0.0, 0.5), pad=0.04)
    fig.colorbar(surf2, shrink=0.4, aspect=6,label='Surface 2', anchor=(1.0, 0.5), pad=0.03)
    fig.colorbar(surf3, shrink=0.4, aspect=6,label='Surface 3', anchor=(2.0, 0.5), pad=0.02)
    fig.colorbar(surf4, shrink=0.4, aspect=6,label='Surface 4', anchor=(3.0, 0.5), pad=0.01)

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
