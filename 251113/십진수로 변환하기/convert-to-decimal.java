import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String binary = sc.next();
        
        int dec = 0;
        for (int i = 0; i < binary.length(); i++) {
            dec = dec * 2 + (binary.charAt(i) - '0');
        }

        System.out.println(dec);
    }
}