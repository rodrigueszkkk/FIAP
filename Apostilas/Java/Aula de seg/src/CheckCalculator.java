import java.util.Scanner;

public class CheckCalculator {

    public static void main(String[] args) {
        // "puxa" uma função de ler inputs
        Scanner leitor = new Scanner(System.in);

        System.out.println("Ola, Digite seu Nome Para iniciarmos: ");
        String nome = leitor.next() + leitor.nextLine(); //amarzena o nome nxt line para receber mais de uma palavra

        System.out.println("Ola " + nome + " Quais foram as suas 2 maiores notas chekpoint?");
        double cp1 = leitor.nextFloat(); // amarzena nota cp1
        double cp2 = leitor.nextFloat(); // amarzena nota cp2

        System.out.println("Certo! agora informe sua nota do challenge!");
        double challenge = leitor.nextFloat(); // amarzena challenge

        System.out.println("E por fim, sua nota da Global Solution!");
        double gs = leitor.nextFloat(); // amarzena gs

        double mediaCP = (cp1 + cp2) / 2; // calculo da média chk

        double media = gs * 0.6 + mediaCP * 0.2 + challenge * 0.2; // calcula da média total

        System.out.println("Ok " + nome + " Sua média final é: " + media); // mostra o resultado final


    }
}
