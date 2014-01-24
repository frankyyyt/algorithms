package src.algorithms_java;

public class Algorithms {

	public static void main(String[] args) {
		String sentence = "So long!";
		String reversed_sentence = reverse_string(sentence);
		System.out.println(sentence);
		System.out.println(reversed_sentence);
	}

	public static String reverse_string(String sentence) {
		String result = "";
		int n = sentence.length();
		//System.out.println(n);
		while (n > 0) {
			String letter = sentence.substring(n-1, n);
			result = result + letter;
			n--;
		}
		return result;
	}
	
}
