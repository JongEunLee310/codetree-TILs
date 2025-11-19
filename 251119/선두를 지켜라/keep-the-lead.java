import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] A = new int[n][2];
        for (int i = 0; i < n; i++) {
            A[i][0] = sc.nextInt();
            A[i][1] = sc.nextInt();
        }
        int[][] B = new int[m][2];
        for (int i = 0; i < m; i++) {
            B[i][0] = sc.nextInt();
            B[i][1] = sc.nextInt();
        }

        int maxTime = 1000000;

        int at = 0;
        int[] aTimeTable = new int[maxTime];
        for (int i = 0; i < n; i++) {   
            for(int t = 1; t <= A[i][1]; t++) {
                aTimeTable[at + t] = aTimeTable[at + t - 1] + A[i][0];
            }
            at += A[i][1];
        }

        int bt = 0;
        int[] bTimeTable = new int[maxTime];
        for (int i = 0; i < m; i++) {   
            for(int t = 1; t <= B[i][1]; t++) {
                bTimeTable[bt + t] = bTimeTable[bt + t - 1] + B[i][0];
            }
            bt += B[i][1];
        }

        int leader = 0;
        int answer = 0;
        for (int i = 0; i < at; i++) {
            if (aTimeTable[i] > bTimeTable[i] && leader != 1) {
                if (leader != 0) {
                    answer++;
                }
                leader = 1;
            } else if (aTimeTable[i] < bTimeTable[i] && leader != 2) {
                if (leader != 0) {
                    answer++;
                }
                leader = 2;
            }
        }

        System.out.println(answer);
    }
}