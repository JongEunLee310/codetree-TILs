import java.util.Scanner;

public class Main {
    public static final int INT_MAX = Integer.MAX_VALUE;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int s = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += arr[i];
        }

        int answer = INT_MAX;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                answer = Math.min(answer, Math.abs(s - (sum - arr[i] - arr[j])));
            }
        }
        
        System.out.println(answer);
    }
}