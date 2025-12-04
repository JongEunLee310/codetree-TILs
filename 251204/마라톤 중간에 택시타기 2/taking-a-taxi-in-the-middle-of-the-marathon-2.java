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
        
        int maxDist = 0;
        for (int i = 1; i < n; i++) {
            maxDist += Math.abs(x[i - 1] - x[i]) + Math.abs(y[i - 1] - y[i]);
        }

        int answer = maxDist;
        for (int i = 1; i < n - 1; i++) {
            int lazy = maxDist - (Math.abs(x[i - 1] - x[i]) + Math.abs(y[i - 1] - y[i])) - (Math.abs(x[i] - x[i + 1]) + Math.abs(y[i] - y[i + 1])) + Math.abs(x[i - 1] - x[i + 1]) + Math.abs(y[i - 1] - y[i + 1]);
            answer = Math.min(answer, lazy);
        }

        System.out.println(answer);
    }
}