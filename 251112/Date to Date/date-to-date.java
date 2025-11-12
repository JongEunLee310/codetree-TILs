import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m1 = sc.nextInt();
        int d1 = sc.nextInt();
        int m2 = sc.nextInt();
        int d2 = sc.nextInt();

        int days1 = getDays(m1, d1);
        int days2 = getDays(m2, d2);

        System.out.println(days2 - days1 + 1);
    }

    public static int getDays(int m, int d) {
        int days = 0;
        
        for (int i = 1; i < m; i++) {
            if (isThirtyDays(i)) {
                days += 30;
            } else if (i == 2) {
                days += 28;
            } else {
                days += 31;
            }       
        }

        days += d;

        return days;
    }

    public static boolean isThirtyDays(int month) {
        int[] thirtyDays = {4, 6, 9, 11};
        
        for (int m : thirtyDays) {
            if (m == month) return true;
        }

        return false;
    }
}