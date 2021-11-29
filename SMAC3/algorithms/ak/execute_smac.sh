#!/bin/bash




for i in {0..1}
do 
    python ../../scripts/smac.py --scenario ./scenario.txt --verbose DEBUG --seed ${i} > normal_ak_${i}.txt | tee normal_ak_${i}.txt
done&

for i in {0..1}
do 
    python ../../scripts/smac.py --scenario ./scenario.txt --verbose DEBUG --seed ${i} --OL True --budget_prob_0 10 --prob_decay 0.99 > OL_PROB010_decay99_ak_${i}.txt | tee OL_PROB010_decay99_ak_${i}.txt
done&







