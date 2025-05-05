import java.util.Scanner;

public class Teste {
    public static void main(String[] args) {

        Scanner leitor = new Scanner(System.in);

        TesteTamanho pessoa1 = new TesteTamanho("Gabriel",
                70,
                1.80,
                18);

        TesteTamanho pessoa2 = new TesteTamanho("Kaiky",
                1.70,
                60,
                20);

        if(pessoa2.getPeso() > pessoa1.getPeso()){

            System.out.println("Kaka é gordo");
        } else {
            System.out.println("Biel é gordo");
        }

        if (pessoa2.getAltura() > pessoa1.getPeso()){
            System.out.println("Kaiky é maior que que biel");
        }else {
            System.out.println("Biel é maior que kaka");
        }
    }
}