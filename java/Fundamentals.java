// Exercises from Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.

import java.util.ArrayList;
import java.util.Random;
import java.util.ArrayList;

public class Fundamentals {

	public static void main(String[] args) {
		
		
		// Exercise 1.1.15
//		int[] a = {0, 1, 2, 2, 4, 7, 0, 0, 0, 0, 0, 4, 4, 4};
//		histogram(a, 5);

		Point2d(3);
		
	}

	public static void Point2d(int N) {
		// generate N random points on the unit square
		
		Random randomizer = new java.util.Random();
		
		ArrayList<double[]> d = new ArrayList<double[]>();
		
		for (int i = 0; i <= N; i ++) {
			
			double x = randomizer.nextDouble();
			double y = randomizer.nextDouble();
			double[] point = {x, y};
			d.add(i, point);
		}
		
		// Find distance between closest two
		Object[] elements = d.toArray();
		for (int i = 0; i <= N; i ++) {
			System.out.println(elements[i][0]);
		}
		
	}
	
	public static void histogram(int[] a, int M) {
		int[] result = new int[M];
		for (int i = 0; i < a.length; i++) {
			if (a[i] < M) {
				result[a[i]] += 1;
			}
		}
		
		for (int i = 0; i < result.length; i++) {
			System.out.println(result[i]);
		}
		
	}
	
	
}
