import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String word1 = sc.next();
        String word2 = sc.next();
        
        char[] charWord1 = word1.toCharArray();
        char[] charWord2 = word2.toCharArray();

        Arrays.sort(charWord1);
        Arrays.sort(charWord2);

        String result = "Yes";
        if (word1.length() == word2.length()) {
            for (int i = 0; i < word1.length(); i++) {
                if (charWord1[i] != charWord2[i]) {
                    result = "No";
                    break;
                }
            }
        } else {
            result = "No";
        }
        

        System.out.println(result);
    }
}