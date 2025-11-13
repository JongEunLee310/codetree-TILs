import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String binary = sc.next();
        
        int n = getDec(binary);
        int[] result = new int[100];
        int cnt = 0;

        while(true) {
            if (n < 2) {
                result[cnt++] = n;
                break;
            }

            result[cnt++] = n % 2;
            n /= 2;
        }

        for (int i = cnt - 1; i > -1; i--) {
            System.out.print(result[i]);
        }
    }

    public static int getDec(String binary) {
        int dec = 0;

        for (int i = 0; i < binary.length(); i++) {
            dec = dec * 2 + (binary.charAt(i) - '0');
        }

        return dec * 17;
    }
}