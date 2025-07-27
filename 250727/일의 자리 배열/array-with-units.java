import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] nums = new int[10];

        for (int i = 0; i < 10; i++) {
            if (i < 2) {
                nums[i] = sc.nextInt();
                continue;
            }

            nums[i] = (nums[i - 1] + nums[i - 2]) % 10;
        }

        for (int i = 0; i < 10; i++) {
            System.out.print(nums[i] + " ");
        }
    }
}