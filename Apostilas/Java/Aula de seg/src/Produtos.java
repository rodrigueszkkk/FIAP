public class Produtos {
    //Atributos

    String nome;
    int codigo;
    float preco;
    float desc;
    boolean disponivel;
    Fornecedor fornecedor;

    //Métodos
    //Criar uma Função que aumenta o preço em porcentagem
    void aumentarPreco(float porcentagem){
        preco += preco * porcentagem/100;
    }

    //Método que calcula o produto com um desconto no valor
    void descontoPreco(float porcentagem){
        desc = preco - (preco * porcentagem/100);

    // calcua
    }
}
