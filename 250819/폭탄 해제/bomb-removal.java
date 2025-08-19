import java.util.Scanner;

class Disarm {
    String code;
    char cable;
    int timer;

    public Disarm(String code, char cable, int timer) {
        this.code = code;
        this.cable = cable;
        this.timer = timer;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String uCode = sc.next();
        char lColor = sc.next().charAt(0);
        int time = sc.nextInt();
        
        Disarm disarm = new Disarm(uCode, lColor, time);

        System.out.println("code : " + disarm.code);
        System.out.println("color : " + disarm.cable);
        System.out.println("second : " + disarm.timer);
    }
}