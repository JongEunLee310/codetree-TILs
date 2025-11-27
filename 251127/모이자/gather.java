import java.util.Scanner;
public class Main {
    public static final int INT_MAX = Integer.MAX_VALUE;

    public static void main(String[] args) {

        
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] a = new int[n];
        for (int i = 0; i < n; i++) {
            a[i] = sc.nextInt();
        }
        
        int answer = INT_MAX;
        for (int i = 0; i < n; i++) {
            int dist = 0;
            for (int j = 0; j < n; j++) {
                dist += Math.abs(i - j) * a[j];
            }
            answer = Math.min(answer, dist);
        }

        System.out.println(answer);
    }
}