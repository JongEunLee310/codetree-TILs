import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word1 = sc.next();
        String word2 = sc.next();
        
        char[] charWord1 = word1.toCharArray();
        Arrays.sort(charWord1);
        String sortedWord1 = new String(charWord1);


        char[] charWord2 = word2.toCharArray();
        Arrays.sort(charWord2);
        String sortedWord2 = new String(charWord2);

        if (sortedWord1.equals(sortedWord2)) {
            System.out.println("Yes");
        } else {
            System.out.println("No");
        }
    }
}