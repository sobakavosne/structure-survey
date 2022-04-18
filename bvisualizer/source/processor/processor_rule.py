# lambda rules for data unit
import sys as SYS


SYS.path.append('./bvisualizer')
import utils.general_helper as H


rule_lib = lambda struct_case: H.head(struct_case)['lib']

rule_fnc = lambda struct_case: H.head(struct_case)['fnc']

rule_iter = lambda struct_case: H.head(struct_case)['iter']

rule_size = lambda struct_case: H.head(struct_case)['size']

rule_fnc_lib = lambda struct_case: { 'fnc': H.head(struct_case)['fnc'], 'lib': H.head(struct_case)['lib'] }
