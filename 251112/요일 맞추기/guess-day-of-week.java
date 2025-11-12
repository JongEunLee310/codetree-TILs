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

        int diff = days2 - days1;
        String day = whichDay(diff);

        System.out.println(day);
    }

    public static int getDays(int month, int day) {
        int days = 0;

        for (int i = 1; i < month; i++) {
            if (isThirtyDays(i)) {
                days += 30;
            } else if (i == 2) {
                days += 28;
            } else {
                days += 31;
            }
        }

        days += day;

        return days;
    }

    public static boolean isThirtyDays(int month) {
        int[] thirtyDays = {4, 6, 9, 11};

        for (int m : thirtyDays) {
            if (m == month) return true;
        }
        return false;
    }

    public static String whichDay(int diff) {
        int day = diff > 0 ? diff % 7 : diff % 7 + 7;

        switch(day) {
            case 1:
                return "Tue";
            case 2:
                return "Wed";
            case 3:
                return "Thu";
            case 4:
                return "Fri";
            case 5:
                return "Sat";
            case 6:
                return "Sun";
            default:
                return "Mon";
        }
    }
}