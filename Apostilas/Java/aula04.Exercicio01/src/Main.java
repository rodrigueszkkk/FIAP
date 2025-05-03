import br.com.fiap.exercicio.model.Cor;
import br.com.fiap.exercicio.model.Lancha;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

    Cor cor = new Cor();
    cor.alterarCor(255, 0, 0, "Vermelho");

    Lancha lancha = new Lancha();
    lancha.setModelo("Veleiro");
    lancha.setCor(cor);
    lancha.setComprimento(10);
    lancha.setAnoFabricacao(2025);
    lancha.setQuantidadeLugares(8);

        System.out.println("Lancha: " + lancha.getModelo());
        System.out.println("");
        System.out.println(cor);



    }
}