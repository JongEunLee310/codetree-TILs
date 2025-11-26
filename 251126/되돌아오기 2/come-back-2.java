import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String commands = sc.next();
        
        int[] dx = new int[]{0, 1, 0, -1};
        int[] dy = new int[]{1, 0, -1, 0};
        int dirNum = 1;
        int[] curLoc = new int[]{0, 0};

        int answer = -1;
        for (int i = 0; i < commands.length(); i++) {
            if (commands.charAt(i) == 'F') {
                curLoc[0] += dx[dirNum];
                curLoc[1] += dy[dirNum];
            } else if (commands.charAt(i) == 'R') {
                dirNum = (dirNum + 1) % 4;
            } else if (commands.charAt(i) == 'L') {
                dirNum = (dirNum + 3) % 4;
            }

            if (curLoc[0] == 0 && curLoc[1] == 0) {
                answer = i + 1;
                break;
            }
        }

        System.out.println(answer);
    }
}