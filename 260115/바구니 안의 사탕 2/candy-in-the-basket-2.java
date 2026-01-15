import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] candies = new int[n];
        int[] positions = new int[n];
        for (int i = 0; i < n; i++) {
            candies[i] = sc.nextInt();
            positions[i] = sc.nextInt();
        }
        
        int maxLength = 101;
        int[] line = new int[maxLength];
        for (int i = 0; i < n; i++) {
            line[positions[i]] += candies[i];
        }

        // k가 maxLength보다 클때?
        int range = Math.min(k, maxLength / 2);
        int answer = 0;
        for (int i = range; i < maxLength - range; i++) {
            int curr = 0;
            for (int j = i - range; j <= i + range; j++) {
                curr += line[j];
            }
            answer = Math.max(answer, curr);
        }

        System.out.println(answer);
    }
}