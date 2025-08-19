import java.util.Scanner;
import java.util.Arrays;

class Loc {
    String name;
    String address;
    String region;

    public Loc() {
        this.name = "";
        this.address = "";
        this.region = "";
    }

    public Loc(String name, String address, String region) {
        this.name = name;
        this.address = address;
        this.region = region;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[] names = new String[n];
        String[] addresses = new String[n];
        String[] regions = new String[n];
        for (int i = 0; i < n; i++) {
            names[i] = sc.next();
            addresses[i] = sc.next();
            regions[i] = sc.next();
        }

        Loc[] locs = new Loc[n];
        for (int i = 0; i < n; i++) {
            locs[i] = new Loc(names[i], addresses[i], regions[i]);
        }

        int latestIdx = 0;
        for (int i = 1; i < n; i++) {
            if (locs[i].name.compareTo(locs[latestIdx].name) > 0) {
                latestIdx = i;
            }
        }

        System.out.println("name " + locs[latestIdx].name);
        System.out.println("addr " + locs[latestIdx].address);
        System.out.println("city " + locs[latestIdx].region);

    }
}