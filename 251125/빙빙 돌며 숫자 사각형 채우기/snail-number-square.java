import java.util.Scanner;
public class Main {
    public static boolean inRange(int x, int y, int n, int m) {
        return (0 <= x && x < n && 0 <= y && y < m);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        
        int[] dx = new int[]{0, 1, 0, -1};
        int[] dy = new int[]{1, 0, -1, 0};
        int dirNum = 0;

        int[][] grid = new int[n][m];
        int[] curLoc = new int[]{0, 0};
        int curr = 2;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (i == 0 && j == 0) {
                    grid[i][j] = 1;
                    continue;
                }

                int nx = curLoc[0] + dx[dirNum];
                int ny = curLoc[1] + dy[dirNum];
                if (!inRange(nx, ny, n, m) || grid[nx][ny] != 0) {
                    dirNum = (dirNum + 1) % 4;
                }

                curLoc[0] = curLoc[0] + dx[dirNum];
                curLoc[1] = curLoc[1] + dy[dirNum];
                grid[curLoc[0]][curLoc[1]] = curr;
                curr++;
            }
        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                System.out.print(grid[i][j] + " ");
            }
            System.out.println();
        }
    }
}