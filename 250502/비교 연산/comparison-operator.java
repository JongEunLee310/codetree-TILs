import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();

        if (A >= B) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }

        if (A > B) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
        
        if (A <= B) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }

        if (A < B) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }

        if (A == B) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }

        if (A != B) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}