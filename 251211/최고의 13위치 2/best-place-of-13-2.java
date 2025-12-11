import java.util.Scanner;
public class Main {
    public static boolean inRange(int x, int y, int n, int m) {
        return (x == n && m - 2 <= y && y <= m + 2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] arr = new int[n][n];
        for(int i = 0; i < n; i++)
            for(int j = 0; j < n; j++)
                arr[i][j] = sc.nextInt();
        
        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n - 2; j++) {
                int cntF = 0;
                for (int c = j; c < j + 3; c++) {
                    cntF += arr[i][c];
                }

                for (int k = i; k < n; k++) {
                    for (int l = 0; l < n - 2; l++) {
                        if (inRange(k, l, i, j)) {
                            continue;
                        }

                        int cntS = 0;
                        for (int c = l; c < l + 3; c++) {
                            cntS += arr[k][c];
                        }
                        answer = Math.max(answer, cntF + cntS);
                    }
                }
            }
        }

        System.out.println(answer);
    }
}