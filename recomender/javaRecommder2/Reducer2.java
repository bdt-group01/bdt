import java.io.IOException;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class Reducer2  extends Reducer<Text,Text,Text,Text>{
	private Text outKey = new Text();//输出的key
	private Text outValue = new Text();//输出的value
	
	protected void reduce(Text key, Iterable<Text> values, Context context)
			throws IOException, InterruptedException {
		StringBuilder sb = new StringBuilder();
		for(Text value:values) {//输入值合并
			//text:行号_值
			sb.append(value+",");
		}
		//如果有数据，必须去掉最后一个逗号
		String line=null;
		if (sb.toString().endsWith(",")) {
			line = sb.substring(0,sb.length() - 1);
		}
		
		//输出 key:行 value:列_值，列_值，列_值，列_值
		outKey.set(key);
		outValue.set(line);
		context.write(outKey, outValue);
	}
}