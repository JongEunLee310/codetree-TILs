import java.util.Scanner;

public class Main {
    public static boolean inRange(int x, int y, int n) {
        return (0 <= x && x < n && 0 <= y && y < n);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int t = sc.nextInt();
        String commands = sc.next();
        int[][] board = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                board[i][j] = sc.nextInt();
            }
        }
        
        int[] dx = new int[]{0, 1, 0, -1};
        int[] dy = new int[]{1, 0, -1, 0};
        int dirNum = 3;
        
        int[] curLoc = new int[]{n / 2, n / 2};
        int answer = board[curLoc[0]][curLoc[1]];
        for (int i = 0; i < commands.length(); i++) {
            char c = commands.charAt(i);

            if (c == 'R') {
                dirNum = (dirNum + 1) % 4;
            } else if (c == 'L') {
                dirNum = (dirNum + 3) % 4;
            } else if (c == 'F') {
                int nx = curLoc[0] + dx[dirNum];
                int ny = curLoc[1] + dy[dirNum];
                if (!inRange(nx, ny, n)) {
                    continue;
                }

                curLoc[0] += dx[dirNum];
                curLoc[1] += dy[dirNum];
                answer += board[curLoc[0]][curLoc[1]];
            }
        }

        System.out.println(answer);
    }
}