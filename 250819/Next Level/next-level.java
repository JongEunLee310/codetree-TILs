import java.util.Scanner;

class User {
    String id;
    int level;

    public User() {
        this.id = "codetree";
        this.level = 10;
    }

    public User(String id, int level) {
        this.id = id;
        this.level = level;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String id = sc.next();
        int level = sc.nextInt();
        
        User usr1 = new User();
        User usr2 = new User();

        usr2.id = id;
        usr2.level = level;

        System.out.println("user " + usr1.id + " lv " + usr1.level);
        System.out.println("user " + usr2.id + " lv " + usr2.level);
    }
}