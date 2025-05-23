package loja.virtual.view;

import loja.virtual.models.Alimento;
import loja.virtual.models.Eletronico;
import loja.virtual.models.Produto;

import java.time.LocalDate;

public class Main {
    public static void main(String[] args) {

        Alimento alimento = new Alimento(31, "isso ai", 50, LocalDate.of(2024, 4, 2));
        Eletronico eletronico = new Eletronico(1, "sim", 123);
        Produto produto = new Produto(412, "POpada", 100);

        System.out.println(produto.calcularDesconto("FIAP20"));

        System.out.println(alimento.calcularDesconto("FIAP40"));



        System.out.println(produto);
        System.out.println(alimento);
    }
}
