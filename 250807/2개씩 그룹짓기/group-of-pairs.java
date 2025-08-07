import java.util.Scanner;
import java.util.Arrays;
import java.lang.Math;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] nums = new int[2 * n];
        for (int i = 0; i < 2 * n; i++) {
            nums[i] = sc.nextInt();
        }
        
        Arrays.sort(nums);
        int minMax = 0;
        for (int i = 0; i < n; i++) {
            int cur = nums[i] + nums[n * 2 - 1 - i];
            minMax = Math.max(minMax, cur);
        }

        System.out.println(minMax);
    }
}