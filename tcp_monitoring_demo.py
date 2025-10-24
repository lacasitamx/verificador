#!/usr/bin/env python3
"""
TCP Monitoring Demo for speedtest-cli

This script demonstrates the new TCP monitoring capabilities added to speedtest-cli.
It shows how to use the --monitor-tcp flag to get detailed performance analysis.
"""

import subprocess
import sys
import time

def run_speedtest_with_monitoring():
    """Run speedtest with TCP monitoring enabled"""
    print("=== Speedtest-cli TCP Monitoring Demo ===")
    print()
    print("This demo shows the new TCP monitoring capabilities that help identify:")
    print("- Fastest periods during speed tests")
    print("- Pauses and timeouts in data transfer")
    print("- Detailed timing analysis for HTTP/2 connections")
    print()
    
    # Check if httpx is available
    try:
        import httpx
        print("✓ httpx is available - HTTP/2 support enabled")
    except ImportError:
        print("✗ httpx not available - HTTP/2 monitoring requires httpx")
        print("  Install with: pip install httpx")
        return
    
    print()
    print("Running speedtest with TCP monitoring...")
    print("=" * 50)
    
    # Run speedtest with monitoring
    cmd = [sys.executable, 'speedtest.py', '--http2', '--monitor-tcp', '--simple']
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        
        if result.returncode == 0:
            print(result.stdout)
            if result.stderr:
                print("Debug output:")
                print(result.stderr)
        else:
            print(f"Error running speedtest: {result.stderr}")
            
    except subprocess.TimeoutExpired:
        print("Speedtest timed out after 2 minutes")
    except Exception as e:
        print(f"Error: {e}")

def show_usage_examples():
    """Show usage examples for the new TCP monitoring feature"""
    print("\n=== Usage Examples ===")
    print()
    print("Basic TCP monitoring:")
    print("  ./speedtest.py --http2 --monitor-tcp")
    print()
    print("TCP monitoring with debug output:")
    print("  ./speedtest.py --http2 --monitor-tcp --debug")
    print()
    print("TCP monitoring with simple output:")
    print("  ./speedtest.py --http2 --monitor-tcp --simple")
    print()
    print("Note: --monitor-tcp automatically enables --http2 if not already specified")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        show_usage_examples()
    else:
        run_speedtest_with_monitoring()
        show_usage_examples()
