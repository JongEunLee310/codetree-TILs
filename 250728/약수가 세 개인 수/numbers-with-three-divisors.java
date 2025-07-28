import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int start = sc.nextInt();
        int end = sc.nextInt();
        int cnt = 0;
        int divisorCnt = 0;
        for (int i = start; i <= end; i++) {
            divisorCnt = 0;
            for (int j = 1; j <= i; j++) {
                if (i % j == 0) {
                    divisorCnt++;
                }

                if (divisorCnt > 3) {
                    break;
                }
            }

            if (divisorCnt == 3) {
                cnt++;
            }
        }
        System.out.print(cnt);
    }
}