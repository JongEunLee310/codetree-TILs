import java.util.Scanner;

class Code {
    String secretCode;
    char meetingPoint;
    int time;

    public Code(String secretCode, char meetingPoint, int time) {
        this.secretCode = secretCode;
        this.meetingPoint = meetingPoint;
        this.time = time;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String sCode = sc.next();
        char mPoint = sc.next().charAt(0);
        int time = sc.nextInt();
        

        Code cd = new Code(sCode, mPoint, time);

        System.out.println("secret code : " + cd.secretCode);
        System.out.println("meeting point : " + cd.meetingPoint);
        System.out.println("time : " + cd.time);
    }
}