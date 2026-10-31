import yaml
import os

def load_knowledge_base():
    with open('.ai/knowledge_base.yaml', 'r') as f:
        return yaml.safe_load(f)

def update_knowledge_base(kb):
    with open('.ai/knowledge_base.yaml', 'w') as f:
        yaml.safe_dump(kb, f)