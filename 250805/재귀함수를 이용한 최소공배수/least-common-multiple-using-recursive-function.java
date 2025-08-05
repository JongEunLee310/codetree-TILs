import java.util.Scanner;
import java.lang.Math;

public class Main {
    public static int getLCM(int[] arr, int idx) {
        if (idx == 0) {
            return arr[idx];
        }

        int result = getLCM(arr, idx - 1);

        int GCD = 1;
        for (int i = 1; i <= Math.min(result, arr[idx]); i++) {
            if (result % i == 0 && arr[idx] % i == 0) {
                GCD = i;
            }
        }

        return result * arr[idx] / GCD;
    } 

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        int result = getLCM(arr, n - 1);
        System.out.println(result);
    }
}