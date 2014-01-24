// Insertion sort based on Algorithms, 4th Edition by Robert Sedgewick and Kevin Wayne.

package src.algorithms_java;

public class Insertion {

	public static void main(String[] args) {
		Comparable[] a = {5, 4, 3, 2, 1};
		
		int length = a.length;
		
		System.out.println("Before");
		for (int i = 0; i < length; i++) {	
			System.out.println(a[i]);
		}
		
		for (int i = 0; i < length; i++) {
			for (int j = i; j > 0 && a[j].compareTo(a[j-1]) < 0; j--) {
				exch(a, j, j-1);
			}
		}
		
		System.out.println("After");
		for (int i = 0; i < length; i++) {
			System.out.println(a[i]);
		}
		
	}
	
	private static void exch(Object[] a, int i, int j) {
        Object swap = a[i];
        a[i] = a[j];
        a[j] = swap;
    }

}
