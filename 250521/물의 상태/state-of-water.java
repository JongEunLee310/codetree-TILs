import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // Please write your code here.
        Scanner sc = new Scanner(System.in);
        int temperature = sc.nextInt();

        if (temperature < 0) {
            System.out.println("ice");
        } else if (temperature >= 100) {
            System.out.println("vapor");
        } else {
            System.out.println("water");
        }
    }
}