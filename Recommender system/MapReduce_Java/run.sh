
version='2.9.1'

javac -classpath $HADOOP_HOME/share/hadoop/common/hadoop-common-${version}.jar: \
 $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-${version}.jar: \
 $HADOOP_HOME/share/hadoop/common/lib/commons-cli-1.2.jar \
 Mapper1.java \
 Reducer1.java \
 MR1.java

jar -cvf mr1.jar *.class

hadoop jar mr1.jar MR1

javac -classpath $HADOOP_HOME/share/hadoop/common/hadoop-common-${version}.jar: \
 $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-${version}.jar: \
 $HADOOP_HOME/share/hadoop/common/lib/commons-cli-1.2.jar \
 Mapper2.java \
 Reducer2.java \
 MR2.java

jar -cvf mr2.jar *.class

hadoop jar mr2.jar MR2

javac -classpath $HADOOP_HOME/share/hadoop/common/hadoop-common-${version}.jar: \
 $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-${version}.jar: \
 $HADOOP_HOME/share/hadoop/common/lib/commons-cli-1.2.jar \
 Mapper3.java \
 Reducer3.java \
 MR3.java

jar -cvf mr3.jar *.class

hadoop jar mr3.jar MR3

javac -classpath $HADOOP_HOME/share/hadoop/common/hadoop-common-${version}.jar: \
 $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-${version}.jar: \
 $HADOOP_HOME/share/hadoop/common/lib/commons-cli-1.2.jar \
 Mapper4.java \
 Reducer4.java \
 MR4.java

jar -cvf mr4.jar *.class

hadoop jar mr4.jar MR4

javac -classpath $HADOOP_HOME/share/hadoop/common/hadoop-common-${version}.jar: \
 $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-${version}.jar: \
 $HADOOP_HOME/share/hadoop/common/lib/commons-cli-1.2.jar \
 Mapper5.java \
 Reducer5.java \
 MR5.java

jar -cvf mr5.jar *.class

hadoop jar mr5.jar MR5