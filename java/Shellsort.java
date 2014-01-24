public class Shellsort {

	public static void print_array(Comparable[] a) {
    	StringBuilder uh = new StringBuilder();
        for (Comparable letter : a) {
        	uh.append(" ");
        	uh.append(letter);
        }
        System.out.println(uh);
    }
	
	public static void main(String[] args) {
		Comparable[] a = {"S", "H", "E", "L", "L", "S", "O", "R", "T", "E", "X", "A", "M", "P", "L", "E"};
		int N = a.length;
		int h = 1;
		
		Stack<Integer> hstack = new Stack<Integer>();
		
		hstack.push(h);
		while (h < N/3) {
			
			h = 3*h + 1;
			hstack.push(h);
		}		
		
		while (hstack.isEmpty() == false) {
			h = hstack.pop();
			for (int i = h; i < N; i++) {
				for (int j = i; j >= h; j-=h) {
					int comp = a[j].compareTo(a[j-1]);
					if (comp <= -1) {
						Comparable tmp = a[j];
						a[j] = a[j-1];
						a[j-1] = tmp;
					}
					print_array(a);
				}
			}
			
		
		
		}
		
	}

}
