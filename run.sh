hadoop fs -put /home/hadoopuser/i211377_A2/input.txt /Assignment2/enumerate_input.txt
hadoop jar /home/hadoopuser/hadoop-3.4.0/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar -input /Assignment2/enumerate_input.txt -output /Assignment2/enumerate_output -mapper enumerate_mapper.py -reducer enumerate_reducer.py -file /home/hadoopuser/i211377_A2/enumerate_mapper.py -file /home/hadoopuser/i211377_A2/enumerate_reducer.py
hadoop fs -put /home/hadoopuser/i211377_A2/enumerates.txt /Assignment2/doc_count_input.txt
hadoop jar /home/hadoopuser/hadoop-3.4.0/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar -input /Assignment2/doc_count_input.txt -output /Assignment2/doc_count_output -mapper doc_count_mapper.py -reducer doc_count_reducer.py -file /home/hadoopuser/i211377_A2/doc_count_mapper.py -file /home/hadoopuser/i211377_A2/doc_count_reducer.py
hadoop fs -put /home/hadoopuser/i211377_A2/document_count.txt /Assignment2/idf_input.txt
hadoop jar /home/hadoopuser/hadoop-3.4.0/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar -input /Assignment2/idf_input.txt -output /Assignment2/idf_output -mapper idf_mapper.py -reducer idf_reducer.py -file /home/hadoopuser/i211377_A2/idf_mapper.py -file /home/hadoopuser/i211377_A2/idf_reducer.py
hadoop fs -put /home/hadoopuser/i211377_A2/IDF.txt /Assignment2/indexer_input.txt
hadoop jar /home/hadoopuser/hadoop-3.4.0/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar -input /Assignment2/indexer_input.txt -output /Assignment2/indexer_output -mapper indexer_mapper.py -reducer indexer_reducer.py -file /home/hadoopuser/i211377_A2/indexer_mapper.py -file /home/hadoopuser/i211377_A2/indexer_reducer.py
hadoop fs -put /home/hadoopuser/i211377_A2/query.txt /Assignment2/query_input.txt
hadoop jar /home/hadoopuser/hadoop-3.4.0/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar -input /Assignment2/query_input.txt -output /Assignment2/query_reader_output -mapper query_reader_mapper.py -reducer query_reader_reducer.py -file /home/hadoopuser/i211377_A2/query_reader_mapper.py -file /home/hadoopuser/i211377_A2/query_reader_reducer.py
hadoop jar /home/hadoopuser/hadoop-3.4.0/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar -input /Assignment2/idf_input.txt -output /Assignment2/combiner1_output -mapper combiner1_mapper.py -reducer combiner1_reducer.py -file /home/hadoopuser/i211377_A2/combiner1_mapper.py -file /home/hadoopuser/i211377_A2/combiner1_reducer.py
hadoop fs -put /home/hadoopuser/i211377_A2/idf_vectors.txt /Assignment2/combiner2_input.txt
hadoop jar /home/hadoopuser/hadoop-3.4.0/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar -input /Assignment2/combiner2_input.txt -output /Assignment2/combiner2_output -mapper combiner2_mapper.py -reducer combiner2_reducer.py -file /home/hadoopuser/i211377_A2/combiner2_mapper.py -file /home/hadoopuser/i211377_A2/combiner2_reducer.py
hadoop fs -put /home/hadoopuser/i211377_A2/query_processing_file.txt /Assignment2/result_query_input.txt
hadoop jar /home/hadoopuser/hadoop-3.4.0/share/hadoop/tools/lib/hadoop-streaming-3.4.0.jar -input /Assignment2/result_query_input.txt -output /Assignment2/result_query_output -mapper result_query_mapper.py -reducer result_query_reducer.py -file /home/hadoopuser/i211377_A2/result_query_mapper.py -file /home/hadoopuser/i211377_A2/result_query_reducer.py
hadoop fs -cat /Assignment2/result_query_output/part-00000