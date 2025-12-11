import java.util.Scanner;
public class Main {
    public static boolean inRange(int x, int y, int n, int m) {
        return (0 <= x && x < n && 0 <= y && y < m);
    }

    public static int cntLee(String[] arr, int x, int y, int n, int m) {
        int[] dx = new int[]{0, -1, -1, -1, 0, 1, 1, 1};
        int[] dy = new int[]{1, 1, 0, -1, -1, -1, 0, 1};

        int result = 0;
        for (int d = 0; d < 8; d++) {
            int cnt = 0;
            for (int i = 0; i < 3; i++) {
                int nx = x + dx[d] * i;
                int ny = y + dy[d] * i;

                if (inRange(nx, ny, n, m)) {
                    if (i == 0 && arr[nx].charAt(ny) == 'L' || i > 0 && arr[nx].charAt(ny) == 'E') {
                        cnt++;
                    }
                }
            }
            if (cnt == 3) {
                result++;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        String[] arr = new String[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.next();
        }

        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                int cnt = cntLee(arr, i, j, n, m);
                answer += cnt;
            }
        }

        System.out.println(answer);
    }
}