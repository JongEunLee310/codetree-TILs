import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int P = sc.nextInt();
        int T = sc.nextInt();
        int[][] shakes = new int[T][3];
        for (int i = 0; i < T; i++) {
            shakes[i][0] = sc.nextInt();
            shakes[i][1] = sc.nextInt();
            shakes[i][2] = sc.nextInt();
        }
        
        Arrays.sort(shakes, (a, b) -> Integer.compare(a[0], b[0]));

        int startT = shakes[0][0];
        int endT = shakes[T - 1][0] + 1;
        int[][][] dev = new int[N + 1][endT][2];

        // 초기 감염자 타임테이블 초기화
        for (int i = 0; i <= N; i++) {
            dev[P][i][0] = 1;
            dev[P][i][1] = K;
        }

        // 감염자 타임 테이블 로직
        for (int i = 0; i < T; i++) {
            int t = shakes[i][0];

            // 현재 타임 테이블 초기값 업데이트
            for (int j = 1; j <= N; j++) {
                dev[j][t] = dev[j][t - 1];
            }

            if (dev[shakes[i][1]][t - 1][0] == 1 && dev[shakes[i][1]][t - 1][1] > 0) {
                // 접촉자 감염
                if (dev[shakes[i][2]][t - 1][0] != 1) { // 비감염자 
                    dev[shakes[i][2]][t][0] = 1;
                    dev[shakes[i][2]][t][1] = K;
                } else {    // 감염자
                    dev[shakes[i][2]][t][1]--;
                }
                // 기존 감염자 타임 테이블 업데이트
                dev[shakes[i][1]][t][0] = 1;
                dev[shakes[i][1]][t][1] = dev[shakes[i][1]][t - 1][1] - 1;
            } else if (dev[shakes[i][2]][t - 1][0] == 1 && dev[shakes[i][2]][t - 1][1] > 0) {
                // 접촉자 감염
                if (dev[shakes[i][1]][t - 1][0] != 1) { // 비감염자 
                    dev[shakes[i][1]][t][0] = 1;
                    dev[shakes[i][1]][t][1] = K;
                } else {    // 감염자
                    dev[shakes[i][1]][t][1]--;
                }
                // 기존 감염자 타임 테이블 업데이트
                dev[shakes[i][2]][t][0] = 1;
                dev[shakes[i][2]][t][1] = dev[shakes[i][1]][t - 1][1] - 1;
            }
        }

        for (int i = 1; i < N + 1; i++) {
            System.out.print(dev[i][endT - 1][0]);
        }
    }
}