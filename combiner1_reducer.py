#!/usr/bin/env python3

import sys

word_count_id = {}

for line in sys.stdin:
	line = line.strip()
	if line.startswith('-'):
		word, count, id = line.split('\t')
		word_count_id[word] = [id, count]
		
with open('/home/hadoopuser/i211377_A2/query_processing_file.txt', 'a') as file:
    for key, value in word_count_id.items():
        file.write(f"{key}\t{value[1]}\t{value[0]}\n")
