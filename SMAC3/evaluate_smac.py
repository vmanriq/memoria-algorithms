import subprocess
import random 
import os



SEED = 3
NUMBER_OF_SEEDS = 5
ALGORITHM = '/home/manriq/Documents/universidad/TT/tunners/SMAC3/algorithms/ak/target_algorithm/AK'
INSTANCE_FOLDER = '/home/manriq/Documents/universidad/TT/tunners/SMAC3/algorithms/instances/testing/testingWeish'

random.seed(SEED)





def exec_algorithm(algorithm, instance, params, seed):
    TOTAL_EVAL = '3000'
    cmd = [algorithm, instance, str(seed), params['ants'], TOTAL_EVAL, params['alpha'], params['beta'], params['ph-max'], params['ph-min'], params['rho']]
    cmd += ['0','0','0','0','0','0','0','0']
    p = subprocess.Popen(cmd, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                  universal_newlines=True)
    stdout_, stderr_ = p.communicate()
    return stdout_.strip()



def evaluate_params(algorithm, instance_folder, seeds_number, params):
    for filename in os.listdir(instance_folder):
        instance = os.path.join(instance_folder, filename)
        if os.path.isfile(instance):
            values = []
            print(f"----------------- INSTANCE: {filename} ----------------------")
            for _ in range(seeds_number):
                instance_seed = random.randint(0, 9999)
                output = exec_algorithm(algorithm, instance, params, instance_seed)
                values.append(output)
                print(f"VALUE: {output} ; SEED: {instance_seed}")
            values = list(map(float, values))
            promedio = sum(values)/len(values)
            print(f"El promedio es {promedio}")
    return



#output_smac = exec_smac('smac_algorithm/scripts/smac', 'ilsmkp/scenario.txt ', 1)

#dic_params = params_to_dict(output_smac)

param_values = [{'alpha':'6', 'ants': '30', 'beta': '4.5', 'ph-max': '6', 'ph-min': '0.01', 'rho': '0.01'}]

for params in param_values:
    print(f"Parámetros obtenidos por SMAC {params}")
    evaluate_params(ALGORITHM, INSTANCE_FOLDER, NUMBER_OF_SEEDS, params)
    print("\n\n")
