import java.util.Scanner;

public class LeituraDados {

    public static void main(String[] args) {
        //Objeto responsavel por ler dados inseridos no tclado
        Scanner leitor = new Scanner(System.in);
        //ler um float e colocar em "nota"
        System.out.println("Digite uma nota: ");
        float nota = leitor.nextFloat();

        System.out.println("sua nota é: " + nota);
    }

}
