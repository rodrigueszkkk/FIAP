import java.util.Scanner;

public class TesteEleitores {

    public static void main(String[] args) {

        Scanner leitor = new Scanner(System.in);

        //Pessoa 1
        System.out.println("=====Primeira Pessoa=====");

        System.out.println("Digite o nome da primeira pessoa: ");
        String nomePessoa1 = leitor.nextLine();

        System.out.println("Digite o nome da segunda pessoa: ");
        int idadePessoa1 = Integer.valueOf(leitor.nextLine()); //convertor

        System.out.println("Digite a altura da primeira pessoa: ");
        double alturaPessoa1 = Double.parseDouble(leitor.nextLine()); //conversor

        System.out.println("Digire o pesso da primeira pessoa: ");
        double pesoPessoa1 = leitor.nextDouble();

        //Pessoa 2
        System.out.println("=====Segunda Pessoa=====");

        System.out.println("Digite o nome da primeira pessoa: ");
        String nomePessoa2 = leitor.nextLine();

        System.out.println("Digite o nome da segunda pessoa: ");
        int idadePessoa2 = Integer.valueOf(leitor.nextLine());

        System.out.println("Digite a altura da primeira pessoa: ");
        double alturaPessoa2 = leitor.nextDouble();

        System.out.println("Digire o pesso da primeira pessoa: ");
        double pesoPessoa2 = leitor.nextDouble();

        //Pessoa 3
        System.out.println("=====Terceira Pessoa=====");

        System.out.println("Digite o nome da primeira pessoa: ");
        String nomePessoa3 = leitor.nextLine();

        System.out.println("Digite o nome da segunda pessoa: ");
        int idadePessoa3 = Integer.valueOf(leitor.nextLine());

        System.out.println("Digite a altura da primeira pessoa: ");
        double alturaPessoa3 = leitor.nextDouble();

        System.out.println("Digire o pesso da primeira pessoa: ");
        double pesoPessoa3 = leitor.nextDouble();

        TesteTamanho pessoa1 = new TesteTamanho(nomePessoa1, pesoPessoa1, alturaPessoa1, idadePessoa1);
        TesteTamanho pessoa2 = new TesteTamanho(nomePessoa2, pesoPessoa2, alturaPessoa2, idadePessoa2);
        TesteTamanho pessoa3 = new TesteTamanho(nomePessoa3, pesoPessoa3, alturaPessoa3, idadePessoa3);

        if (pessoa1.getIdade() < 16 ){
            System.out.println(pessoa1.getNome() + " Não é eleitor");
        } else if (pessoa1.getIdade() > 16 || pessoa1.getIdade() < 65){
            System.out.println(pessoa1.getNome() + "É eleitor facultativo");
        } else {
            System.out.println(pessoa1.getNome() + " É eleitor obrigatório");
        }

        if (pessoa2.getIdade() < 16 ){
            System.out.println(pessoa2.getNome() + " Não é eleitor");
        } else if (pessoa2.getIdade() > 16 || pessoa2.getIdade() < 65){
            System.out.println(pessoa2.getNome() + "É eleitor facultativo");
        } else {
            System.out.println(pessoa2.getNome() + " É eleitor obrigatório");
        }

        if (pessoa3.getIdade() < 16 ){
            System.out.println(pessoa3.getNome() + " Não é eleitor");
        } else if (pessoa3.getIdade() > 16 || pessoa3.getIdade() < 65){
            System.out.println(pessoa3.getNome() + "É eleitor facultativo");
        } else {
            System.out.println(pessoa3.getNome() + " É eleitor obrigatório");
        }
    }
}
