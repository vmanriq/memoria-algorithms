# R < iraceRun.R --no-save --args 10 ./ak scenario.txt TRUE trainInstancesHARD.txt
# se necesita estar parado en la carpeta  tunners/irace/tunning
library('irace')
library('devtools')
load_all()

args <- commandArgs()

cat("Los commands Args son", args, "\n")
setwd(args[5])
#
seed <- args[4]

scenario <- readScenario(filename = args[6])
scenario$seed <- seed
scenario$OL <- args[7]
scenario$trainInstancesFile <- args[8]
irace.main(scenario = scenario)

