package br.com.fiap.tds.model.livro;

import br.com.fiap.tds.model.produto.Produto;

public class Livro extends Produto {
    private String autor;
    private String titulo;
    private String isbn;
    private Editora editora;


    public Livro(int codigo, String titulo) {
        super(codigo);
        this.titulo = titulo;
    }

    public Livro(int codigo, String titulo, Editora editora) {
        super(codigo);
        this.titulo = titulo;
        this.editora = editora;
    }
}
