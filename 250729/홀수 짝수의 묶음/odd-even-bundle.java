import java.util.Scanner;
import java.lang.Math;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int[] numbers = new int[N];
        for (int i = 0; i < N; i++) {
            numbers[i] = sc.nextInt();
        }
        
        // 짝수 홀수 구분
        int evenIdx = 0;
        int oddIdx = 0;
        for (int i = 0; i < N; i++) {
            if (numbers[i] % 2 == 0) {
                evenIdx++;
            } else {
                oddIdx++;
            }
        }

        // 짝수, 홀수
        int cnt = 0;
        if (evenIdx > oddIdx) { // 2 | 1 | 2, 2, 2, 2, 2, 2, 2, 2, 2, 2
            cnt = oddIdx * 2 + 1;
        } else if (evenIdx < oddIdx) { // 2 | 1 | 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1
            // 마지막 짝수, 홀수 쌍까지 묶음 개수
            cnt = evenIdx * 2;

            // 남은 홀수를 사용해 만들 수 있는 최대 묶음 수
            int restOdd = oddIdx - evenIdx;
            int oddGroupCnt = restOdd / 3 * 2;
            int restOfRest = restOdd - oddGroupCnt / 2 * 3;

            if (restOfRest % 3 == 0) { // (1, 1) | (1) | (1, 1) | (1) | (1, 1), (1)
                cnt += oddGroupCnt;
            } else if (restOfRest % 3 == 1) { // (1, 1), (1) | (1, 1), (1) | (1)
                cnt += oddGroupCnt - 1;
            } else {    // (1, 1), (1) | (1, 1), (1) | (1, 1)
                cnt += oddGroupCnt + 1;
            }
        } else { // 2 | 1 | 2 | 1
            cnt = oddIdx * 2;
        }

        System.out.println(cnt);
        
    }
}