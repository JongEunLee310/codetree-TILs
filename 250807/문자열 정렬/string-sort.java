import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        char[] charString = s.toCharArray();
        
        Arrays.sort(charString);
        String newString = new String(charString);

        System.out.println(newString);

    }
}