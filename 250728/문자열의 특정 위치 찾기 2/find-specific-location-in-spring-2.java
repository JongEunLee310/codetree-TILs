import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        char tgt = sc.next().charAt(0);

        String[] words = {"apple", "banana", "grape", "blueberry", "orange"};

        int cnt = 0;
        for (int i = 0; i < 5; i++) {
            if (words[i].charAt(2) == tgt || words[i].charAt(3) == tgt) {
                cnt++;
                System.out.println(words[i]);
            }
        }
        System.out.println(cnt);
    }
}