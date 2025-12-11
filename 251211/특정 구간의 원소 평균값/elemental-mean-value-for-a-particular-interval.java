import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++)
            arr[i] = sc.nextInt();
        
        int answer = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                double sumVal = 0;
                for (int k = i; k <= j; k++) {
                    sumVal += arr[k];
                }

                double avgVal = sumVal / (j - i + 1);
                for (int k = i; k <= j; k++) {
                    if (arr[k] == avgVal) {
                        answer++;
                        break;
                    }
                }
            }
        }

        System.out.println(answer);
    }
}