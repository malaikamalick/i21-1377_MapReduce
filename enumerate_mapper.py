#!/usr/bin/env python3

import sys


for line in sys.stdin:
    article_id, text = line.strip().split('\t')
    print(f"{article_id}\t{text}")
        

