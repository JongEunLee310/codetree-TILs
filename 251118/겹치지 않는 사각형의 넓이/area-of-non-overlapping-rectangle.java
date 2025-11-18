import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int ax1 = sc.nextInt();
        int ay1 = sc.nextInt();
        int ax2 = sc.nextInt();
        int ay2 = sc.nextInt();
        int bx1 = sc.nextInt();
        int by1 = sc.nextInt();
        int bx2 = sc.nextInt();
        int by2 = sc.nextInt();
        int mx1 = sc.nextInt();
        int my1 = sc.nextInt();
        int mx2 = sc.nextInt();
        int my2 = sc.nextInt();
        
        int offset = 1000;
        int[][] grid = new int[2001][2001];
        for (int i = ay1; i < ay2; i++) {
            for (int j = ax1; j < ax2; j++) {
                grid[i + offset][j + offset] = 1;
            }
        }

        for (int i = by1; i < by2; i++) {
            for (int j = bx1; j < bx2; j++) {
                grid[i + offset][j + offset] = 2;
            }
        }

        for (int i = my1; i < my2; i++) {
            for (int j = mx1; j < mx2; j++) {
                grid[i + offset][j + offset] = 0;
            }
        }

        int answer = 0;
        for (int i = 0; i < 2001; i++) {
            for (int j = 0; j < 2001; j++) {
                if (grid[i][j] > 0) answer++;
            }
        }

        System.out.println(answer);
    }
}