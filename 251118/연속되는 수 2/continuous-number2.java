import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        
        int answer = 0;
        int curr = 1;
        for (int i = 1; i < n; i++) {
            if (arr[i - 1] == arr[i]) {
                curr++;
            } else {
                answer = Math.max(answer, curr);
                curr = 1;
            }
        }

        System.out.println(answer);
    }
}