import java.util.Scanner;
public class Main {
    public static boolean inRange(int x, int y, int n, int m) {
        return (0 <= x && x < n && 0 <= y && y < m);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        int[][] grid = new int[n][m];
        grid[0][0] = 1;

        int[] dx = {0, 1, 0, -1};
        int[] dy = {1, 0, -1, 0};
        int dirNum = 1;
        int[] curLoc = new int[]{0, 0};
        for (int i = 2; i <= n * m; i++) {
            int nx = curLoc[0] + dx[dirNum];
            int ny = curLoc[1] + dy[dirNum];

            if (!inRange(nx, ny, n, m) || grid[nx][ny] != 0) {
                dirNum = (dirNum + 3) % 4;
            }

            curLoc[0] += dx[dirNum];
            curLoc[1] += dy[dirNum];
            grid[curLoc[0]][curLoc[1]] = i;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(grid[i][j] + " ");
            }
            System.out.println();
        }
    }
}