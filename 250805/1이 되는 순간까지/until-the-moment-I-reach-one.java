import java.util.Scanner;
public class Main {
    public static int calCnt(int n) {
        if (n == 1) {
            return 0;
        }

        if (n % 2 == 0) {
            return calCnt(n / 2) + 1;
        } else {
            return calCnt(n / 3) + 1;
        }
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int cnt = calCnt(n);
        System.out.println(cnt);
    }
}