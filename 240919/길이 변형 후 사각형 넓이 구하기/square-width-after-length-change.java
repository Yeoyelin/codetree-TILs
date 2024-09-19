import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int ga = sc.nextInt();
        int se = sc.nextInt();
        
        System.out.println((ga + 8));
        System.out.println((se * 3));
        System.out.println(((ga + 8)*(se * 3)));
    }
}