#!/usr/bin/env python3
import sys

articles = {}
word_count_id = {}

for line in sys.stdin:
    line = line.strip()
    if line.startswith('*'):
        # Remove the * prefix and split the line into article ID and text
        article_id, text = line.split('\t', 1)
        article_id = article_id[1:]
        articles[article_id] = text
    elif line.startswith('-'):
        word, count, id = line.split('\t')
        word = word[1:]
        word_count_id[word] = [id, count]
        
tf = {}
for id, text in articles.items():
    tf[id] = {}  # Initialize TF dictionary for each article
    for word in word_count_id.keys():
        tf[id][word] = 0  # Initialize TF for each word in the current article
        for value in text.split():
            if word == value:
                tf[id][word] += 1

        
        
tf_updated = {}

for key, value in tf.items():
    tf_updated[key] = {}
    for term, freq in value.items():
        if freq != 0:
            tf_updated[key][term] = freq


for key, value in tf_updated.items():
    for term, freq in value.items():
        if term in word_count_id.keys():
            value[term]/=int(word_count_id[term][1])
            
            
for key, value in tf_updated.items():
    for term, freq in list(value.items()):  # Use list() to create a copy for safe iteration
        if term in word_count_id.keys():
            # Divide the frequency by the value from word_count_id
            value[word_count_id[term][0]] = value.pop(term)


# Storing to a text file
with open('/home/hadoopuser/i211377_A2/IDF.txt', 'w') as file:
    for key, value in tf_updated.items():
        file.write(f"*{key}\t")
        for term, freq in value.items():
            file.write(f"({term},{freq}) ")
        file.write("\n")
    file.write("-")
    file.write(str(len(word_count_id)))
