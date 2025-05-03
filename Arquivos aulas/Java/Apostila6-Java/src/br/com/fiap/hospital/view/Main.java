package br.com.fiap.hospital.view;

import br.com.fiap.hospital.model.Medico;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        //intanciad do medico e construtor
        Medico medico = new Medico("Drauzio", 312, "sexo", true);

        Scanner leitor = new Scanner(System.in);

        //Exibir os valores dos atributos do médico

        System.out.println("Digite o nome do Médico");
        medico.setNome(leitor.nextLine());
        System.out.println("Digite o crm do Médico");
        medico.setCrm(leitor.nextInt());
        System.out.println("Digite as Especialidades do médico");
        medico.setEspecialidades(leitor.nextLine());
        System.out.println("Digite o status do Médico");
        medico.setAtivo(leitor.nextBoolean());

    }
}
