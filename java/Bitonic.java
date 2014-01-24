/**
 * Created by ehrlichja on 1/20/14.
 */
public class Bitonic {

    /*
    1.4.20 Bitonic search. An array is bitonic if it is comprised of an increasing sequence of integers followed
    immediately by a decreasing sequence of integers. Write a program that, given a bitonic array of N distinct
    int values, determines whether a given integer is in the array. Your program should use ~3lg N compares in the
    worst case.
     */


    public static void main(String[] args) {
        Integer[] a = new Integer[100];
        a = create_bitonic_array(a);

        int query = 17;

        int lo = 0;
        int hi = a.length;
        bitonic_search(a, lo, hi, query);

    }

    private static void bitonic_search(Integer[] a, int lo, int hi, int query) {
        int mid = lo + (hi - lo) / 2;

        if (query > a[mid]) {
            return;
        }

        search_left(a, mid, query);

        search_right(a, mid, query);

    }

    private static void search_right(Integer[] a, int mid, int query) {

        for (int i = 0; i < mid; i++) {
            if (a[i] == query) {
                System.out.println("i found it");
            }
        }

    }

    private static void search_left(Integer[] a, int mid, int query) {
        for (int i = mid; i < a.length; i++) {
            if (a[i] == query) {
                System.out.println("i found it");
            }
        }
    }

    private static Integer[] create_bitonic_array(Integer[] a) {

        for (int i = 0; i < a.length/2; i++) {
            a[i] = i;
        }

        int x = 0;
        for (int i = a.length/2; i > 0; i--) {
            a[i + (x*2)] = i;
            x++;
        }

        return a;
    }


}
