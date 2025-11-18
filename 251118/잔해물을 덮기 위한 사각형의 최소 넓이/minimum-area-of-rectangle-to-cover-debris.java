import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int rect1_x1 = sc.nextInt();
        int rect1_y1 = sc.nextInt();
        int rect1_x2 = sc.nextInt();
        int rect1_y2 = sc.nextInt();
        int rect2_x1 = sc.nextInt();
        int rect2_y1 = sc.nextInt();
        int rect2_x2 = sc.nextInt();
        int rect2_y2 = sc.nextInt();

        int offset = 1000;
        int[][] grid = new int[2001][2001];

        for (int y = rect1_y1; y < rect1_y2; y++) {
            for (int x = rect1_x1; x < rect1_x2; x++) {
                grid[y + offset][x + offset] = 1;
            }
        }

        for (int y = rect2_y1; y < rect2_y2; y++) {
            for (int x = rect2_x1; x < rect2_x2; x++) {
                grid[y + offset][x + offset] = 0;
            }
        }

        int x1 = 0;
        int x2 = 0;
        int y1 = 0;
        int y2 = 0;
        for (int i = 0; i < 2001; i++) {
            for (int j = 0; j < 2001; j++) {
                if (grid[i][j] == 1) {
                    if (x1 == x2 && x1 == 0) {
                        x1 = j;
                        x2 = j;
                    } else {
                        x2 = Math.max(x2, j);
                    }

                    if (y1 == y2 && y1 == 0) {
                        y1 = i;
                        y2 = i;
                    } else {
                        y2 = Math.max(y2, i);
                    }
                }
            }
        }

        //System.out.println("x1 : " + x1 + " x2 : " + x2 + " y1 : " + y1 + " y2 : " + y2);

        int answer = (x1 == x2 && y1 == y2) ? 0 : (x2 - x1 + 1) * (y2 - y1 + 1);
        System.out.println(answer);
    }
}