javac -classpath $HADOOP_HOME/share/hadoop/common/hadoop-common-${version}.jar: \
 $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapreduce-client-core-${version}.jar: \
 $HADOOP_HOME/share/hadoop/common/lib/commons-cli-1.3.jar \
 Mapper3.java \
 Reducer3.java \
 MR3.java

jar -cvf mr3.jar *.class

hadoop jar mr3.jar MR1