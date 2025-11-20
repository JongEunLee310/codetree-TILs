import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] dx = new int[]{1, 0, -1, 0};
        int[] dy = new int[]{0, -1, 0, 1};

        int[] curr = new int[]{0, 0};
        for (int i = 0; i < n; i++) {
            char direction = sc.next().charAt(0);
            int distance = sc.nextInt();
            
            int dir = 0;
            if (direction == 'E') {
                dir = 0;
            } else if (direction == 'S') {
                dir = 1;
            } else if (direction == 'W') {
                dir = 2;
            } else if (direction == 'N') {
                dir = 3;
            }

            curr[0] += dx[dir] * distance;
            curr[1] += dy[dir] * distance;
        }

        System.out.println(curr[0] + " " + curr[1]);
    }
}