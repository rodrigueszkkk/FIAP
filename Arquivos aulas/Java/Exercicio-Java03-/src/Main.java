import java.lang.ref.Cleaner;
import java.util.Arrays;
import java.util.Scanner;

public class Main{

    public static void main(String[] args) {
        //Instanciar o aluno (transformar a classe em um objeto)
        //Ler os dados do aluno
        Scanner leitor = new Scanner(System.in);

        Endereco endereco = new Endereco(); // instanciamento de classe na memória
        Cliente cliente = new Cliente();
        ContaCorrente contaCorrente = new ContaCorrente();

        //dados endereço
        System.out.println("Digite o logradouro: ");
        endereco.logradouro = leitor.nextLine();

        System.out.println("Digite seu numero: ");
        endereco.numero = leitor.nextShort();
        leitor.nextLine();

        System.out.println("Complemento: ");
        endereco.complemento = leitor.nextLine();

        System.out.println("Digite seu cep: ");
        endereco.cep = leitor.nextLine();

        System.out.println("========Cliente========");

        System.out.println("Digite seu nome: ");
        cliente.nome = leitor.nextLine();

        System.out.println("Digite seu CPF: ");
        cliente.cpf = leitor.nextLine();

        cliente.endereco = endereco; //atribuindo o endereco da classe endereco

        System.out.println("=====Conta Corrente=====");

        System.out.println("Digite seu Saldo");
        contaCorrente.saldo = leitor.nextDouble();

        contaCorrente.titular = cliente; // Atribuindo titular na contaCorrente

        System.out.println("Valor a depositar na conta corrente");
        double saldoADepositar = leitor.nextDouble(); // definindo uma variavel

        contaCorrente.depositar(saldoADepositar); //chamando o metodo

        System.out.println("Novo saldo: " + contaCorrente.retornarSaldo());

        System.out.println("Valor a retirar na conta corrente");
        double saldoARetirar = leitor.nextDouble();

        contaCorrente.retirar(saldoARetirar);

        System.out.println("Novo saldo: " + contaCorrente.retornarSaldo());

        System.out.println("=====Dados do Cliente=====");
        System.out.println(cliente.retornarDados());

        System.out.println("=====Endereco do cliente=====");
        System.out.println(cliente.endereco.retornarEndereco());
    }
}