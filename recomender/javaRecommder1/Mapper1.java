import java.io.IOException;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class Mapper1 extends Mapper<LongWritable,Text,Text,Text>  {
	private Text outKey = new Text();//输出的key
	private Text outValue = new Text();//输出的value
	
	/**
	 * key:1	2...
	 * value:A,1,1	C,3,5
	 */
	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, Text>.Context context)
			throws IOException, InterruptedException {
		String[] values = value.toString().split(",");
		String userID = values[0];
		userID = userID.substring(1, userID.length()-1);
		String itemID = values[1];
		itemID = itemID.substring(1, itemID.length()-1);
		String score = values[3];
		score = score.substring(1, score.length()-1);
        if(score.equals("pv")){
            score="1";
        }else if(score.equals("cart")){
            score="3";
        }else if(score.equals("fav")){
            score="5";
        }else if(score.equals("buy")){
            score="10";
        }
		
		outKey.set(itemID);
		outValue.set(userID+"_"+score);
		
		context.write(outKey, outValue);
	}
}