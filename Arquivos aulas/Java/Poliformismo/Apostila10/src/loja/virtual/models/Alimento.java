package loja.virtual.models;

import java.time.LocalDate;

public class Alimento extends Produto{
    private LocalDate vencimento;

    @Override // modificando o metodo pai
    public double calcularDesconto() {
        return calcularDesconto(15);
    }

    @Override
    public double calcularDesconto(String cupom){
        if (cupom.equals("FIAP10")){
            return calcularDesconto(10);
        } else if (cupom.equals("FIAP20")) {
            return calcularDesconto(20);
        } else if (cupom.equals("FIAP40")) {
            return calcularDesconto(40);
        } else return getPreco();

    }

    // modificando o metodo pai


    public LocalDate getVencimento() {
        return vencimento;
    }

    public void setVencimento(LocalDate vencimento) {
        this.vencimento = vencimento;
    }
}
