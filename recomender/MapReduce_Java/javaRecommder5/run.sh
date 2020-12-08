javac -classpath $HADOOP_HOME/share/hadoop/common/hadoop-common-${version}.jar: \
 $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-${version}.jar: \
 $HADOOP_HOME/share/hadoop/common/lib/commons-cli-1.5.jar \
 Mapper5.java \
 Reducer5.java \
 MR5.java

jar -cvf mr5.jar *.class

hadoop jar mr5.jar MR1