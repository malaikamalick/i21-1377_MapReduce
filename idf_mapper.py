#!/usr/bin/env python3

import sys

for line in sys.stdin:
	line = line.strip()
	if line.startswith('*'):
		article_id, text = line.split('\t')
		print(f"{article_id}\t{text}")
	elif line.startswith('-'):
		word, count, id = line.split('\t')
		print(f"{word}\t{count}\t{id}")
