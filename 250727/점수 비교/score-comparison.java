import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int AMath = sc.nextInt();
        int AEng = sc.nextInt();
        int BMath = sc.nextInt();
        int BEng = sc.nextInt();

        if (AMath > BMath && AEng > BEng) {
            System.out.println(1);
        } else {
            System.out.println(0);
        }
    }
}