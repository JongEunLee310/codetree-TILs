import java.util.Scanner;
public class Main {
    public static int getN(String a, int idx) {
        int N = 0;
        for (int i = 0; i < a.length(); i++) {
            if (i == idx) {
                if (a.charAt(i) == '1') {
                    N = N * 2;
                } else if (a.charAt(i) == '0') {
                    N = N * 2 + 1;
                }
            } else {
                N = N * 2 + (int)(a.charAt(i) - '0');
            }
        }

        return N;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
        int answer = 0;
        for (int i = 1; i < a.length(); i++) {
            int N = getN(a, i);
            answer = Math.max(answer, N);
        }
        
        System.out.println(answer);
    }
}