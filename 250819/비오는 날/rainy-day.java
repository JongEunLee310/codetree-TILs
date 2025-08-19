import java.util.Scanner;

class Weather {
    String date;
    String day;
    String weather;

    public Weather() {
        this.date = "";
        this.day = "";
        this.weather = "";
    }

    public Weather(String date, String day, String weather) {
        this.date = date;
        this.day = day;
        this.weather = weather;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        Weather ans = new Weather("9999-99-99", "", "");
        for (int i = 0; i < n; i++) {
            String date = sc.next();
            String day = sc.next();
            String weather = sc.next();
            
            Weather w = new Weather(date, day, weather);
            if (w.weather.equals("Rain") && w.date.compareTo(ans.date) < 0) {
                ans = w;
            }
        }

        System.out.println(ans.date + " " + ans.day + " " + ans.weather);
    }
}