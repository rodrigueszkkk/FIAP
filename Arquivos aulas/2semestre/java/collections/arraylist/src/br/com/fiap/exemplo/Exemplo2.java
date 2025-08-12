package br.com.fiap.exemplo;

import br.com.fiap.model.Fruta;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Exemplo2 {

    public static void main(String[] args) {
        Scanner leitor = new Scanner(System.in);

        //Criar uma lista de frutas
        List<String> frutas = new ArrayList<>();

        //Pedir para o usuario inserir uma fruta na lista
        System.out.println("Deseja, ver a lista ou adicionar frutas?");
        int i = leitor.nextInt();

        if (i == 1) {
            for (int a = 0; i < frutas.size(); a++){
                System.out.println("Posição: " + a + " - " + frutas.get(a));
            }
        }
        while ( i != 0 ) {



            System.out.println("Qual o nome da fruta?");
            String nome = leitor.nextLine();

            System.out.println("cor dela");
            String cor = leitor.nextLine();

            System.out.println("Valor dela");
            double preco = leitor.nextDouble();


            Fruta f = new Fruta(nome, cor, preco);
            frutas.add(String.valueOf(f));

        }


        //Exibir todas as frutas da lista

    }
}