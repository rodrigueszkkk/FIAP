package br.com.fiap.esporte.view;

import br.com.fiap.esporte.model.Endereco;
import br.com.fiap.esporte.model.Pessoa;
import br.com.fiap.esporte.model.PessoaFisica;

public class Teste {
    public static void main(String[] args) {

        PessoaFisica pf = new PessoaFisica("popada");


        pf.setNome("Kaiky");
        pf.setCpf("129783");
        pf.setEmail("kaiky@fiap.com.br");
        pf.setIdade(18);
        pf.setAposentado(false);


        Endereco endereco = new Endereco();
        endereco.setNumero("1100");
        endereco.setLogradouro("Av. Paulista");
        pf.setEndereco(endereco);

        System.out.println(pf.getNome());
        System.out.println(pf.getCpf());
        System.out.println(pf.getEmail());
        System.out.println(pf.getIdade());
        System.out.println(pf.isAposentado());
        System.out.println(pf.getEndereco().getLogradouro() + ", " + pf.getEndereco().getNumero());
    }
}
