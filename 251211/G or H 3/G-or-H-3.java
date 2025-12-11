import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        int[] line = new int[10001];
        for (int i = 0; i < n; i++) {
            int pos = sc.nextInt();
            char c = sc.next().charAt(0);

            if (c == 'G') {
                line[pos] = 1;
            } else if (c == 'H') {
                line[pos] = 2;
            }
        }
        
        int answer = 0;
        for (int i = 1; i < 10001 - k; i++) {
            int curr = 0;
            for (int j = i; j <= i + k; j++) {
                curr += line[j];
            }
            answer = Math.max(answer, curr);
        }

        System.out.println(answer);
    }
}