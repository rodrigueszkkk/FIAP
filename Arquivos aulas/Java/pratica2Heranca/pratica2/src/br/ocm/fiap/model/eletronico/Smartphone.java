package br.ocm.fiap.model.eletronico;

import br.com.fiap.tds.model.produto.Produto;

public class Smartphone extends Produto {
    private String modelo;
    private String fabricante;
    private int memoria;

    public Smartphone(int codigo, String modelo) {
        super(codigo);
        this.modelo = modelo;
    }

    public Smartphone(int codigo, String fabricante, String modelo) {
        super(codigo);
        this.fabricante = fabricante;
        this.modelo = modelo;
    }
}
