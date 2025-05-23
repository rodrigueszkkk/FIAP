package loja.virtual.models;

public class Produto {
    private int codigo;
    private String descricao;
    private double preco;



    public double calcularDesconto(double porcentagem){
        return preco - preco * (porcentagem/100);

    }

    public double calcularDesconto(){
        return calcularDesconto(5);
    }

    public double calcularDesconto(String cupom){
        if (cupom.equals("FIAP10"))
           return calcularDesconto(10);
        else if (cupom.equals("FIAP20"))
           return calcularDesconto(20);
         else return preco;
    }
    //recebe String cupom FIAP10 -> 10% desconto FIAP20 -> 20%
    // sobrescrita no metro na calsse alimento
    //recebe String cupom FIAP10 -> 10% desconto FIAP20 -> 20% FIAP 40% ->


    public int getCodigo() {
        return codigo;
    }

    public void setCodigo(int codigo) {
        this.codigo = codigo;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }
}
