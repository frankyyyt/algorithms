package src.algorithms_java;

public class MergeTwo {

	public static void print_array(Comparable[] a) {
    	StringBuilder uh = new StringBuilder();
        for (Comparable letter : a) {
        	uh.append(" ");
        	uh.append(letter);
        }
        System.out.println(uh);
    }
	
	public static void sort(Comparable[] a, Comparable[] aux, int lo, int hi) {
		// Base case: we are working with one character in the array
		if (hi <= lo) {
			return;
		}
		
		int mid = lo + (hi - lo) / 2;
		
		// break off the left side recursively
		sort(a, aux, lo, mid);
		
		// break off the right side recursively
		sort(a, aux, mid+1, hi);
		
		// merge the two sorted halves together
		merge(a, aux, lo, mid, hi);
		
	}
	
	public static void merge(Comparable[] a, Comparable[] aux, int lo, int mid, int hi) {
		
		 for (int k = lo; k <= hi; k++) {
	            aux[k] = a[k]; 
	        }
		
		// Four cases here. Either:
		// The current left character is less than current right character (so take left)
		// The current right character is less than current left character (so take right)
		// Left side is all done (so take right)
		// Right side is all done (so take left)

		 // i and j are the markers for the two sides of the array we are merging
		 int i = lo;
		 int j = mid + 1;
		 
		 for (int k = lo; k <= hi; k++) {
			 if (i > mid) { // left has been exhausted
				 a[k] = aux[j];
				 j++;
			 } else if (j > hi) { // right has been exhausted
				 a[k] = aux[i];
				 i++;
			 } else if (aux[j].compareTo(aux[i]) < 0) { // right is less than left
				 a[k] = aux[j];
				 j++;
			 } else { // left is less than right
				 a[k] = aux[i];
				 i++;
			 }
		 }
		
		
	}
	
	public static void main(String[] args) {
		Comparable[] a = {"M", "E", "R", "G", "E", "S", "O", "R", "T", "E", "X", "A", "M", "P", "L", "E"};
		print_array(a);
		Comparable[] aux = new Comparable[a.length];

		sort(a, aux, 0, a.length-1);
		print_array(a);

	}

}
