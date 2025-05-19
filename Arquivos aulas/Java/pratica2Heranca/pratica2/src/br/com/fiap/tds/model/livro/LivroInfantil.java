package br.com.fiap.tds.model.livro;

public class LivroInfantil extends Livro{
    private String ilustrador;

    public LivroInfantil(int codigo, String titulo) {
        super(codigo, titulo);
        this.ilustrador = ilustrador;
    }
}
