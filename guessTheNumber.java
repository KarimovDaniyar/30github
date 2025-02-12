import java.util.Scanner;

public class guessTheNumber {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        boolean cont = true;
        while(cont){
            int randomNum = (int)(Math.random()*101);
            int c = 0;
            boolean quessed = false;
            System.out.println("Угадайте число от 0 до 100");
            System.out.println("Ваше предположение: ");
            while(!quessed) {
                int n = scanner.nextInt();
                c++;

                if (n == randomNum) {
                    System.out.println("Вы угадали");
                    System.out.println("c " + c + " попытки");
                    quessed = true;
                } else if (n < randomNum) {
                    System.out.println("Берите выше");
                } else{
                    System.out.println("Берите ниже");
                }
            }
            System.out.println("Хотите продолжить ? ");
            String answer = scanner.next();
            if (!answer.equalsIgnoreCase("Да")) {
                cont = false;
                System.out.println("До встречи ");
            }
        }
        scanner.close();
    }
}
