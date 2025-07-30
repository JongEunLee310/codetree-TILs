import java.util.Scanner;
public class Main {
    public static void ascNum(int n) {
        if (n == 0) {
            return;
        }

        ascNum(n - 1);
        System.out.print(n + " ");
    }

    public static void descNum(int n) {
        if (n == 0) {
            return;
        }

        System.out.print(n + " ");
        descNum(n - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        ascNum(n);
        System.out.println();
        descNum(n);
    }
}