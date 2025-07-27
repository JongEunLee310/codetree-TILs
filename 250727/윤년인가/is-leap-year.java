import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int Y = sc.nextInt();
        Boolean isLeapYear = true;

        if (Y % 4 == 0) {
            if (Y % 100 == 0) {
                if (Y % 400 != 0) {
                    isLeapYear = false;
                }
            }
        } else {
            isLeapYear = false;
        }

        System.out.println(isLeapYear);
    }
}