import java.util.Scanner;
import java.util.Arrays;

class Elem implements Comparable<Elem> {
    int idx;
    int value;

    public Elem(int idx, int value) {
        this.idx = idx;
        this.value = value;
    }

    public int compareTo(Elem e) {
        if (this.value != e.value)
            return this.value - e.value;
        return this.idx - e.idx;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[n];
        for(int i = 0; i < n; i++){
            arr[i] = sc.nextInt();
        }
        
        Elem[] elems = new Elem[n];
        for (int i = 0; i < n; i++) {
            elems[i] = new Elem(i + 1, arr[i]);
        }

        Arrays.sort(elems);

        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            answer[elems[i].idx - 1] = i + 1;
        }

        for (int i = 0; i < n; i++) {
            System.out.print(answer[i] + " ");
        }
    }
}