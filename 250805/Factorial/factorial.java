import java.util.Scanner;

public class Main {
    public static int fac(int n) {
        if (n == 0 || n == 1) {
            return 1;
        }

        return n * fac(n - 1);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int result = fac(n);
        System.out.println(result);
    }
}