import os as OS
import dotenv as DOTENV
import visualizer as V
import matplotlib.pyplot as PLT
import visualizer_handler as V_HANDLER
import utility.general_helper as H

DOTENV.load_dotenv('.env')

N_LIST_LOG_DIR = OS.getenv('N_LIST_LOG_DIR')

V.visualize_sinle_planeIO()

PLT.show()

# H.trace(
#   list(V_HANDLER.prepareBenchmarkDataIO(N_LIST_LOG_DIR))
# )

#H.trace(list(
#    V_HANDLER.construct_fnc_structures_case(V_HANDLER.prepareBenchmarkDataIO(N_LIST_LOG_DIR), 'Identity', 'Mori')
#))
