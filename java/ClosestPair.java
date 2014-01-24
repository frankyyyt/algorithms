/**
 * Created by ehrlichja on 1/20/14.
 */

import java.util.Random;

/**
 * 1.4.16 Closest pair (in one dimension). Write a program that, given an array a[] of N double values,
 * finds a closest pair : two values whose difference is no greater than the the
 * difference of any other pair (in absolute value). The running time of your program should be
 * linearithmic in the worst case.
 */

public class ClosestPair {

    public int lowest_difference;

    public static void main(String[] args) {
        int N = 100;
        Integer[] a = new Integer[N];

        a = populate_array(a);

        quadratic(N, a);

        int lo = 0;
        int hi = N - 1;

        System.out.println("");
        //System.out.println("New way: " + Integer.toString(finder(a, lo, hi)));
        System.out.println(finder(a, lo, hi));

    }

    private static int finder(Integer[] a, int lo, int hi) {

       if (lo == hi) {
           int difference = 0;
           int lowest_difference = difference;
           for (int i = lo+1; i < a.length; i++) {
               difference = Math.abs(a[lo] - a[i]);
               if (difference < lowest_difference) {
                   difference = lowest_difference;
               }

           }
           return lowest_difference;
       }

       int mid = lo + (hi - lo) / 2;

       int left_lowest = finder(a, lo, mid);
       int right_lowest = finder(a, mid+1, hi);

       if (left_lowest < right_lowest) {
           return left_lowest;
       } else {
           return right_lowest;
       }


    }


    private static void quadratic(int N, Integer[] a) {
        int lowest_found = Math.abs(a[0] - a[1]);
        int lowest_i = 0;
        int lowest_j = 1;

        // This is quadratic (N^2 running) time.
        // TODO: change to be linearithmic (N log N)

        for (int i = 0; i < N; i++) {
            for (int j = i+1; j < N; j++) {
                int difference = Math.abs(a[i] - a[j]);
                if (difference < lowest_found) {
                    lowest_found = difference;
                    lowest_i = i;
                    lowest_j = j;
                }
            }
        }
        StdOut.print(Integer.toString(lowest_found) + " found as " + Integer.toString(a[lowest_i]) + " and " + Integer.toString(a[lowest_j]));

    }

    private static Integer[] populate_array(Integer[] a) {

        Random rando = new Random();

        for (int i = 0; i < a.length; i++) {
            a[i] = rando.nextInt();
        }

        return a;
    }

}
