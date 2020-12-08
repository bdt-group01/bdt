javac -classpath $HADOOP_HOME/share/hadoop/common/hadoop-common-${version}.jar: \
 $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-${version}.jar: \
 $HADOOP_HOME/share/hadoop/common/lib/commons-cli-1.2.jar \
 Mapper1.java \
 Reducer1.java \
 MR1.java

jar -cvf mr1.jar *.class

hadoop jar mr1.jar MR1