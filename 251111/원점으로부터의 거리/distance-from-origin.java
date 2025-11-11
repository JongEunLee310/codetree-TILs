import java.util.Scanner;
import java.util.Arrays;

class Point implements Comparable<Point> {
    int num;
    int x;
    int y;

    public Point(int num, int x, int y) {
        this.num = num;
        this.x = x;
        this.y = y;
    }

    @Override
    public int compareTo(Point point) {
        if (Math.abs(this.x) + Math.abs(this.y) == Math.abs(point.x) + Math.abs(point.y)) {
            return this.num - point.num;
        }
        return (Math.abs(this.x) + Math.abs(this.y)) - (Math.abs(point.x) + Math.abs(point.y));
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[][] points = new int[n][2];
        for (int i = 0; i < n; i++) {
            points[i][0] = sc.nextInt();
            points[i][1] = sc.nextInt();
        }
        
        Point[] point = new Point[n];
        for (int i = 0; i < n; i++) {
            point[i] = new Point(i + 1, points[i][0], points[i][1]);
        }

        Arrays.sort(point);

        for (int i = 0; i < n; i++) {
            System.out.println(point[i].num);
        }
    }
}