import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        /* Scanner인 객체 sc를 만든다 = 객체 sc는 시스템이 입력을 받을 수 있는 새로운 Scanner*/
        int a = sc.nextInt();
        System.out.printf("Your score is %d point.", a);
    }
}