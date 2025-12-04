import java.util.Scanner;
public class Main {
    public static final int INT_MAX = Integer.MAX_VALUE;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        
        int answer = INT_MAX;
        for (int i = 0; i < n; i++) {
            int dist = 0;
            for (int j = 0; j < n; j++) {
                if (j - i >= 0) {
                    dist += (j - i) * arr[j];
                } else {
                    dist += (n - 1 - j) * arr[j];
                }
            }
            answer = Math.min(answer, dist);
        }

        System.out.println(answer);
    }
}