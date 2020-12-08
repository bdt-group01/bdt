Execuation Step:
1. Generate processed data. \
  cat "filename" | ./mapper_countFrequency.py | sort | ./reducer_countFrequency.py > "output_filename" \
  ex: cat userBehavior.csv | ./mapper_countFrequency.py | sort | ./reducer_countFrequency.py > mapreduceUserBehavior.txt 
2. Run kmeans algorithm. \
  In line 224, put the filename into the box.\
  In line 223, if you set 'cal_sc' = True, the program will calculate the best K value ranging from(2, 12). You can also change the range in line 226. The program will generate the graph showing the silhouette coefficients in the range and the result from K-Means \
  In line 223, if you set 'cal_sc' = False and set the k value, the program will only geneate the result from K-Means with given K value. \
  run "python kmeans.py"



Explaination:\
1. The purpose of this project is to find the most loyal customers based on their latest purchase time and their purchase frequency. The first step is to use map reduce function to get their latest purhcase time and their purchase frequency. Then use kmeans algorithm to clusters the customer groups. Then we can clearly see the loyalty level of each customer groups on the graph. 
2. The program is improved with K-Means++ and silhouette analysis.



Files: \
1. MapReduce Program( mapper_countFrequency.py reducer_countFrequency.py )\
2. Kmeans Algorithm( kmeans.py )\
3. Initial Test Data ( date_100k.csv)\
4. Processed Data( mapreduceUserBehavior_100k.txt mapReduce_processedData )\
5. Sample Result Image( kmean_result)\
6. Sample Kmeans++ Result( kmeans++_result) \
7. Sample Silhouette Coefficient Result( silhouette_coefficient_result) 
