import yaml
import sys
import os

def validate_agent_yaml(file_path):
    try:
        with open(file_path, 'r') as f:
            doc = yaml.safe_load(f)
        required_keys = ['name', 'version', 'layer', 'role', 'description']
        missing = [k for k in required_keys if k not in doc]
        if missing:
            print(f"🚨 Missing keys in {file_path}: {', '.join(missing)}")
            return False
        return True
    except Exception as e:
        print(f"❌ Error validating {file_path}: {str(e)}")
        return False

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    agent_dir = os.path.join(script_dir, '..', '.ai', 'agents')
    for root, _, files in os.walk(agent_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                if not validate_agent_yaml(file_path):
                    sys.exit(1)