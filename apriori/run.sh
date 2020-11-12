input='../../data/apriori/input/categoriesItems'
output='../../data/apriori/output'

#rm -r ${output}/*

rm -r ${output}/1_1
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar \
-input ${input} \
-output ${output}/1_1 \
-mapper "./mapper_init.py ${output}/oneItemIndex.txt" \
-reducer ./reducer.py

rm -r ${output}/1_2
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar \
-input ${output}/1_1/part-00000 \
-output ${output}/1_2 \
-mapper "./mapper2.py ${output}/oneItemIndex.txt" \
-reducer ./reducer2.py
#
#
for i in {1..20}
do
    let "b=$i+1"
    rm -r "${output}/${b}_1"
    hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar \
    -input "${output}/${i}_2" \
    -output "${output}/${b}_1" \
    -mapper "./mapper.py " \
    -reducer ./reducer.py

    rm -r "${output}/${b}_2"
    hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.1.2.jar \
    -input "${output}/${b}_1/part-00000" \
    -output "${output}/${b}_2" \
    -mapper "./mapper2.py ${output}/oneItemIndex.txt" \
    -reducer ./reducer2.py
done
# cat ./output/part-00000 | sort -t$'\t' -k 2nr | head -n 100 > output.txt


