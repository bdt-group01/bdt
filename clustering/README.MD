Execuation Step:
1. Generate processed data. Since "mapreduceUserBehavior.txt" is a hardcode filename in kmeans.py, you dont need to modify it.
  cat "filename" | ./mapper_countFrequency.py | sort | ./reducer_countFrequency.py > mapreduceUserBehavior.txt 
  ex: cat userBehavior.csv | ./mapper_countFrequency.py | sort | ./reducer_countFrequency.py > mapreduceUserBehavior.txt 
  
2. Run kmeans algorithm. You need to set a "k" number in line 120
  python kmeans.py

3. NEED HELP!
  a. currently I randomly select k points as the initial centers, which may affect the accuracy and efficiency on clustering. Need improvement on that.
  b. for the k value, I select it based on experience. Need better algorithm to do the jobs.



Explaination:
The purpose of this project is to find the most loyal customers based on their latest purchase time and their purchase frequency. The first step is to use map reduce function to get their latest purhcase time and their purchase frequency. Then use kmeans algorithm to clusters the customer groups. Then we can clearly see the loyalty level of each customer groups on the graph 

Files:
MapReduce Program( mapper_countFrequency.py reducer_countFrequency.py )
Kmeans Algorithm( kmeans.py )
Initial Test Data ( userBehavior.csv)
Processed Data( mapreduceUserBehavior.txt )
Sample Result Image( result.png )
BehaviorTransformation&Hour.sql
