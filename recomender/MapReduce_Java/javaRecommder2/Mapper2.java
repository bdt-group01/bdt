import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.text.DecimalFormat;
import java.util.ArrayList;
import java.util.List;
import org.apache.hadoop.io.LongWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class Mapper2  extends Mapper<LongWritable,Text,Text,Text>{
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
		FileReader fs=new FileReader("itemUserScore");
		BufferedReader br=new BufferedReader(fs);//字符缓冲输入流
		
		//每行格式 行<tab>列_值,列_值,列_值,列_值
		String line=null;
		while((line=br.readLine())!=null) {
			cacheList.add(line);//第二个矩阵以行为单位放入List容器中
		}		
		fs.close();
		br.close();//关闭流
	}
	
	/**
	 * @param key:行号
	 * @param value:行<tab>列_值,列_值,列_值,列_值
	 */
	@Override
	protected void map(LongWritable key, Text value, Mapper<LongWritable, Text, Text, Text>.Context context)
			throws IOException, InterruptedException {
		////左侧矩阵行
		String row_matrix1 = value.toString().split("\t")[0];
		////左侧矩阵 列_值（数组）
		String[] column_value_array_matrix1 = value.toString().split("\t")[1].split(",");
		
		double  denominator1 = 0;
		//计算空间距离--左侧矩阵
		for(String column_value : column_value_array_matrix1 ) {
			String score = column_value.split("_")[1];
			denominator1 += Double.valueOf(score) * Double.valueOf(score);//分值的平方进行累加
 		}
		denominator1=Math.sqrt(denominator1);//开根号
	
		for(String line:cacheList) {
			//右侧矩阵的行 List
			//每行格式 行<tab>列_值,列_值,列_值,列_值
			String row_matrix2 = line.toString().split("\t")[0];//行号
			//列_值（数组）
			String[] column_value_array_matrix2 = line.toString().split("\t")[1].split(",");
			
			double  denominator2 = 0;
			//计算空间距离--右侧矩阵
			for(String column_value : column_value_array_matrix2 ) {
				String score = column_value.split("_")[1];
				denominator2 += Double.valueOf(score) * Double.valueOf(score);//分值的平方进行累加
	 		}
			denominator2=Math.sqrt(denominator2);//开根号
			
			//2矩阵进行行相乘，得到的结果
			//注意：此时右矩阵已经转置，所以2矩阵行相乘，实际就是左矩阵行乘右矩阵列
			int numerator=0;
			//遍历左侧矩阵每一行的每一列
			for(String column_value_matrix1 :column_value_array_matrix1 ) {
				String column_matrix1 = column_value_matrix1.split("_")[0];//左矩阵列号
				String value_matrix1 = column_value_matrix1.split("_")[1];//左矩阵列值
				
				//遍历右侧矩阵每一行的每一列
				for(String column_value_matrix2 :column_value_array_matrix2 ) {
					String column_matrix2 = column_value_matrix2.split("_")[0];//右矩阵列号
					String value_matrix2 = column_value_matrix2.split("_")[1];//右矩阵列值
					//左右矩阵列号相等就相乘
					if (column_value_matrix2.startsWith(column_matrix1+"_")) {
						//两列值相乘，并累加
						numerator += Integer.valueOf(value_matrix2) * Integer.valueOf(value_matrix1);
					}				
				}
			}
			
			//计算余弦相似度
			double cos = numerator / (denominator1 * denominator2);
			if (cos == 0) {
				continue; //结果为0，跳过循环，不输出
			}
			
			//result是结果矩阵中的某个元素，坐标为 行column_matrix1 列 column_matrix2（因为右矩阵已经转置）
			//mapper阶段输出
			//输出格式 key:行号 value：列号_值
			outKey.set(row_matrix1); 
			outValue.set(row_matrix2+"_"+df.format(cos));
			context.write(outKey, outValue);
		}		
	}	
}