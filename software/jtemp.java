import java.util.*;
import java.io.*;
public class A{
	public static reader rd = new reader();
	public static void debug(String s){
		System.err.print(s);
	}
	public static void print(String s){
		System.out.print(s);
	}	
	public static void test_case(){	
		
	}   
	public static void main(String[] args) {	
		int t = rd.nextint();
		for(int i = 1;i<=t;i++){
			print("Case #"+i+": ");
			test_case();
		}
	}
}	    
class reader{
	public static BufferedReader rd = new BufferedReader(new InputStreamReader(System.in));
	public static String next(){
		try{
			return rd.readLine();
		}catch(Exception e){
			return "0";
		}
	}
	int nextint(){
		return Integer.parseInt(next());
	}
	int[] readr(int n){
		int arr[] = new int[n];
		for(int i = 0;i<n;i++){
			arr[i] = nextint();
		}
		return arr;
	}
}


