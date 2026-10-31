import yaml
import os

def validate_dispatch_config():
    with open('.ai/agents/registry.yaml', 'r') as f:
        config = yaml.safe_load(f)
    # Add validation logic here
    return True