#!/usr/bin/python3
###############################################################################
# This script is the command that is executed every run.
# Check the examples in examples/
#
# This script is run in the execution directory (execDir, --exec-dir).
#
# PARAMETERS:
# argv[1] is the candidate configuration number
# argv[2] is the instance ID
# argv[3] is the seed
# argv[4] is the instance name
# The rest (argv[5:]) are parameters to the run
#
# RETURN VALUE:
# This script should print one numerical value: the cost that must be minimized.
# Exit with 0 if no error, with 1 in case of error
###############################################################################

import os.path
import subprocess
import sys

def execute(instance, seed, ITER, params, exe):
  executable = os.path.expanduser(exe)
  command = [executable, instance, seed, params['--ants'], ITER, params['--alpha'], params['--beta'], params['--phMax'], params['--phMin'], params['--rho'] ]
  command += ['0','0','0','0','0','0','0','0']
  io = subprocess.Popen(command, stdout=subprocess.PIPE)
  out_, _ = io.communicate()
  result = out_.decode("utf-8").strip()
  return result

exe = "./AK"

ITER = '1000'

if len(sys.argv) < 5:
    print("\nUsage: ./target-runner.py <configuration_id> <instance_id> <seed> <instance_path_name> <list of parameters>\n")
    sys.exit(1)

# Get the parameters as command line arguments.
configuration_id = sys.argv[1]
instance_id = sys.argv[2]
seed = sys.argv[3]
instance = sys.argv[4]
conf_params = sys.argv[5:]

values = {}
while conf_params:
  param = conf_params.pop(0)
  value = conf_params.pop(0)
  values[param] = value

resultado = execute(instance, seed, ITER, values, exe)
print(resultado)
sys.exit(0)