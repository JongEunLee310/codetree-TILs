import java.util.Scanner;

public class Main {
    public static boolean inRange(int x, int y, int n) {
        return (0 <= x && x < n && 0 <= y && y < n);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        int[][] grid = new int[n][n];
        grid[n / 2][n / 2] = 1;

        int[] dx = new int[]{0, 1, 0, -1};
        int[] dy = new int[]{1, 0, -1, 0};
        int dirNum = 0;

        int[] curLoc = new int[]{n / 2, n / 2};
        for (int i = 2; i <= n * n; i++) {
            // 옮길 예상 위치
            int nx = curLoc[0] + dx[dirNum];
            int ny = curLoc[1] + dy[dirNum];

            // 현재 좌표에서 진행 방향의 반대 방향 좌표
            int bx = curLoc[0] + dx[(dirNum + 2) % 4];
            int by = curLoc[1] + dy[(dirNum + 2) % 4];

            // 현재 좌표에서 진행 방향의 왼쪽 방향 좌표
            int lx = curLoc[0] + dx[(dirNum + 3) % 4];
            int ly = curLoc[1] + dy[(dirNum + 3) % 4];

            if (!inRange(nx, ny, n) || grid[bx][by] != 0 && grid[lx][ly] == 0) {
                dirNum = (dirNum + 3) % 4;
            }

            curLoc[0] += dx[dirNum];
            curLoc[1] += dy[dirNum];
            grid[curLoc[0]][curLoc[1]] = i;
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.print(grid[i][j] + " ");
            }
            System.out.println();
        }
    }
}