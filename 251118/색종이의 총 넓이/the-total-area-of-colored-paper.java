import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] x = new int[n];
        int[] y = new int[n];
        for (int i = 0; i < n; i++) {
            x[i] = sc.nextInt();
            y[i] = sc.nextInt();
        }
        
        int offset = 100;
        int[][] grid = new int[201][201];
        for (int i = 0; i < n; i++) {
            for (int gy = y[i]; gy > y[i] - 8; gy--) {
                for (int gx = x[i]; gx < x[i] + 8; gx++) {
                    grid[gy + offset][gx + offset] = 1;
                }
            }
        }

        int answer = 0;
        for (int i = 0; i < 201; i++) {
            for (int j = 0; j < 201; j++) {
                if (grid[i][j] == 1) answer++;
            } 
        }

        System.out.println(answer);
    }
}