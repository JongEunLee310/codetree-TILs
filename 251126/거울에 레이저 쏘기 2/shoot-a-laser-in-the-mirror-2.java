import java.util.Scanner;

public class Main {
    public static boolean inRange(int x, int y, int n) {
        return (0 < x && x <= n && 0 < y && y <= n);
    }

    public static int[] initLoc(int startNum, int n) {
        int dirNum = startNum / n;
        int[] curLoc = new int[]{0, 0};
        int locIdx = startNum % n + 1;

        if (dirNum == 0) {
            curLoc[1] = locIdx;
        } else if (dirNum == 1) {
            curLoc[0] = locIdx;
            curLoc[1] = n + 1;
        } else if (dirNum == 2) {
            curLoc[0] = n + 1;
            curLoc[1] = n - locIdx + 1;
        } else {
            curLoc[0] = n - locIdx + 1;
        }

        return curLoc;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        char[][] grid = new char[n + 2][n + 2];
        for (int i = 1; i <= n; i++) {
            String s = sc.next();
            for (int j = 1; j <= n; j++) {
                grid[i][j] = s.charAt(j - 1);
            }
        }
        int startNum = sc.nextInt() - 1;
        
        int[] dx = new int[]{1, 0, -1, 0};
        int[] dy = new int[]{0, -1, 0, 1};
        int dirNum = startNum / n;
        int[] curLoc = initLoc(startNum, n);
        
        int cnt = 0;
        while(true) {
            int nx = curLoc[0] += dx[dirNum];
            int ny = curLoc[1] += dy[dirNum];

            if (!inRange(nx, ny, n)) {
                break;
            }

            if (grid[nx][ny] == '/') {
                if (dirNum == 0 || dirNum == 2) {
                    dirNum = (dirNum + 1) % 4;
                } else {
                    dirNum = (dirNum + 3) % 4;
                }
            } else {
                if (dirNum == 0 || dirNum == 2) {
                    dirNum = (dirNum + 3) % 4;
                } else {
                    dirNum = (dirNum + 1) % 4;
                }
            }

            curLoc[0] = nx;
            curLoc[1] = ny;
            cnt++;
        }
        System.out.println(cnt);
    }
}