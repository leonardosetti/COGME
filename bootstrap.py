import os
import subprocess

def main():
    # Load model artifacts
    artifact_dir = os.getenv('MODEL_ARTIFACTS', '/lab/FATEC/202602/ger_proj/COGME/artifacts')
    
    # Initialize training environment
    subprocess.run(['torchrun', '--nproc_per_node', '8', 'train.py',
                   f'--data-dir {artifact_dir}',
                   '--config config.json'], check=True)

if __name__ == '__main__':
    main()