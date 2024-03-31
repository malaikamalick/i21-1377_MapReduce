#!/usr/bin/env python3

import sys


articles = {}
word_enumerate = {}

for line in sys.stdin:
    line = line.strip()
    if line.startswith('*'):
        # Remove the * prefix and split the line into article ID and text
        article_id, text = line.split('\t', 1)
        article_id = article_id[1:]
        articles[article_id] = text
    elif line.startswith('-'):
        # Remove the - prefix and split the line into word and ID
        word, id = line.split('\t', 1)
        word = word[1:]
        word_enumerate[word]=id

unique_words = []
for id, text in articles.items():
    for word in text.split(' '):
        if word not in unique_words:
            unique_words.append(word)
word_freq = {}
for word in unique_words:
    for id, text in articles.items():
        if word in text.split(' '):
            if word not in word_freq:
                word_freq[word]=1
            else:
                word_freq[word]+=1
                
with open('/home/hadoopuser/i211377_A2/document_count.txt', 'w') as file:
    for id, text in articles.items():
        file.write(f"*{id}\t{text}\n")
    for word, freq in word_freq.items():
        if word in word_enumerate.keys():
            word_id = word_enumerate[word]
        file.write(f"-{word}\t{freq}\t{word_id}\n")
