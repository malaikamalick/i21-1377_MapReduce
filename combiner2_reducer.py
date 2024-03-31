#!/usr/bin/env python3

import sys
with open('/home/hadoopuser/i211377_A2/query_processing_file.txt', 'a') as f:
    for line in sys.stdin:
        line = line.strip()  # Remove leading and trailing whitespace
        if line:  # Check if the line is not empty after stripping whitespace
            print(f"+{line}")
            f.write(f"+{line}\n")  # Ensure a newline is added after each line

