import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int[][] matrix = new int[4][4];

        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                matrix[i][j] = sc.nextInt();
            }
        }

        int total = 0;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j <= i; j++) {
                total += matrix[i][j];
            }
        }

        System.out.println(total);
    }
}