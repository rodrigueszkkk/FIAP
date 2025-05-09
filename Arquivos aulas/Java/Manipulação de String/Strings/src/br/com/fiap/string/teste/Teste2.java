package br.com.fiap.string.teste;

public class Teste2 {
    public static void main(String[] args) {
        String email = "churros@fiap.com.br";
        String confirmarEmail = new String("churros@fiap.com.br");

        //validar se emails sao iguais
        //equal verificar o valor da String
        if (email.equals(confirmarEmail)){
            System.out.println("Email confirmado");
        } else {
            System.out.println("nao sao iguais");
        }

        //exibir caracteres do email

        System.out.println(email + " contem " + email.length() + " letras");

        //exibir a posicao do @
        int posicao = email.indexOf('@');

        System.out.println("o caracter: '@' esta na posicao: " + email.indexOf('@'));

        //exibir o email sem dominio

        String semDominio = email.substring(0, posicao);

        System.out.println("Sem dominio: " + semDominio);

        //exibir dominio

        String comDominio = email.substring(posicao);

        System.out.println("Dominio email: " + comDominio);
    }
}
