import java.util.Scanner;
public class Main {
    public static int getNoCarrySum(int n1, int n2, int n3) {
        int[] N1 = splitNum(n1);
        int[] N2 = splitNum(n2);
        int[] N3 = splitNum(n3);

        boolean noCarry = true;
        for (int i = 0; i < N1.length; i++) {
            if (N1[i] + N2[i] + N3[i] > 10) {
                noCarry = false;
                break;
            }
        }

        if (noCarry) {
            return n1 + n2 + n3;
        }
        
        return -1;
    }

    public static int[] splitNum(int n) {
        int[] N = new int[5];
        
        int i = 0;
        while(true) {
            if (n < 10) {
                N[i] = n;
                break;
            }

            N[i] = n % 10;
            n /= 10;
            i++;
        }
        return N;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }
        
        int answer = -1;
        for (int i = 0; i < n - 2; i++) {
            for (int j = i + 1; j < n - 1; j++) {
                for (int k = j + 1; k < n; k++) {
                    answer = Math.max(answer, getNoCarrySum(arr[i], arr[j], arr[k]));
                }
            }
        }
        
        System.out.println(answer);
    }
}