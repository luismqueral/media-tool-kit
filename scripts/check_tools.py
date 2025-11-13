#!/usr/bin/env python3
"""
Check if required media processing tools are installed and accessible.
Run this to verify your environment is set up correctly.
"""
import subprocess
import sys
from pathlib import Path


def check_tool(command, name):
    """Check if a command-line tool is available."""
    try:
        result = subprocess.run(
            [command, "--version"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode == 0:
            version = result.stdout.split('\n')[0] if result.stdout else result.stderr.split('\n')[0]
            print(f"✓ {name}: {version}")
            return True
    except FileNotFoundError:
        print(f"✗ {name}: NOT FOUND")
        return False
    except Exception as e:
        print(f"✗ {name}: ERROR ({str(e)})")
        return False


def main():
    """Check all required tools."""
    print("Checking media processing tools...\n")
    
    tools = [
        ("ffmpeg", "FFmpeg"),
        ("convert", "ImageMagick"),
        ("sox", "SoX"),
        ("python3", "Python"),
    ]
    
    results = []
    for command, name in tools:
        results.append(check_tool(command, name))
    
    print("\n" + "=" * 50)
    if all(results):
        print("✓ All tools installed and ready!")
        return 0
    else:
        print("✗ Some tools are missing. See README.md for installation instructions.")
        return 1


if __name__ == "__main__":
    sys.exit(main())

