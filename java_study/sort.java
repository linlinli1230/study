package autofy;
//排序
import java.util.Arrays;

public class sort {
	public static void main(String[] args) {
		int []a= {5,56,12,84,26,18,65};
		//方法1
		Arrays.sort(a);
		for(int x:a) {
			System.out.print(x+" ");
		}
		System.out.println();
		//方法2
		for(int i=1;i<a.length ;i++) {
			for(int j=0;j<a.length-i;j++) {
				if(a[j]>a[j+1]) {
					int t=a[j];
					a[j]=a[j+1];
					a[j+1]=t;
				}
			}
		}for(int x:a) {
			System.out.print(x+" ");
	}

}
}
