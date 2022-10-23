from ctypes import Array
import visualizer_configuration as CFG


def construct_correlation_surface(x_plane: Array, y_plane: Array):
  return lambda z_correlation: CFG.AXES.plot_surface(
    x_plane, 
    y_plane, 
    z_correlation, 
    cmap=next(CFG.COLOR_MAPS)
  )


def append_colorbar(label: str):
  return lambda correlation_surface: CFG.FIGURE.colorbar(
    correlation_surface, 
    shrink=0.3,
    aspect=6,
    label=label, 
    anchor=(0.1, 0.1), 
    pad=0.01
  )
