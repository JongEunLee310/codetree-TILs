import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int p = sc.nextInt();
        char[] c = new char[M];
        int[] u = new int[M];
        for (int i = 0; i < M; i++) {
            c[i] = sc.next().charAt(0);
            u[i] = sc.nextInt();
        }
        
        if (u[p - 1] == 0) {
            System.out.println("");
        } else {
            int aIdx = (int) 'A';
            boolean[] read = new boolean[N];
            for (int i = p - 1; i < M; i++) {
                read[(int) c[i] - aIdx] = true;
            }

            for (int i = p - 1; i >= 0; i--) {
                if (u[p - 1] == u[i]) {
                    read[(int) c[i] - aIdx] = true;
                }
            }

            for (int i = 0; i < N; i++) {
                if (!read[i]) {
                    System.out.print((char) (aIdx + i) + " ");
                }
            }
        }
    }
}