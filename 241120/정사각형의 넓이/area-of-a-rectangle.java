import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int w = n*n;

        if (n<5){
            System.out.println(w);
            System.out.println("tiny");
        }
        else{
            System.out.println(w);
        }
        
   
    }
}