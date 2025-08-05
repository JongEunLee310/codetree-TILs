import java.util.Scanner;
public class Main {
    public static int seq(int n) {
        if (n == 1) {
            return 0;
        }

        return n % 2 == 0 ? seq(n / 2) + 1 : seq(n * 3 + 1) + 1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int result = seq(n);
        System.out.println(result);
    }
}