import java.util.Random;

/**
 *
 */

/**
 * @author ehrlichja
 *
 */

// Exercise 1.14.18
// Local minimum of an array. 
// Write a program that, given an array a[] of N distinct integers, finds a local minimum: an index i 
// such that both a[i] < a[i-1] and a[i] < a[i+1] (assuming the neighboring entry is in bounds). 
// Your program should use ~2 lg N compares in the worst case.

public class LocalMinimum {

    /**
     * @param args
     */
    public static void main(String[] args) {

        // Generate an array of random ints

        int lo = 0;
        int hi = 10000;
        int mid = hi / 2;

        int[] a = generate_integers(hi);

        find_local_minimum(a, hi, lo);



    }

    private static void find_local_minimum(int[] a, int hi, int lo) {

        int mid = lo + (hi - lo) / 2;

        if (mid+1 == hi) {
            return;
        }

        int right = a[mid+1];
        int left = a[mid-1];

        if (a[mid] < left && a[mid] < right) {
            System.out.println("Found one:");
            System.out.println(Integer.toString(left) + " " + Integer.toString(a[mid]) + " " + Integer.toString(right));
        }

        mid = lo + (hi - lo) / 2;

        find_local_minimum(a, hi, mid);
        find_local_minimum(a, mid, lo);
    }


    public static int[] shuffle(int[] a) {
        int N = a.length;
        for (int i = 0; i < N; i++) {  // Exchange a[i] with random element in a[i..N-1]
            int r = i + StdRandom.uniform(N-i);
            int temp = a[i];
            a[i] = a[r];
            a[r] = temp;
        }
        return a;
    }

    private static int[] generate_integers(int hi) {
        int[] a = new int[hi];

        Random generator = new Random();

        a[0] = generator.nextInt(500) + 1;

        for (int i = 1; i < a.length; i++) {
            a[i] = a[i-1] + 1;
        }

        a = shuffle(a);

        return a;

    }

}
