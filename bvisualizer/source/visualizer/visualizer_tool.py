import os as OS
import dotenv as DOTENV
import visualizer as V
import matplotlib.pyplot as PLT
import visualizer_handler as V_HANDLER
import utility.general_helper as H

DOTENV.load_dotenv('.env')

N_LIST_LOG_DIR = OS.getenv('N_LIST_LOG_DIR')

lst = [
    [{'fnc': 'Identity', 'iter': 5, 'lib': 'Ramda', 'size': 100},
     [['Mori', 4977], ['Lazy', 5434], ['Native', 5590], ['Immutable', 5078]]],
    [{'fnc': 'Identity', 'iter': 5, 'lib': 'Ramda', 'size': 700},
     [['Mori', 611], ['Lazy', 697], ['Native', 660], ['Immutable', 598]]],
    [{'fnc': 'Identity', 'iter': 3, 'lib': 'C++', 'size': 0},
     [['Mori', 21502], ['Lazy', 1898], ['Native', 49647], ['Immutable', 13887]]]
]

# V.visualize_sinle_planeIO()

# PLT.show()

# H.trace(list(V_HANDLER.prepareBenchmarkDataIO(N_LIST_LOG_DIR)))

H.trace(list(
    V_HANDLER.construct_fnc_to_structs_case(
        V_HANDLER.prepareBenchmarkDataIO(N_LIST_LOG_DIR), 'Identity', 'Mori')
))
