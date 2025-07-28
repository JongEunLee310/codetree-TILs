import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] nums = new int[N];

        int numIndex = 0;
        for (int i = 0; i < N; i++) {
            int n = sc.nextInt();

            if (n % 2 == 0) {
                nums[numIndex] = n;
                numIndex++;
            }
        }

        for (int i = numIndex - 1; i >= 0; i--) {
            System.out.print(nums[i] + " ");
        }
    }
}