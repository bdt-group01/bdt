import java.io.IOException;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

//reduce的输入参数就是map输出参数，类型一致
public class Reducer3 extends Reducer<Text,Text,Text,Text>{
	private Text outKey = new Text();//输出的key
	private Text outValue = new Text();//输出的value
	
	//输入参数--key:列号 value：[行号_值,行号_值,行号_值,行号_值...]
	@Override
	protected void reduce(Text key, Iterable<Text> values, Reducer<Text, Text, Text, Text>.Context context)
			throws IOException, InterruptedException {
		StringBuilder sb = new StringBuilder();
		for(Text text:values) {//输入值合并
			//text:行号_值
			sb.append(text+",");
		}
		//如果有数据，必须去掉最后一个逗号
		String line=null;
		if (sb.toString().endsWith(",")) {
			line = sb.substring(0,sb.length() - 1);
		}
		outKey.set(key);
		outValue.set(line);
		context.write(outKey, outValue);
	}
}