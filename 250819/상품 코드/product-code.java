import java.util.Scanner;

class Merchan {
    String name;
    int code;

    public Merchan() {
        this.name = "codetree";
        this.code = 50;
    }

    public Merchan(String name, int code) {
        this.name = name;
        this.code = code;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String id2 = sc.next();
        int code2 = sc.nextInt();
        
        Merchan merchan1 = new Merchan();
        Merchan merchan2 = new Merchan(id2, code2);

        System.out.println("product " + merchan1.code + " is " + merchan1.name);
        System.out.println("product " + merchan2.code + " is " + merchan2.name);
    }
}