import java.util.Scanner;
import java.util.Arrays;

class Person {
    String name;
    int height;
    double weight;

    public Person(String name, int height, double weight) {
        this.name = name;
        this.height = height;
        this.weight = weight;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = 5;
        String[] names = new String[n];
        int[] heights = new int[n];
        double[] weights = new double[n];
        for (int i = 0; i < n; i++) {
            names[i] = sc.next();
            heights[i] = sc.nextInt();
            weights[i] = sc.nextDouble();
        }

        Person[] p = new Person[n];
        for (int i = 0; i < n; i++) {
            p[i] = new Person(names[i], heights[i], weights[i]);
        }

        Arrays.sort(p, (a, b) -> a.name.compareTo(b.name));
        System.out.println("name");
        for (int i = 0; i < n; i++) {
            System.out.printf("%s %d %.1f\n", p[i].name, p[i].height, p[i].weight);
        }

        Arrays.sort(p, (a, b) -> b.height - a.height);
        System.out.println("\nheight");
        for (int i = 0; i < n; i++) {
            System.out.printf("%s %d %.1f\n", p[i].name, p[i].height, p[i].weight);
        }
    }
}