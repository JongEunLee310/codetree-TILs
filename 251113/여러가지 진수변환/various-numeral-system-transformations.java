import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int b = sc.nextInt();
        
        int[] digits = new int[100];
        int cnt = 0;

        while(true) {
            if (n < b) {
                digits[cnt++] = n;
                break;
            }

            digits[cnt++] = n % b;
            n /= b;
        }

        for (int i = cnt - 1; i > -1; i--) {
            System.out.print(digits[i]);
        }
    }
}