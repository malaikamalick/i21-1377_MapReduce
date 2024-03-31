#!/usr/bin/env python3

import sys

for line in sys.stdin:
	if line.startswith('-'):
		word, count, id = line.split('\t')
		print(f"{word}\t{count}\t{id}")	
