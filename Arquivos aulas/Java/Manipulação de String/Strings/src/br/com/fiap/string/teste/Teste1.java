package br.com.fiap.string.teste;

import java.sql.SQLOutput;

public class Teste1 {

    public static void main(String[] args) {
        //declarar uma String

        String nome = "Kaiky\nPereira";
        double preco = 15;
        //concatenacao de string ou outro tipo numerico
        String produto = nome + ", " + preco;

        System.out.println(produto);
    }
}
