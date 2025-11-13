import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        String N = sc.next();
        
        int num = getDec(N, A);

        int[] result = new int[100];
        int cnt = 0;

        while(true) {
            if (num < B) {
                result[cnt++] = num;
                break;
            }

            result[cnt++] = num % B;
            num /= B;
        }

        for (int i = cnt - 1; i > -1; i--) {
            System.out.print(result[i]);
        }
    }

    public static int getDec(String num, int A) {
        int result = 0;

        for (int i = 0; i < num.length(); i++) {
            result = result * A + (num.charAt(i) - '0');
        }

        return result;
    }
}