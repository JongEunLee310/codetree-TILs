import java.util.Scanner;
public class Main {
    public static int getMax(int[] arr, int idx) {
        if (idx == 0) {
            return arr[idx];
        }

        int max = getMax(arr, idx - 1);

        if(arr[idx] > max) {
            return arr[idx];
        } else {
            return max;
        }

    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        int result = getMax(arr, n - 1);
        System.out.println(result);
    }
}