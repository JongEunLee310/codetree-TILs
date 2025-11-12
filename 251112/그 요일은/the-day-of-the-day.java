import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m1 = sc.nextInt();
        int d1 = sc.nextInt();
        int m2 = sc.nextInt();
        int d2 = sc.nextInt();
        String A = sc.next();
        
        int days1 = getDays(m1, d1);
        int days2 = getDays(m2, d2);

        int diff = days2 - days1 + 1;
        int result = numOfA(diff, A);

        System.out.println(result);
    }

    public static int getDays(int month, int day) {
        int days = 0;
        int[] dayOfMonth = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        for (int i = 1; i < month; i++) {
            days += dayOfMonth[i];
        }

        days += day;
        
        return days;
    }

    public static int numOfA(int diff, String A) {
        int times = diff / 7;
        int remainder = diff % 7;
        
        switch(A) {
            case "Tue":
                if (remainder >= 1) times += 1;
                break;
            case "Wed":
                if (remainder >= 2) times += 1;
                break;
            case "Thu":
                if (remainder >= 3) times += 1;
                break;
            case "Fri":
                if (remainder >= 4) times += 1;
                break;
            case "Sat":
                if (remainder >= 5) times += 1;
                break;
            case "Sun":
                if (remainder >= 6) times += 1;
                break;
            default:
                times += 1;
        }
        
        return times;
    }
}