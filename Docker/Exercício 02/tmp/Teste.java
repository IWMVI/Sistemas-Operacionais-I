import java.util.Scanner;
    
    public class Teste {
        public static void main(String[] args){
            Scanner sc = new Scanner(System.in);
            System.out.print("Informe o 1 numero inteiro: ");
            int a = sc.nextInt();
            System.out.print("Informe o 2 numero inteiro: ");
            int b = sc.nextInt();
            int res = a + b;
            System.out.println("Soma = " + res);
            sc.close();
        }
    }