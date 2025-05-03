import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);

        Cliente cliente = new Cliente();
        ContaCorrente contaCorrente = new ContaCorrente();
        Endereco endereco = new Endereco();

        System.out.println("Faça seu cadastro antes de iniciarmos!");
        System.out.println("Digite seu nome: ");
        String nome = leitor.next() + leitor.nextLine();

        System.out.println("Qual seu cpf? ");
        String cpf = leitor.next();

        System.out.println("Quanto gostaria de depositar em sua conta? ");
        double saldo = leitor.nextDouble();

        System.out.println("Seu saldo atual é de: " + contaCorrente.retornarSaldo());

        System.out.println("Gostaria de retirar alguma quantia? ");
        double saldo = leitor.nextDouble();


        cliente.nome = nome;
        cliente.cpf = cpf;

        contaCorrente.saldo = saldo;
        contaCorrente.titular = cliente;

        contaCorrente.depositar();
        contaCorrente.retirar();
        contaCorrente.retornarSaldo();

        System.out.println("Seu saldo atual é de: " + contaCorrente.retornarSaldo());


    }
}