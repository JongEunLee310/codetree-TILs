import java.util.Scanner;
public class Main {
    public static int getDir(char d) {
        int dirNum = 0;

        if (d == 'N') {
            dirNum = 1;
        } else if (d == 'S') {
            dirNum = 3;
        } else if (d == 'E') {
            dirNum = 0;
        } else if (d == 'W') {
            dirNum = 2;
        }
        
        return dirNum;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[] dx = new int[]{0, 1, 0, -1};
        int[] dy = new int[]{1, 0, -1, 0};
        int[] curLoc = new int[]{0, 0};

        int answer = -1;
        int t = 0;
        for(int i = 0; i < n; i++){
            char dir = sc.next().charAt(0);
            int dist = sc.nextInt();
            int dirNum = getDir(dir);

            for (int j = 0; j < dist; j++) {
                curLoc[0] = curLoc[0] + dx[dirNum];
                curLoc[1] = curLoc[1] + dy[dirNum];
                t++;

                if (curLoc[0] == 0 && curLoc[1] == 0) {
                    answer = t;
                    break;
                }
            }
            if (answer != -1) {
                break;
            }
        }
        
        System.out.println(answer);
    }
}