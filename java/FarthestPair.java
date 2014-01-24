import java.util.Random;

/**
 * Created by ehrlichja on 1/22/14.
 */

/*
1.4.17 Farthest pair (in one dimension). Write a program that, given an array a[] of N double values, finds a
farthest pair : two values whose difference is no smaller than the the difference of any other pair (in absolute
value). The running time of your program should be linear in the worst case.
 */

public class FarthestPair {

    // Starting with the brute force method

    public static void main(String[] args) {


        Double[] a = new Double[1000];
        a = populate_array(a);

        Double[] b = new Double[10000];
        b = populate_array(b);

        Double[] c = new Double[100000];
        c = populate_array(c);


        Stopwatch timer = new Stopwatch();
        quadratic(a);
        System.out.println(timer.elapsedTime());
        quadratic(b);
        System.out.println(timer.elapsedTime());
        quadratic(c);
        System.out.println(timer.elapsedTime());


        // On to the divide-and-conquer method

        Stopwatch timer2 = new Stopwatch();

        Double answer = linear(a, 0, 1000-1);
        System.out.println(timer2.elapsedTime());
        answer = linear(b, 0, 10000-1);
        System.out.println(timer2.elapsedTime());
        answer = linear(c, 0, 100000-1);
        System.out.println(timer2.elapsedTime());


    }

    public static Double linear(Double[] a, int lo, int hi) {
        if (lo == hi) {
            Double biggest_difference = Math.abs(a[0] - a[lo]);
            Double biggest_difference_x = a[0];
            Double biggest_difference_y = a[lo];

            for (int i = 0; i < a.length; i++) {
                Double difference = Math.abs(a[i] - a[lo]);
                if (difference > biggest_difference) {
                    biggest_difference = difference;
                    biggest_difference_x = a[i];
                    biggest_difference_y = a[0];
                }
            }
            return biggest_difference;


        } else {

            int mid = lo + (hi - lo) / 2;
            Double left = linear(a, lo, mid);
            Double right = linear(a, mid+1, hi);
            if (left > right) {
                return left;
            } else {
                return right;
            }
        }

    }

    public static void quadratic(Double[] a) {
        Double biggest_difference = Math.abs(a[0] - a[1]);
        Double biggest_difference_x = a[0];
        Double biggest_difference_y = a[1];

        for (int x = 0; x < a.length; x++) {
            for (int y = 1; y < a.length; y++) {
                Double difference = Math.abs(a[x] - a[y]);
                if (difference > biggest_difference) {
                    biggest_difference = difference;
                    biggest_difference_x = a[x];
                    biggest_difference_y = a[y];
                }
            }
        }

        StdOut.print(biggest_difference);
        StdOut.print(" from ");
        StdOut.print(biggest_difference_x);
        StdOut.print(" and ");
        StdOut.print(biggest_difference_y);
        StdOut.print("\n");
    }

    private static Double[] populate_array(Double[] a) {

        Random rando = new Random();

        for (int i = 0; i < a.length; i++) {
            a[i] = rando.nextDouble();
        }

        return a;
    }

}
