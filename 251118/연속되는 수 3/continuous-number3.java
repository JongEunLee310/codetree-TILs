import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        
        int answer = 0;
        int cnt = 1;
        for (int i = 0; i < n; i++) {
            if (i >= 1 && (arr[i - 1] > 0 && arr[i] > 0 || arr[i - 1] < 0 && arr[i] < 0)) {
                cnt++;
            } else {
                cnt = 1;
            }

            answer = Math.max(answer, cnt);
        }

        System.out.println(answer);
    }
}