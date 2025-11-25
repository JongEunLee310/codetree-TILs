import java.util.Scanner;

public class Main {
    public static int getDir(String D) {
        int dirNum = 0;

        if (D.equals('U')) {
            dirNum = 1;
        } else if (D.equals('D')) {
            dirNum = 2;
        } else if (D.equals('R')) {
            dirNum = 0;
        } else if (D.equals('L')) {
            dirNum = 3;
        }

        return dirNum;
    }

    public static boolean inRange(int x, int y, int n) {
        return (0 < x && x <= n && 0 < y && y <= n);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int T = sc.nextInt();
        int R = sc.nextInt();
        int C = sc.nextInt();
        String D = sc.next();
        
        int[] dx = new int[]{0, 1, -1, 0};
        int[] dy = new int[]{1, 0, 0, -1};
        int dirNum = getDir(D);

        for (int t = 0; t < T; t++) {
            int nx = R + dx[dirNum];
            int ny = C + dy[dirNum];

            if (inRange(nx, ny, N)) {
                R = nx;
                C = ny;
            } else {
                dirNum = 3 - dirNum;
            }
        }

        System.out.println(R + " " + C);
    }
}