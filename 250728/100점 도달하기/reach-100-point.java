import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        while (N <= 100) {
            if (N >= 90) {
                System.out.print("A ");
            } else if (N >= 80) {
                System.out.print("B ");
            } else if (N >= 70) {
                System.out.print("C ");
            } else if (N >= 60) {
                System.out.print("D ");
            } else {
                System.out.print("F ");
            }

            N += 1;
        }
    }
}