package br.com.fiap.exercicio.model;

public class Cor {
    String nome;
    private int r, g, b;

    public int getR() {
        return r;
    }

    public void setR(int r) {
        this.r = r;
    }

    public int getG() {
        return g;
    }

    public void setG(int g) {
        this.g = g;
    }

    public int getB() {
        return b;
    }

    public void setB(int b) {
        this.b = b;
    }

    public void alterarCor(int r, int g, int b, String nome){
        this.r = r;
        this.g = g;
        this.b = b;
        this.nome = nome;
    }

}
