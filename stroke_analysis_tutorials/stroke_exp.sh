#!/bin/bash
#
#SBATCH --job-name=stroke_exp
#SBATCH --mem=20000                     # Job memory request
#SBATCH -t 6-23:59               # Time limit days-hrs:min:sec
#SBATCH -N 1                         # requested number of nodes (usually just 1)
#SBATCH -n 12                       # requested number of CPUs
#SBATCH -p scavenger-gpu       # requested partition on which the job will run
#SBATCH --gres=gpu:1               # gpu:[number_of_requested_gpus]
#SBATCH --exclude=dcc-tdunn-gpu-02,dcc-mastatlab-gpu-01,dcc-gehmlab-gpu-04,dcc-dhvi-gpu-01,dcc-dhvi-gpu-02,dcc-allenlab-gpu-03,dcc-allenlab-gpu-04,dcc-youlab-gpu-01
#SBATCH --output=stroke_exp.out
set -e
source ~/.bashrc
source activate neuroposelib
python stroke_exp.py