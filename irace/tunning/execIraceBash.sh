#!/bin/bash

name_file=$1
iter_lower=$2
iter_upper=$3
algorithm_folder=$4
scenario_name=$5
oppositeFlag=$6
nameinstances=$7


for i in $(eval echo {$iter_lower..$iter_upper})
do 
    R < iraceRun.R --no-save --args $i $algorithm_folder $scenario_name $oppositeFlag $nameinstances > ${name_file}_${i}.txt
done
