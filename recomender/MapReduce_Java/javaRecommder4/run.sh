javac -classpath $HADOOP_HOME/share/hadoop/common/hadoop-common-${version}.jar: \
 $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-${version}.jar: \
 $HADOOP_HOME/share/hadoop/common/lib/commons-cli-1.4.jar \
 Mapper4.java \
 Reducer4.java \
 MR4.java

jar -cvf mr4.jar *.class

hadoop jar mr4.jar MR1