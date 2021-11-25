import subprocess
import random 
import os 


SEED = 3
NUMBER_OF_SEEDS = 5
ALGORITHM = '/home/manriq/Documents/universidad/TT/tunners/SMAC3/algorithms/ilsmkp/target_algorithm/ILSMKP'
INSTANCE_FOLDER = '/home/manriq/Documents/universidad/TT/tunners/SMAC3/algorithms/instances/testing/testing500'


random.seed(SEED)


def save_config_value(config, config_file_save):
    return


def get_best_config(config_file_save):
    return 


def edit_domain(domain, new_restriction, max_restrictions):
    return

#
# Función que permite ejecutar smac y obtener el output de este
#
# @param [<Type>] smac_path path donde se encuentra el script de smac
# @param [<Type>] scenario_path path donde se encuentra el archivo de escenario
# @param [<Type>] numero_parametros cantidad de parámetros que retornara smac
#
# @return [<Type>] Output final de smac el cual solo contiene los parametros encontrados y sus valores
#
def exec_smac(smac_path, scenario_path, numero_parametros):
    return subprocess.check_output(f"python {smac_path} --scenario {scenario_path} | tail -n{numero_parametros + 1}", shell=True)


#
# Función para ejecutar el algoritmo objetivo con los parámetros dados
#
# @param [str] algorithm ruta donde se encuentra el algoritmo a ejecutar
# @param [str] instance instancia con la cual se ejecutara el algoritmo
# @param [dict] params diccionario con los parámetros a utilizar para el algoritmo
# @param [int] seed semilla a utilizar para el algoritmo
#
# @return [<Type>] devuelve output del algoritmo 
#
def exec_algorithm(algorithm, instance, params, seed):
    cmd = [algorithm, instance, '0', '99999999', '0', str(seed)]
    for nombre, valor in params.items():
        cmd.append(f"-{nombre}")
        cmd.append(str(valor))
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                  universal_newlines=True)
    stdout_, stderr_ = p.communicate()
    return stdout_


#
# Función que permite transformar el output de smac en un diccionaro
#
# @param [<Type>] parameter output de smac que contiene solo los parámetros
#
# @return [<Type>] Diccionario donde la llave es el nombre del parámetro y el valor el valor de este
#
def params_to_dict(output_smac):
    output_params = output_smac.decode("utf-8").strip().split("\n")
    params_dic = {}
    for param in output_params:
        param_split = param.split(",")
        param_name = param_split[0]
        param_value = int(param_split[-1].split(":")[-1].replace('\'', ''))
        params_dic[param_name] = param_value
    return params_dic



def evaluate_params(algorithm, instance_folder, seeds_number, dic_params):
    for filename in os.listdir(instance_folder):
        instance = os.path.join(instance_folder, filename)
        if os.path.isfile(instance):
            values = []
            print(f"----------------- INSTANCE: {filename} ----------------------")
            for _ in range(seeds_number):
                instance_seed = random.randint(0, 9999)
                output = exec_algorithm(algorithm, instance, dic_params, instance_seed)
                value = output.strip().split(',')[-3]
                values.append(value)
                print(f"VALUE: {value} ; SEED: {instance_seed}")
            values = list(map(int, values))
            promedio = sum(values)/len(values)
            print(f"El promedio es {promedio}")
    return



#output_smac = exec_smac('smac_algorithm/scripts/smac', 'ilsmkp/scenario.txt ', 1)

#dic_params = params_to_dict(output_smac)

param_values = [182, 472]
param_dics = []

for value in param_values:
    param_dics.append({"param1":value})

for dic_params in param_dics:
    print(f"Parámetros obtenidos por SMAC {dic_params}")
    evaluate_params(ALGORITHM, INSTANCE_FOLDER, NUMBER_OF_SEEDS, dic_params)
    print("\n\n")
