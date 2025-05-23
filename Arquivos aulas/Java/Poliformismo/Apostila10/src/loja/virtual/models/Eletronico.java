package loja.virtual.models;

public class Eletronico extends Produto{
    private int voltagem;

    public Eletronico(int codigo, String descricao, double preco) {
        super(codigo, descricao, preco);
    }

    public int getVoltagem() {
        return voltagem;
    }

    public void setVoltagem(int voltagem) {
        this.voltagem = voltagem;
    }
}
