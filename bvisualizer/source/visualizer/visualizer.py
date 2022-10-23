import visualizer_handler as V_HANDLER
import utils.general_helper as H
import visualizer_configuration as CFG


def construct_model(correlation, lib):
  return H.compose(
    V_HANDLER.append_colorbar(lib),
    V_HANDLER.construct_correlation_surface(
      CFG.X, 
      CFG.Y
    )
  )(correlation)
