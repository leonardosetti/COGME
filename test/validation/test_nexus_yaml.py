import pytest
from scripts.validate_nexus_yaml import validate_agent_slugs

def test_agent_slugs():
    assert validate_agent_slugs() == []

def test_orchestrator_present():
    assert 'agent-orchestrator' in validate_agent_slugs()