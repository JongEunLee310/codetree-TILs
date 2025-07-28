import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int A = 0;
        int B = 0;
        int total = 0;
        for (int i = 0; i < N; i++){
            A = sc.nextInt();
            B = sc.nextInt();
            total = 0;

            for (int j = A; j <= B; j++) {
                if (j % 2 == 0) {
                    total += j;
                }
            }

            System.out.println(total);
        }
    }
}