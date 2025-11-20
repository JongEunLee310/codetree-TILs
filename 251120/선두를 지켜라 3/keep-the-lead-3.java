import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] a = new int[n][2];
        int[][] b = new int[m][2];
        for (int i = 0; i < n; i++) {
            a[i][0] = sc.nextInt();
            a[i][1] = sc.nextInt();
        }
        for (int i = 0; i < m; i++) {
            b[i][0] = sc.nextInt();
            b[i][1] = sc.nextInt();
        }
        
        int maxTime = 1000001;
        int[] aTimeTable = new int[maxTime];
        int at = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < a[i][1]; j++) {
                aTimeTable[at + j] += a[i][0];
            }
            at += a[i][1];
        }

        int[] bTimeTable = new int[maxTime];
        int bt = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < b[i][1]; j++) {
                bTimeTable[bt + j] += b[i][0];
            }
            bt += b[i][1];
        }

        int leader = 0;
        int answer = 0;
        for (int i = 1; i < at; i++) {
            if (aTimeTable[i] > bTimeTable[i] && leader != 1) {
                leader = 1;
                answer++;
            } else if (aTimeTable[i] < bTimeTable[i] && leader != 2) {
                leader = 2;
                answer++;
            } else if (aTimeTable[i] == bTimeTable[i] && leader != 3) {
                leader = 3;
                answer++;
            }
        }

        System.out.println(answer);
    }
}