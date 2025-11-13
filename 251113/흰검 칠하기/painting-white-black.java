import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] w_tiles = new int[200001];
        int[] b_tiles = new int[200001];
        Integer[] tiles = new Integer[200001];
        int curr = 100000;
        for (int i = 0; i < N; i++) {
            int x = sc.nextInt();
            char d = sc.next().charAt(0);

            for (int j = 0; j < x; j++) {
                if (d == 'L') {
                    if (j > 0) curr--;
                    w_tiles[curr]++;
                    if (w_tiles[curr] >= 2 && b_tiles[curr] >= 2) {
                        tiles[curr] = 3;
                    } else {
                        tiles[curr] = 1;
                    }
                } else {
                    if (j > 0) curr++;
                    b_tiles[curr]++;
                    if (b_tiles[curr] >= 2 && w_tiles[curr] >= 2) {
                        tiles[curr] = 3;
                    } else {
                        tiles[curr] = 2;
                    }
                }
            }
        }

        int w = 0;
        int b = 0;
        int g = 0;
        for (int i = 0; i < 200001; i++) {
            if (tiles[i] == null) {
                continue;
            } else if (tiles[i] == 1) {
                w++;
            } else if (tiles[i] == 2) {
                b++;
            } else {
                g++;
            }
        }

        System.out.println(w + " " + b + " " + g);
    }
}