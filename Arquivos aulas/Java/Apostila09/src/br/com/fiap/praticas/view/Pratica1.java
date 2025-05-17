package br.com.fiap.praticas.view;

import br.com.fiap.praticas.model.Aviao;
import br.com.fiap.praticas.model.Carro;
import br.com.fiap.praticas.model.Lancha;

import java.util.Scanner;

public class Pratica1 {
    public static void main(String[] args) {

        Scanner leitor = new Scanner(System.in);

        Carro carro = new Carro("uou");
        Aviao aviao = new Aviao();
        Lancha lancha = new Lancha();


        System.out.println("Quais dos veiculos abaixo gostaria de cadastrar?");
        System.out.println("\n 1- Carro \n 2- Aviao \n 3- lancha");

        int opcao = leitor.nextInt();

            if (opcao == 1){
            System.out.println("Qual o modelo?");
            carro.setModelo(leitor.nextLine());
            System.out.println("Qual a placa do veiculo?");
            carro.setPlaca(leitor.nextLine());




            }

}}
