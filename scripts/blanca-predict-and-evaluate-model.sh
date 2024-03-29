#!/bin/bash
#SBATCH --nodes=1           # Number of requested nodes
#SBATCH --gres=gpu:v100
#SBATCH --ntasks=4          # Number of requested cores
#SBATCH --mem=32G
#SBATCH --time=12:00:00          # Max walltime              # Specify QOS
#SBATCH --qos=blanca-kann
#SBATCH --out=eval_igt.%j.out      # Output file name
#SBATCH --error=eval_igt.%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=michael.ginn@colorado.edu

# purge all existing modules
module purge
# Load the python module
module load anaconda
# Run Python Script
conda activate AutoIGT
cd "/projects/migi8081/AutoIGT/Automatic-IGT-Glossing/src"

for lang in arp git lez nyb ddo usp ntu
do
  for track in open closed
  do
    python3 token_class_model.py predict --lang $lang --track $track --pretrained_path "../src/$lang-$track/output"
  done
done
