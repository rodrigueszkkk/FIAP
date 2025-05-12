package br.com.fiap.string.teste;

import java.util.Scanner;

public class Maiuscula {

    public static void main(String[] args) {

        Scanner leitor = new Scanner(System.in);

        System.out.println("Digite seu Nome");
        String nomeCompleto = leitor.nextLine();

        String nomeMaiusculo = nomeCompleto.toUpperCase();

        System.out.println("Pós formatação: " + nomeMaiusculo);
    }
}
