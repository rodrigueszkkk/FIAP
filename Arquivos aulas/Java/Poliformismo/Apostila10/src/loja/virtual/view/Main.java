package loja.virtual.view;

import loja.virtual.models.Alimento;
import loja.virtual.models.Eletronico;
import loja.virtual.models.Produto;

public class Main {
    public static void main(String[] args) {

        Alimento alimento = new Alimento();
        Eletronico eletronico = new Eletronico();
        Produto produto = new Produto();

        produto.setPreco(100);
        System.out.println(produto.calcularDesconto(""));

        alimento.setPreco(50);
        System.out.println(alimento.calcularDesconto("FIAP20"));


        Produto churros = new Alimento();


    }
}
