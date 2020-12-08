import java.io.IOException;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class Mapper3 extends Mapper<LongWritable,Text,Text,Text> {
	private Text outKey = new Text();//输出的key
	private Text outValue = new Text();//输出的value
	
	/*
	 * 以第二个矩阵第一行为例 1 1_0,2_3,3_-1,4_2,5_3
	 * key:1 行号
	 * value:1 1_0,2_3,3_-1,4_2,5_3
	 */
	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, Text>.Context context)
			throws IOException, InterruptedException {
		String[] rowAndLine = value.toString().split("\t");//行号和列信息之间用tab分割
		
		String row = rowAndLine[0];//矩阵的行号
		String[] lines = rowAndLine[1].split(",");//把列信息按照逗号拆分
		
		//lines = ["1_0","2_3","3_-1","4_2","5_3"]，继续拆分列信息等到每列列号和列值，分隔符是下划线
		for(int i=0;i<lines.length;i++) {
			String column = lines[i].split("_")[0];//列号
			String valueStr = lines[i].split("_")[1];//列值
			
			//mapper阶段输出，把第二个矩阵转置
			//key:列号 value：行号_值
			outKey.set(column); 
			outValue.set(row+"_"+valueStr);
			context.write(outKey, outValue);
			
		}
	}
}