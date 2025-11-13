import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] x1 = new int[n];
        int[] x2 = new int[n];
        for (int i = 0; i < n; i++) {
            x1[i] = sc.nextInt();
            x2[i] = sc.nextInt();
        }
        
        int[] lines = new int[201];
        for (int i = 0; i < n; i++) {
            for (int j = x1[i]; j < x2[i]; j++) {
                lines[j + 100] += 1;
            }
        }

        int result = Arrays.stream(lines).max().getAsInt();
        System.out.println(result);
    }
}