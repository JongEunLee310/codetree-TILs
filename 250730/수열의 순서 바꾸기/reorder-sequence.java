import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
       
        int linearCnt = 1;
        for (int i = n - 2; i >= 0; i--) {
            if (arr[i + 1] > arr[i]) {
                linearCnt++;
            } else {
                break;
            }
        }

        System.out.println(n - linearCnt);
    }
}