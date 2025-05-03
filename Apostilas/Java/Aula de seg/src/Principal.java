import java.util.Scanner;

public class Principal {

    public static void main(String[] args) {

        //criar leitor para ler dados inseridos
        Scanner leitor = new Scanner(System.in);

        System.out.println("Qual o nome do produto");
        String nome = leitor.next() + leitor.nextLine();

        System.out.println("Qual o código do produto?");
        int codigo = leitor.nextInt();

        System.out.println("Qual o preço do produto");
        float preco = leitor.nextFloat();

        System.out.println("O item está disponivel? true ou false");
        boolean disponivel = leitor.nextBoolean();

        //ler dados do fornecedor

        System.out.println("Qual o nome da empresa do fornecedor: ");
        String empresa = leitor.next() + leitor.nextLine();

        System.out.println("Qual o telefone do fornecedor? ");
        String telefone = leitor.next();

        System.out.println("Qual o Cnpj da empresa? ");
        String cnpj = leitor.next();

        //criar objeto
        Produtos produto = new Produtos();
        Fornecedor fornecedor = new Fornecedor();

        //inserir dados no produto
        produto.nome = nome;
        produto.codigo = codigo;
        produto.preco = preco;
        produto.disponivel = disponivel;

       produto.fornecedor = fornecedor;

        fornecedor.nome = empresa;
        fornecedor.telefone = telefone;
        fornecedor.cnpj = cnpj;


        System.out.println(fornecedor);
        System.out.println(produto);


        System.out.println(
                "Nome do produto: " + produto.nome + "\n"
                        + "Código do produto: " + produto.codigo + "\n"
                        + "Preço do produto: " + produto.preco + "\n"
                        + "Disponibilidade: " + produto.disponivel
        );
        System.out.println( "\n" +
                "Nome do fornecedor: " + fornecedor.nome + "\n"
                + "Telefone do fornecedor: " + fornecedor.telefone + "\n"
                + "Cnpj do fornecedor: " + fornecedor.cnpj + "\n"
        );
        produto.aumentarPreco(20);
        System.out.println(produto.preco);

        produto.descontoPreco(20);
        System.out.println(produto.desc);
    }

}
