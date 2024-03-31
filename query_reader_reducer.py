#!/usr/bin/env python3

import sys

for line in sys.stdin:
	print(f"*{line}")
	with open('/home/hadoopuser/i211377_A2/query_processing_file.txt', 'w') as f:
	    f.write(f"*{line}")
	    f.write('\n')
