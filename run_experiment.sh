#!/bin/bash
#SBATCH --job-name=llm-security
#SBATCH --partition=c23g
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --gres=gpu:1
#SBATCH --mem=24G
#SBATCH --time=01:00:00
#SBATCH --output=logs/experiment_%j.out
#SBATCH --error=logs/experiment_%j.err

set -e

cd "$HOME/multi-agent-llm-security"

module load Python/3.11.5
source .venv/bin/activate

export OMP_NUM_THREADS=4
export TOKENIZERS_PARALLELISM=false

echo "Job ID: $SLURM_JOB_ID"
echo "Node: $(hostname)"
echo "GPU allocation:"
nvidia-smi -L

echo "Starting experiment..."
python experiment.py

echo "Experiment completed."
