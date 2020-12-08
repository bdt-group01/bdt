import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.List;

import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Mapper.Context;

public class Mapper5  extends Mapper<LongWritable,Text,Text,Text>{
	private Text outKey = new Text();//输出的key
	private Text outValue = new Text();//输出的value
	
	private List<String> cacheList=new ArrayList<String>();
	
	private DecimalFormat df =new DecimalFormat("0.00");//定义输出格式，保留2位小数
	
	//覆写Mapper类的初始化方法，在map()方法之前执行
	@Override
	protected void setup(Context context)
			throws IOException, InterruptedException {
		super.setup(context);
		//通过输入流将全局缓存中的第二个矩阵读入List<String>中
		FileReader fs=new FileReader("itemUserScore3");
		BufferedReader br=new BufferedReader(fs);//字符缓冲输入流
		
		//每行格式 行<tab>列_值,列_值,列_值,列_值
		String line=null;
		while((line=br.readLine())!=null) {
			cacheList.add(line);//第二个矩阵以行为单位放入List容器中
		}
		
		fs.close();
		br.close();//关闭流
	}
	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, Text>.Context context)
			throws IOException, InterruptedException {
		String item_matrix1=value.toString().split("\t")[0];
		String[] user_score_array_matrix1=value.toString().split("\t")[1].split(",");
		
		for(String line:cacheList) {
			String item_matrix2=line.toString().split("\t")[0];
			String[] user_score_array_matrix2=line.toString().split("\t")[1].split(",");
			
			//如果物品ID相同
			if (item_matrix1.equals(item_matrix2)) {
				//遍历matrix1的列 相似度矩阵 * 评分矩阵=推荐矩阵
				for(String user_score_matrix1:user_score_array_matrix1) {
					boolean flag=false;
					String user_matrix1=user_score_matrix1.split("_")[0];
					String score_matrix1=user_score_matrix1.split("_")[1];
					
					//遍历matrix2的列 评分矩阵
					for(String user_score_matrix2:user_score_array_matrix2) {
						String user_matrix2=user_score_matrix2.split("_")[0];
						if(user_matrix1.equals(user_matrix2)) {
							flag=true;
						}
					}
					
					if (flag==false) {//用户没有对该物品产生过行为，可以输出到最终的推荐列表
						outKey.set(user_matrix1); 
						outValue.set(item_matrix1+"_"+score_matrix1);
						context.write(outKey, outValue);
					}					
				}
			}
		}
	}	
}