import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        int[] a = new int[1000000];
        int at = 0;
        for (int i = 0; i < n; i++) {
            char dir = sc.next().charAt(0);
            int t = sc.nextInt();
            for (int j = 1; j <= t; j++) {
                if (dir == 'R') {
                    a[at + j] = a[at + j - 1] + 1;
                } else {
                    a[at + j] = a[at + j - 1] - 1;
                }
            }
            at += t;
        }

        int[] b = new int[1000000];
        int bt = 0;
        for (int i = 0; i < m; i++) {
            char dir = sc.next().charAt(0);
            int t = sc.nextInt();
            for (int j = 1; j <= t; j++) {
                if (dir == 'R') {
                    b[bt + j] = b[bt + j - 1] + 1;
                } else {
                    b[bt + j] = b[bt + j - 1] - 1;
                }
            }
            bt += t;
        }

        int answer = -1;
        for (int i = 1; i < Math.min(at, bt); i++) {
            if (a[i] == b[i]) {
                answer = i;
                break;
            }
        }
        System.out.println(answer);
    }
}