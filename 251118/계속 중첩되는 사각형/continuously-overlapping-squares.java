import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int offset = 100;
        int[][] grid = new int[201][201];
        for (int i = 0; i < n; i++) {
            int x1 = sc.nextInt();
            int y1 = sc.nextInt();
            int x2 = sc.nextInt();
            int y2 = sc.nextInt();

            for (int y = y1; y < y2; y++) {
                for (int x = x1; x < x2; x++) {
                    if (i % 2 == 0) {
                        grid[y + offset][x + offset] = 1;
                    } else {
                        grid[y + offset][x + offset] = 2;
                    }
                }
            }
        }

        int answer = 0;
        for (int i = 0; i < 201; i++) {
            for (int j = 0; j < 201; j++) {
                if (grid[i][j] == 2) answer++;
            }
        }        

        System.out.println(answer);
    }
}