import java.util.Scanner;
public class Main {
    public static int seq(int n) {
        if (n <= 2) return n;

        return seq(n / 3) + seq(n - 1); 
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int result = seq(n);
        System.out.println(result);
    }
}