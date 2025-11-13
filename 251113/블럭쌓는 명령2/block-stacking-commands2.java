import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] spaces = new int[N + 1];
        for (int i = 0; i < K; i++) {
            int A = sc.nextInt();
            int B = sc.nextInt();

            for (int j = A; j <= B; j++) {
                spaces[j] += 1;
            }
        }

        int result = Arrays.stream(spaces).max().getAsInt();
        System.out.println(result);
    }
}