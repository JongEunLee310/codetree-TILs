import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        
        int[] dx = new int[]{1, 0, -1, 0};
        int[] dy = new int[]{0, -1, 0, 1};
        int[] curLoc = new int[]{0, 0};
        int dirNum = 3;

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'L') {
                dirNum = (dirNum + 3) % 4;
            } else if (s.charAt(i) == 'R') {
                dirNum = (dirNum + 1) % 4;
            } else {
                curLoc[0] += dx[dirNum];
                curLoc[1] += dy[dirNum];
            }
        }

        System.out.println(curLoc[0] + " " + curLoc[1]);
    }
}