#!/usr/bin/env python3
"""
Apache Beam Code Practice Setup Script

This script validates the environment and provides guidance for setting up
Apache Beam for learning.
"""

import sys
import subprocess
import os

def check_python_version():
    """Check Python version requirement."""
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✓ Python version: {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"✗ Python version must be 3.8+, found {version.major}.{version.minor}.{version.micro}")
        return False

def check_apache_beam():
    """Check if Apache Beam is installed."""
    try:
        import apache_beam
        print(f"✓ Apache Beam version: {apache_beam.__version__}")
        return True
    except ImportError:
        print("✗ Apache Beam not installed")
        return False

def check_dependencies():
    """Check if required dependencies are installed."""
    required = ['jupyter', 'pandas', 'numpy']
    missing = []
    
    for package in required:
        try:
            __import__(package)
            print(f"✓ {package} installed")
        except ImportError:
            print(f"✗ {package} not installed")
            missing.append(package)
    
    return len(missing) == 0

def main():
    """Main setup validation."""
    print("=== Apache Beam Environment Validation ===\n")
    
    checks = [
        ("Python Version", check_python_version),
        ("Apache Beam", check_apache_beam),
        ("Dependencies", check_dependencies)
    ]
    
    all_passed = True
    for name, check in checks:
        print(f"\n{name}:")
        if not check():
            all_passed = False
    
    print("\n" + "="*50)
    if all_passed:
        print("✓ All checks passed - environment is ready!")
        print("\nNext steps:")
        print("1. Run: python3 scripts/generate_sample_data.py")
        print("2. Start with Lab 1: Environment Setup")
    else:
        print("✗ Some checks failed - please install missing dependencies")
        print("\nInstall missing packages:")
        print("pip install apache-beam[gcp] jupyter pandas numpy")

if __name__ == "__main__":
    main()