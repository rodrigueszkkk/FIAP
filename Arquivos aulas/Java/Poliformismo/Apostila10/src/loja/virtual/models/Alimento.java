package loja.virtual.models;

import java.time.LocalDate;

public class Alimento extends Produto{
    private LocalDate vencimento;

    public Alimento(int codigo, String descricao, double preco, LocalDate vencimento) {
        super(codigo, descricao, preco);
        this.vencimento = vencimento;
    }

    @Override
    public String toString() {
        return super.toString() + "\n Vencimento " + getVencimento();
    }

    @Override // modificando o metodo pai
    public double calcularDesconto() {
        return calcularDesconto(15);
    }

    public double calcularDesconto(String cupom) {
        if (cupom.equals("FIAP40"))
            return super.calcularDesconto(40);
        return super.calcularDesconto(cupom);

    }

    // modificando o metodo pai


    public LocalDate getVencimento() {
        return vencimento;
    }

    public void setVencimento(LocalDate vencimento) {
        this.vencimento = vencimento;
    }
}
