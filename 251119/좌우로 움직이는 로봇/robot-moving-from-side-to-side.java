import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        int maxTime = 1000000;

        int[] A = new int[maxTime];
        int at = 0;
        for (int i = 0; i < n; i++) {
            int t = sc.nextInt();
            char d = sc.next().charAt(0);
            
            for (int j = 1; j <= t; j++) {
                if (d == 'R') {
                    A[at + j] = A[at + j - 1] + 1;
                } else {
                    A[at + j] = A[at + j - 1] - 1;
                }
            }
            at += t;
        }
        
        int[] B = new int[maxTime];
        int bt = 0;
        for (int i = 0; i < m; i++) {
            int t = sc.nextInt();
            char d = sc.next().charAt(0);
            
            for (int j = 1; j <= t; j++) {
                if (d == 'R') {
                    B[bt + j] = B[bt + j - 1] + 1;
                } else {
                    B[bt + j] = B[bt + j - 1] - 1;
                }
            }
            bt += t;
        }
        
        int answer = 0;
        int aCurr = 1;
        int bCurr = 1;
        int t = 0;
        while(t < Math.max(at, bt)) {
            if (A[aCurr - 1] != B[bCurr - 1] && A[aCurr] == B[bCurr]) {
                answer++;
            }

            if (aCurr + 1 <= at) {
                aCurr++;
            }

            if (bCurr + 1 <= bt) {
                bCurr++;
            }

            t++;
        }
        System.out.println(answer);
    }
}