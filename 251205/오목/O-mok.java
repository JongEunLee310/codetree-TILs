import java.util.Scanner;

public class Main {
    public static boolean inRange(int x, int y) {
        return (0 <= x && x < 19 && 0 <= y && y < 19);
    }

    public static int[] getContinuousStones(int[][] arr, int s, int i, int j) {
        int[] dx = new int[]{0, 1, 1, 1, 0, -1, -1, -1};
        int[] dy = new int[]{1, 1, 0, -1, -1, -1, 0, 1};
        int dirNum = 0;

        int cnt = 1;
        int[] result = new int[3]; 
        for (int d = 0; d < 8; d++) {
            for (int dist = 1; dist < 5; dist++) {
                int nx = i + dx[dirNum] * dist;
                int ny = j + dy[dirNum] * dist;

                if (inRange(nx, ny) && arr[nx][ny] == s) {
                    cnt++;
                } else {
                    cnt = 1;
                    dirNum++;
                    break;
                }
            }

            if (cnt == 5) {
                result[0] = cnt;
                result[1] = i + dx[dirNum] * 2 + 1;
                result[2] = j + dy[dirNum] * 2 + 1;
                System.out.println(i + " " + j + " " + dirNum);
                break;
            }
        }
        
        return result;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[][] arr = new int[19][19];
        for (int i = 0; i < 19; i++) {
            for (int j = 0; j < 19; j++) {
                arr[i][j] = sc.nextInt();
            }
        }
        
        int answer = 0;
        int[] coor = new int[2];
        for (int s = 1; s <= 2; s++) {
            for (int i = 0; i < 19; i++) {
                for (int j = 0; j < 19; j++) {
                    if (arr[i][j] == 0) {
                        continue;
                    }

                    int[] result = getContinuousStones(arr, s, i, j);
                    if (result[0] == 5) {
                        answer = s;
                        coor[0] = result[1];
                        coor[1] = result[2];
                        break;
                    }
                }
                if (answer > 0) {
                    break;
                }
            }
            if (answer > 0) {
                break;
            }
        }
        System.out.println(answer);
        if (answer != 0) {
            System.out.println(coor[0] + " " + coor[1]);
        }
    }
}