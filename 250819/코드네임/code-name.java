import java.util.Scanner;

class Agent {
    String codeName;
    int score;

    public Agent() {
        this.codeName = "";
        this.score = 0;
    }

    public Agent(String codeName, int score) {
        this.codeName = codeName;
        this.score = score;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Agent[] agents = new Agent[5];
        
        for (int i = 0; i < 5; i++) {
            String codeName = sc.next();
            int score = sc.nextInt();
            agents[i] = new Agent(codeName, score);
        }

        int minIdx = 0;
        for (int i = 1; i < 5; i++) {
            if (agents[i].score < agents[minIdx].score) {
                minIdx = i;
            }
        }

        System.out.println(agents[minIdx].codeName + " " + agents[minIdx].score);
    }
}