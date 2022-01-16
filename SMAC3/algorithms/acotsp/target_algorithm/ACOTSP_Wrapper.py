import sys
import argparse
import os
import re
__copyright__ = "Copyright 2021, AutoML.org Freiburg-Hannover"
__license__ = "3-clause BSD"

from subprocess import Popen, PIPE


def get_optimum(instance):
    all_opts = {'a280': 2579, 'ali535': 202310, 'att48': 10628,
                'att532': 27686, 'bayg29': 1610, 'bays29': 2020, 'berlin52': 7542, 'bier127': 118282,
                'brazil58': 25395, 'brg180': 1950, 'burma14': 3323, 'ch130': 6110, 'ch150': 6528, 'd198': 15780,
                'd493': 35002, 'd657': 48912, 'd1291': 50801, 'd1655': 62128 }
    instance_name = instance.split('/')[-1].split('.')[0]
    return all_opts[instance_name]
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='wrapper acotsp')
    parser.add_argument('-algorithm', '--algorithm', action='store', dest='algorithm')
    parser.add_argument('-ls', '--ls', action='store', dest='ls')
    parser.add_argument('-alpha', '--alpha', action='store', dest='alpha')
    parser.add_argument('-beta', '--beta', action='store', dest='beta')
    parser.add_argument('-rho', '--rho', action='store', dest='rho')
    parser.add_argument('-ants', '--ants', action='store', dest='ants')
    parser.add_argument('-nnls', '--nnls', action='store', dest='nnls')
    parser.add_argument('-q0', '--q0', action='store', dest='q0')
    parser.add_argument('-dlb', '--dlb', action='store', dest='dlb')
    parser.add_argument('-rasranks', '--rasranks', action='store', dest='rasranks')
    parser.add_argument('-elitistants', '--elitistants', action='store', dest='elitistants')

    args, unkown = parser.parse_known_args()
    instance = unkown[0]
    seed = unkown[-1]
    instance_opt = get_optimum(instance)
    arguments_to_call = ['-r', '1', '--seed', seed, '-i', instance, '-o', str(instance_opt), '--quiet']
    all_arguments = ['algorithm', 'ls', 'alpha', 'beta', 'rho', 'ants', 'nnls', 'q0', 'dlb', 'rasranks', 'elitistants']
    for argument in all_arguments:
        value = getattr(args, argument)
        if value == None: continue

        if argument == 'algorithm':
            arguments_to_call.append(f"--{value}")
        else:
            arguments_to_call.append(f"--{argument}")
            arguments_to_call.append(value)


    cmd = ['./target_algorithm/acotsp']
    cmd += arguments_to_call
    io = Popen(cmd, stdout=PIPE)
    out_, err_ = io.communicate()
    result = out_.decode("utf-8").strip()
    best = re.findall(r'Best [-+0-9.e]+', result)[0].split(' ')[-1]
    updated_best = 100*(abs(instance_opt - float(best)))/instance_opt
    print(f"Result for SMAC: SUCCESS, -1, -1, {updated_best}, {seed}")
