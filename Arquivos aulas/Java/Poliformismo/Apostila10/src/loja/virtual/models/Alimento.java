package loja.virtual.models;

import java.time.LocalDate;

public class Alimento extends Produto{
    private LocalDate vencimento;

    public LocalDate getVencimento() {
        return vencimento;
    }

    public void setVencimento(LocalDate vencimento) {
        this.vencimento = vencimento;
    }
}
