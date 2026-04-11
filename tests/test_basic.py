"""
Basic tests for DevGuard Pro
Phase 5 - CI/CD Demo Tests
"""

def test_python_works():
    """Verify Python is working"""
    assert 1 + 1 == 2

def test_string_operations():
    """Verify string operations"""
    name = "DevGuard"
    assert name.lower() == "devguard"
    assert len(name) == 8

def test_list_operations():
    """Verify list operations"""
    items = ["ram", "disk", "cpu"]
    assert len(items) == 3
    assert "ram" in items

def test_imports_work():
    """Verify required modules can be imported"""
    import os
    import sys
    import subprocess
    assert os is not None
    assert sys is not None
