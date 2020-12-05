import java.io.IOException;
import java.util.HashMap;
import java.util.Map;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class Reducer1  extends Reducer<Text,Text,Text,Text>{
	private Text outKey = new Text();//输出的key
	private Text outValue = new Text();//输出的value
	
	@Override
	protected void reduce(Text key, Iterable<Text> values, Reducer<Text, Text, Text, Text>.Context context)
			throws IOException, InterruptedException {
		String itemID = key.toString();
		
		//Map<userID,score>
		Map<String,Integer> map = new HashMap<String,Integer>();
		for(Text value:values) {
			String userID=value.toString().split("_")[0];
			String score=value.toString().split("_")[1];
			
			if(map.get(userID) == null) {
				map.put(userID, Integer.valueOf(score));
			}else {
				Integer perScore = map.get(userID);
				map.put(userID, perScore+Integer.valueOf(score));//权重累加
			}
		}
		StringBuilder sBuilder = new StringBuilder();
		for (Map.Entry<String, Integer> entry:map.entrySet()) {
			String userID=entry.getKey();
			String score=String.valueOf(entry.getValue());
			sBuilder.append(userID+"_"+score+",");
		}
		
		String line=null;
		//去掉行末的逗号
		if (sBuilder.toString().endsWith(",")) {
			line = sBuilder.substring(0,sBuilder.length() - 1);
		}
		
		outKey.set(itemID);
		outValue.set(line);
		context.write(outKey, outValue);
	}
}