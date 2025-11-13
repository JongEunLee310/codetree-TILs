import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] line = new int[2001];
        int curr = 1000;
        for (int i = 0; i < N; i++) {
            int x = sc.nextInt();
            char dir = sc.next().charAt(0);
            
            for (int j = 0; j < x; j++) {
                if (dir == 'R') {
                    line[curr]++;
                    curr++;
                } else {
                    curr--;
                    line[curr]++;
                }
            }
        }

        int result = 0;
        for (int i = 0; i < 2001; i++) {
            if (line[i] >= 2) result++;
        }
        System.out.println(result);
    }
}