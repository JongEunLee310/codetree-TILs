import java.util.Scanner;
public class Main {
    public static int sum(int n) {
        if (n < 10) {
            return n;
        }
        
        return sum(n / 10) + (n % 10);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        int result = sum(a * b * c);
        System.out.println(result);
    }
}