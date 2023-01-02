import numpy as np
from mayavi.mlab import *
from mpl_toolkits.mplot3d import axes3d

def test_surf():
    """Test surf on regularly spaced co-ordinates like MayaVi."""
    def f(x, y):
        sin, cos = np.sin, np.cos
        return sin(x + y) + sin(2 * x - y) + cos(3 * x + 4 * y)

    X, Y, Z = axes3d.get_test_data(0.05)
    Z = np.rollaxis(Z,0,2)
    X = np.rollaxis(X,0,2)
    Y = np.rollaxis(Y,0,2)
    x, y = np.mgrid[-7.:7.05:0.1, -5.:5.05:0.05]
    s = surf(x, y, f, warp_scale="auto", opacity=1)
    axes(xlabel='X', ylabel='Y', zlabel='Z')
    s1 = surf(X, Y, Z, warp_scale="auto", opacity=1)
    #cs = contour_surf(x, y, f, contour_z=0)
    return s


test_surf()
show()