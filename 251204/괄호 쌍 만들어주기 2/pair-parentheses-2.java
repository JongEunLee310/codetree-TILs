import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();

        int n = input.length();
        int answer = 0;
        for (int i = 0; i < n - 3; i++) {
            if (input.charAt(i) == '(' && input.charAt(i + 1) == '(') {
                for (int j = i + 2; j < n - 1; j++) {
                    if (input.charAt(j) == ')' && input.charAt(j + 1) == ')') {
                        answer++;
                    }
                }
            }
        }
        System.out.println(answer);
    }
}