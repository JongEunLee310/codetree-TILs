import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();

        while (true) {
            System.out.print(A + " ");
            
            if (A % 2 != 0) {
                A *= 2;
            } else {
                A += 3;
            }

            if (A > B) {
                break;
            }
        }
    }
}