import java.util.Scanner;

public class Main {

    public static int condSum(int n) {
        if (n == 1 || n == 2) {
            return n;
        }

        return n + condSum(n - 2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int result = condSum(n);
        System.out.println(result);
    }
}