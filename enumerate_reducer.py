#!/usr/bin/env python3

import sys

articles = {}

for line in sys.stdin:
    article_id, text = line.strip().split('\t')
    if article_id not in articles:
        articles[article_id] = text

word_enumerate = {}
i = -1
for id, text in articles.items():
    for word in text.split(' '):
        if word not in word_enumerate:
            i+=1
            word_enumerate[word] = i

with open('/home/hadoopuser/i211377_A2/enumerates.txt', 'w') as file:
    # Write articles
    for id, text in articles.items():
        file.write(f"*{id}\t{text}\n")
    # Write word enumerations
    for word, _id in word_enumerate.items():
        file.write(f"-{word}\t{_id}\n")
