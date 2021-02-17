import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    // Complete the hourglassSum function below.
    static int hourglassSum(int[][] arr) {
        int[] Sum = new int[16];
        int p = 0;
        
        	for (int locX = 0; locX < 4; locX++) {
    		for (int locY = 0; locY < 4; locY++) {
    			Sum[p] = 0;	
    			for(int i = 0; i < 3; i++) {
    				for(int j = 0; j<3; j++) {
    					if(i == 1 && (j == 0 || j == 2))continue;
    					else Sum[p]+=arr[i+locX][j+locY];	
    				}
    			}
                p++;
    		}
    	}

        int high = Sum[0];
        for(int i = 1; i < 16; i++) {
            if(high <= Sum[i])
                high = Sum[i];
        }
        
        return high;
        
    }

    private static final Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) throws IOException {
        BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(System.getenv("OUTPUT_PATH")));

        int[][] arr = new int[6][6];

        for (int i = 0; i < 6; i++) {
            String[] arrRowItems = scanner.nextLine().split(" ");
            scanner.skip("(\r\n|[\n\r\u2028\u2029\u0085])?");

            for (int j = 0; j < 6; j++) {
                int arrItem = Integer.parseInt(arrRowItems[j]);
                arr[i][j] = arrItem;
            }
        }

        int result = hourglassSum(arr);

        bufferedWriter.write(String.valueOf(result));
        bufferedWriter.newLine();

        bufferedWriter.close();

        scanner.close();
    }
}
