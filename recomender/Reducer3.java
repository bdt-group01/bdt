import java.io.IOException;
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.FileSystem;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class MR3 {
	//输入文件路径
	String inPath="/output/itemcf/part-r-00000";
	//输出文件路径
	String outPath="/output/itemcf/step3";
	//hdfs地址
	private static  String hdfs="hdfs://xxx.xxx.xxx.xxx:9000";
	
	public int run() throws IOException, ClassNotFoundException, InterruptedException {
		//创建job配置类
		Configuration conf = new Configuration ();
		//设置hdfs地址
		conf.set("fs.defaultFS", hdfs);
		//创建一个job实例
		Job job=Job.getInstance(conf,"step3");
		
		//设置job的主类
		job.setJarByClass(MR3.class);	
		//设置job的Mapper类和Reducer类
		job.setMapperClass(Mapper3.class);
		job.setReducerClass(Reducer3.class);
		
		//设置Mapper输出的类型
		job.setMapOutputKeyClass(Text.class);
		job.setMapOutputValueClass(Text.class);
		
		//设置Reducer输出的类型
		job.setOutputKeyClass(Text.class);
		job.setOutputValueClass(Text.class);
		
		FileSystem fs = FileSystem.get(conf);
		//设置输入和输出路径
		Path path = new Path(inPath);
		if (fs.exists(path)) {
			FileInputFormat.addInputPath(job, path);
		}
		Path outoutPath = new Path(outPath);
		fs.delete(outoutPath,true);//如果路径存在，那么删除
		
		FileOutputFormat.setOutputPath(job, outoutPath);
		
		return job.waitForCompletion(true)?1 : -1;//返回作业状态，1成功，-1失败
	}
	
	public static void main(String[] args) throws ClassNotFoundException, IOException, InterruptedException {
		int result = -1;//作业运行结果
		result=new MR3().run();
		if (result == 1) {
			System.out.println("Step3运行成功！");
		}else if (result == -1) {
			System.out.println("Step3运行失败！");
		}
	}
}