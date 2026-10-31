import yaml
import os
from datetime import datetime

def load_ledger():
    with open('.ai/agents/ledger.yaml', 'r') as f:
        return yaml.safe_load(f)

def update_ledger(ledger):
    with open('.ai/agents/ledger.yaml', 'w') as f:
        yaml.safe_dump(ledger, f)

def validate_ledger(ledger):
    required_fields = ['version', 'current_session', 'audit_trail', 'last_updated']
    for field in required_fields:
        if field not in ledger:
            raise ValueError(f'Missing required field: {field}')
    return True