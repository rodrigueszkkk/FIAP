import java.util.Scanner;

public class Tarefa2 {
    public static void main(String[] args) {
        // ler o nome de um produto, quantidade e valor
        // ler desconto, calcular o valor
        // valor total: "Produto x, y itens, valor total: R$xxx"
        Scanner leitor = new Scanner(System.in);
        System.out.println("Qual seu nome?");
        String nome = leitor.next() + leitor.nextLine();

        System.out.println("OK " + nome + " Diga o nome do produto");
        String product = leitor.next() + leitor.nextLine();

        System.out.println("Certo! Qual seria o preço e a quantidade respectivamente?");
        double price = leitor.nextFloat();
        double quant = leitor.nextFloat();

        System.out.println("Qual foi o desconto concebido (em Porcentagem Ex. 30 = 30%)?");
        double desc = leitor.nextFloat();

        double preco = price * quant; // multiplica o preco pela quantidade
        double descFinal = preco - ((desc / 100) * preco); // converte a % e ja calcula o desconto junto

        System.out.println("Ok, " + nome + " seu item: " + product + " fica: R$" + descFinal + " já com descontos aplicados!");
    }

}
