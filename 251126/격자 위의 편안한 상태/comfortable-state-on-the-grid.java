import java.util.Scanner;
public class Main {
    public static boolean inRange(int x, int y, int n) {
        return (0 < x && x <= n && 0 < y && y <= n);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        int[] dx = new int[]{0, 1, 0, -1};
        int[] dy = new int[]{1, 0, -1, 0};

        int[][] grid = new int[n + 1][n + 1];
        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            grid[x][y] = 1;

            // 칠해진 칸 주변 4방향으로 색칠된 칸 갯수 확인
            int cnt = 0;
            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];
                if (inRange(nx, ny, n) && grid[nx][ny] == 1){
                    cnt++;
                }
            }

            if (cnt == 3) {
                System.out.println(1);
            } else {
                System.out.println(0);
            }
        }
    }
}