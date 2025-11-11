import java.util.Scanner;
import java.util.Arrays;

class Student implements Comparable<Student> {
    int height;
    int weight;
    int num;

    public Student(int height, int weight, int num) {
        this.height = height;
        this.weight = weight;
        this.num = num;
    }

    @Override
    public int compareTo(Student s) {
        if (this.height == s.height) 
            return s.weight - this.weight;
        return this.height - s.height;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        Student[] students = new Student[n];
        for (int i = 0; i < n; i++) {
            int height = sc.nextInt();
            int weight = sc.nextInt();
            students[i] = new Student(height, weight, i + 1);
        }
        
        Arrays.sort(students);
        for (int i = 0; i < n; i++) {
            System.out.printf("%d %d %d\n", students[i].height, students[i].weight, students[i].num);
        }
    }
}