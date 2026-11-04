import yaml
import os

# Load YAML with error handling
try:
    with open('.ai/agents/registry.yaml', 'r') as file:
        content = yaml.safe_load(file)
    # Write cleaned YAML
    with open('.ai/agents/registry.yaml', 'w') as file:
        yaml.safe_dump(content, file, default_flow_style=False, sort_keys=False)
    print("YAML cleanup successful. Backup saved to registry.yaml.backup")
    # Create backup
    os.rename('.ai/agents/registry.yaml', '.ai/agents/registry.yaml.backup')
except Exception as e:
    print(f"YAML cleanup failed: {str(e)}")