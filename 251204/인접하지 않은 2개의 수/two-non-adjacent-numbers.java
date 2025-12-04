import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }
        
        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (j == i - 1 || j == i || j == i + 1) {
                    continue;
                }

                int curr = arr[i] + arr[j];
                answer = Math.max(answer, curr);
            }
        }

        System.out.println(answer);
    }
}