import java.io.*;
import java.util.*;
public class TestClass {
	 public static void main(String[] args) { 
       
       Scanner sc = new Scanner(System.in);
       
       int n = sc.nextInt();
       int temp, sum=0;
       while (n!=0) {
         temp = n%10;
         sum = sum+temp;
         n= n/10;
       }
       
       System.out.println(sum);
       
		
	}
}