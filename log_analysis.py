# Log Analysis Script for Security Incident Detection
# Analyzes log files for potential security incidents
# Part of the cybersecurity-analysis-tool project

import sys
import re
from datetime import datetime

SECURITY_PATTERNS = [
    r'failed login',
    r'unauthorized access',
    r'permission denied',
    r'brute force',
    r'SQL injection',
    r'XSS attempt'
]

def analyze_log(filepath):
    """Analyze log file for security incidents."""
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
        print(f"Analyzing {len(lines)} log entries...")
        incidents = []
        for i, line in enumerate(lines, 1):
            for pattern in SECURITY_PATTERNS:
                if re.search(pattern, line, re.IGNORECASE):
                    incidents.append((i, pattern, line.strip()))
        print(f"Found {len(incidents)} potential security incidents.")
        return incidents
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return []

if __name__ == "__main__":
    if len(sys.argv) > 1:
        analyze_log(sys.argv[1])
    else:
        print("Usage: python log_analysis.py <logfile>")
