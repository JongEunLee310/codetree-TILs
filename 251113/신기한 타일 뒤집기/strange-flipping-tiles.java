import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] tiles = new int[200001];
        int curr = 100000;
        for (int i = 0; i < n; i++) {
            int x = sc.nextInt();
            char d = sc.next().charAt(0);

            for (int j = 0; j < x; j++) {
                if (d == 'L') {
                    if (j > 0) curr--;
                    tiles[j] = 1;
                } else {
                    if (j > 0) curr++;
                    tiles[j] = 2;
                }
            }
        }

        int w = 0;
        int b = 0;
        for (int i = 0; i < 200001; i++) {
            if (tiles[i] == 1) {
                w++;
            } else if (tiles[i] == 2) {
                b++;
            }
        }
        System.out.println(w + " " + b);
    }
}