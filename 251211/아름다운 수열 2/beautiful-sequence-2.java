import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] A = new int[N];
        for (int i = 0; i < N; i++)
            A[i] = sc.nextInt();
        int[] B = new int[M];
        for (int i = 0; i < M; i++)
            B[i] = sc.nextInt();
        
        Arrays.sort(B);
        int answer = 0;
        for (int i = 0; i < N - M + 1; i++) {
            int[] partialA = new int[M];
            for (int j = i; j < i + M; j++) {
                partialA[j - i] = A[j];
            }

            Arrays.sort(partialA);

            boolean isSame = true;
            for (int j = 0; j < M; j++) {
                if (B[j] != partialA[j]) {
                    isSame = false;
                    break;
                }
            }

            if (isSame) {
                answer++;
            }
        }

        System.out.println(answer);
    }
}