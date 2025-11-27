import java.util.Scanner;
public class Main {
    public static boolean inRange(int x, int y, int n, int m) {
        return (0 <= x && x < n && 0 <= y && y < m);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        char[][] grid = new char[n][m];
        int alpha = 65;
        grid[0][0] = (char) alpha;

        int[] dx = new int[]{0, 1, 0, -1};
        int[] dy = new int[]{1, 0, -1, 0};
        int dirNum = 0;

        int[] curLoc = new int[]{0, 0};
        for (int i = 1; i < n * m; i++) {
            int nx = curLoc[0] + dx[dirNum];
            int ny = curLoc[1] + dy[dirNum];

            if (!inRange(nx, ny, n, m) || grid[nx][ny] != 0) {
                dirNum = (dirNum + 1) % 4;
            }

            curLoc[0] += dx[dirNum];
            curLoc[1] += dy[dirNum];

            grid[curLoc[0]][curLoc[1]] = (char)(alpha + (i % 26));
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(grid[i][j] + " ");
            }
            System.out.println();
        }
    }
}