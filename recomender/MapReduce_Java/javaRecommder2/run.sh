javac -classpath $HADOOP_HOME/share/hadoop/common/hadoop-common-${version}.jar: \
 $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-${version}.jar: \
 $HADOOP_HOME/share/hadoop/common/lib/commons-cli-1.2.jar \
 Mapper2.java \
 Reducer2.java \
 MR2.java

jar -cvf mr2.jar *.class

hadoop jar mr2.jar MR1